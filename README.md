# BioRisk Sentinel

BioRisk Sentinel is a student cybersecurity assessment tool for evaluating the reliability, privacy controls, and attack resistance of biometric authentication systems. It accepts only fictional or synthetic, aggregated assessment data. It must never receive or store biometric samples, templates, passwords, banking records, or personal customer data.

## Local setup

1. Create and activate a Python virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and set a local secret key.
4. Run `python app.py`.
5. Open `http://127.0.0.1:5000` and verify `http://127.0.0.1:5000/health` returns an OK response.

The SQLite database is created automatically at `instance/biorisk.db` on first run.

## Current backend scope

The initial data model supports users, assessments, reliability metrics, privacy controls, attack test results, findings, and audit logs. The deterministic scoring service and its unit tests are also included.

Authentication currently supports assessor registration, sign-in, sign-out, and a protected assessment workspace. Public registration always creates an `assessor`; it never accepts a role supplied by the browser. Create an administrator only from a trusted local terminal:

```powershell
flask --app app create-admin
```

The command prompts for the administrator's name, email, and password without displaying the password. Use a password of at least 12 characters.

## Creating an assessment

After signing in, open the assessment workspace at `/assessments/` and choose **Create new assessment**, or go directly to `/assessments/new`.

The form captures metadata for a fictional biometric-authentication system only:

- Organisation and application names (fictional)
- Environment: Development, Test, Staging, or Production-simulation
- Biometric type category (Iris, Fingerprint, Face, Voice, Multi-modal, or Other) — categorisation only, never image upload
- Whether MFA, liveness detection, and administrator access are enabled on the assessed system

The **administrator access** question refers to the fictional system being evaluated, not BioRisk Sentinel's own app-admin role. It supports later urgent-review warnings when audit logging is missing on admin-accessible systems.

All entries must be fictional or synthetic aggregate data. Do not enter biometric samples, templates, banking records, or personal customer data.

On successful creation, the assessment is saved with the signed-in assessor as owner, an audit log entry is written, and you are redirected to the reliability metrics step.

## Reliability metrics

After creating an assessment, open `/assessments/<id>/reliability` to enter aggregate authentication counts:

- Total, successful, and failed attempts
- False acceptances and false rejections
- Genuine and impostor attempts
- Average response time in seconds

Only whole-number counts and aggregate metrics are accepted. The scoring service validates that successful plus failed attempts equals total attempts, genuine plus impostor attempts equals total attempts, and that error counts do not exceed their denominators. On save, the reliability score is calculated automatically and you are redirected to the privacy controls step.

Assessors can access only their own assessments. Administrators can access any assessment. Saving again updates the existing reliability record instead of creating a duplicate row.

### Existing SQLite databases

Fresh installs create the full schema automatically. If you already have a local `instance/biorisk.db` from an earlier version, the app runs a lightweight startup upgrade to add the `admin_accessible` column when needed. You can also delete `instance/biorisk.db` and restart the app to recreate the database.

## Tests

Run all unit and integration tests after activating the local environment:

```powershell
python -m unittest discover -s tests -v
```

The tests exercise the scoring logic, authentication, assessment creation, validation for reliability/privacy/attacks, results generation and printable report rendering. They use an in-memory SQLite database and create/drop the schema in each test's setUp/tearDown.

## Routes overview

- /health — health check (GET)
- / — landing page
- /auth/register — create assessor account (public)
- /auth/login — sign in
- /auth/logout — sign out (POST)
- /assessments/ — assessment workspace (requires sign-in)
- /assessments/new — create new assessment (requires sign-in)
- /assessments/<id>/reliability — enter aggregate reliability metrics
- /assessments/<id>/privacy — enter privacy controls (yes/no)
- /assessments/<id>/attacks — enter authorized simulated attack counts
- /assessments/<id>/results — view computed scores, risk band, and findings
- /assessments/<id>/report — printable HTML report

## Privacy and safe-use notes

- This application is a security assessment tool and must never accept, store, or process biometric images, templates, embeddings, model artifacts, passwords (except app-account passwords, which are hashed), banking records, or personal customer data.
- All assessment inputs must be fictional or synthetic aggregate data.
- The separate research notebook and any trained models are offline research artifacts and must not be imported or hosted by this application.

## Developer notes / next steps

- Local database: instance/biorisk.db (created automatically). For production, switch to a managed Postgres and run proper migrations.
- To create an administrator locally, run:

```powershell
flask --app app create-admin
```

- Do not commit .env, database files, or virtual environments to version control.
- Next suggested improvements: nicer layout templates, CSV export of aggregated results (privacy-safe), or PDF export implemented locally without cloud hosting.

## Scoring rules in this prototype

- Reliability: 45% authentication accuracy, 30% false-acceptance resistance, 20% false-rejection resistance, and 5% response-time quality. A 1% FAR receives a 30-point quality penalty because unauthorized acceptance is especially severe in financial applications.
- Privacy: the points from the project brief, totalling 100.
- Attack resistance: equal-weighted mean of each authorized simulated attack's detection rate.
- Overall: 35% reliability, 30% privacy, and 35% attack resistance.

Raw biometric-data storage and missing template encryption always trigger an urgent review warning, even if the numerical risk band is low.
