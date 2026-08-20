# FAR CODE
# False Acceptance Rate
# Bad person gets accepted

def calculate_far(false_acceptances, impostor_attempts):
    if impostor_attempts == 0:
        return 0

    return (false_acceptances / impostor_attempts) * 100


# FRR CODE
# False Rejection Rate
# Good person gets rejected

def calculate_frr(false_rejections, genuine_attempts):
    if genuine_attempts == 0:
        return 0

    return (false_rejections / genuine_attempts) * 100


# ACCURACY
# Percentage of correct decisions

def calculate_accuracy(correct_decisions, total_attempts):
    if total_attempts == 0:
        return 0

    return (correct_decisions / total_attempts) * 100


# RELIABILITY SCORE

def calculate_reliability_score(far, frr, response_time):
    score = 100

    # FAR deduction
    if far < 0.1:
        score -= 0
    elif far <= 0.5:
        score -= 10
    elif far <= 1:
        score -= 25
    else:
        score -= 40

    # FRR deduction
    if frr < 2:
        score -= 0
    elif frr <= 5:
        score -= 10
    else:
        score -= 25

    # Response time deduction
    if response_time > 3:
        score -= 10

    return max(0, score)


# USER INPUT

print("=== Biometric Reliability Assessment ===")

false_acceptances = int(input("Enter false acceptances: "))
impostor_attempts = int(input("Enter impostor attempts: "))

false_rejections = int(input("Enter false rejections: "))
genuine_attempts = int(input("Enter genuine attempts: "))

correct_decisions = int(input("Enter correct decisions: "))
total_attempts = int(input("Enter total attempts: "))

response_time = float(input("Enter average response time (seconds): "))


# CALCULATIONS

far = calculate_far(false_acceptances, impostor_attempts)

frr = calculate_frr(false_rejections, genuine_attempts)

accuracy = calculate_accuracy(
    correct_decisions,
    total_attempts
)

reliability = calculate_reliability_score(
    far,
    frr,
    response_time
)


# RESULTS

print("\n=== RESULTS ===")

print("FAR:", round(far, 2), "%")
print("FRR:", round(frr, 2), "%")
print("Accuracy:", round(accuracy, 2), "%")
print("Reliability Score:", reliability, "/ 100")

#PRIVACY SCORE (appropriate privacy controls)
# PRIVACY SCORE

def calculate_privacy_score(
    template_encryption,
    tls_https,
    no_raw_data,
    access_control,
    audit_logs,
    retention_policy,
    deletion_process,
    consent_process,
    key_management,
    security_review
):
    score = 0

    if template_encryption:
        score += 15

    if tls_https:
        score += 10

    if no_raw_data:
        score += 15

    if access_control:
        score += 10

    if audit_logs:
        score += 10

    if retention_policy:
        score += 10

    if deletion_process:
        score += 10

    if consent_process:
        score += 10

    if key_management:
        score += 5

    if security_review:
        score += 5

    return score

# PRIVACY INPUT

print("\n=== Privacy Assessment ===")

template_encryption = input("Template encryption (yes/no): ").lower() == "yes"

tls_https = input("TLS/HTTPS enabled (yes/no): ").lower() == "yes"

no_raw_data = input("No raw biometric data stored (yes/no): ").lower() == "yes"

access_control = input("Access control implemented (yes/no): ").lower() == "yes"

audit_logs = input("Audit logs available (yes/no): ").lower() == "yes"

retention_policy = input("Retention policy exists (yes/no): ").lower() == "yes"

deletion_process = input("Deletion process exists (yes/no): ").lower() == "yes"

consent_process = input("Consent process exists (yes/no): ").lower() == "yes"

key_management = input("Secure key management (yes/no): ").lower() == "yes"

security_review = input("Security review performed (yes/no): ").lower() == "yes"

privacy_score = calculate_privacy_score(
    template_encryption,
    tls_https,
    no_raw_data,
    access_control,
    audit_logs,
    retention_policy,
    deletion_process,
    consent_process,
    key_management,
    security_review
)
print("Privacy Score:", privacy_score, "/ 100")

#Attack resistance(how well company system detect or block attacks)
# ATTACK RESISTANCE SCORE

def calculate_attack_resistance_score(
    replay_attempts,
    replay_detected,
    spoof_attempts,
    spoof_detected,
    brute_force_attempts,
    brute_force_blocked,
    bypass_attempts,
    bypass_blocked,
    template_attempts,
    template_detected
):
    def detection_rate(detected, attempts):
        if attempts == 0:
            return 0
        return (detected / attempts) * 100

    replay_rate = detection_rate(replay_detected, replay_attempts)

    spoof_rate = detection_rate(spoof_detected, spoof_attempts)

    brute_force_rate = detection_rate(
        brute_force_blocked,
        brute_force_attempts
    )

    bypass_rate = detection_rate(
        bypass_blocked,
        bypass_attempts
    )

    template_rate = detection_rate(
        template_detected,
        template_attempts
    )

    score = (
        replay_rate * 0.20
        + spoof_rate * 0.30
        + brute_force_rate * 0.15
        + bypass_rate * 0.20
        + template_rate * 0.15
    )

    return score
# ATTACK INPUT

print("\n=== Attack Resistance Assessment ===")

replay_attempts = int(input("Replay attack attempts: "))
replay_detected = int(input("Replay attacks detected/blocked: "))

spoof_attempts = int(input("Spoofing attempts: "))
spoof_detected = int(input("Spoofing attacks detected/blocked: "))

brute_force_attempts = int(input("Brute-force attempts: "))
brute_force_blocked = int(input("Brute-force attacks blocked: "))

bypass_attempts = int(input("Bypass attempts: "))
bypass_blocked = int(input("Bypass attempts blocked: "))

template_attempts = int(input("Template attack attempts: "))
template_detected = int(input("Template attacks detected/blocked: "))
attack_score = calculate_attack_resistance_score(
    replay_attempts,
    replay_detected,
    spoof_attempts,
    spoof_detected,
    brute_force_attempts,
    brute_force_blocked,
    bypass_attempts,
    bypass_blocked,
    template_attempts,
    template_detected
)
print("Attack Resistance Score:", round(attack_score, 2), "/ 100")

#Overall Score ( Combines Reliability , Privacy , Attack Resistance)
# OVERALL SCORE

def calculate_overall_score(
    reliability_score,
    privacy_score,
    attack_resistance_score
):
    overall_score = (
        reliability_score * 0.40
        + privacy_score * 0.30
        + attack_resistance_score * 0.30
    )

    return overall_score
overall_score = calculate_overall_score(
    reliability,
    privacy_score,
    attack_score
)
print("Overall Score:", round(overall_score, 2), "/ 100")

#Risk level ( convert overall score into understandable category)
# RISK LEVEL

def calculate_risk_level(overall_score):
    if overall_score >= 80:
        return "Low Risk"
    elif overall_score >= 60:
        return "Medium Risk"
    else:
        return "High Risk"

overall_score = calculate_overall_score(
reliability,
privacy_score,
attack_score
)
risk_level = calculate_risk_level(overall_score)
print("Risk Level:", risk_level)

# FINDINGS

def generate_findings(
    far,
    frr,
    accuracy,
    response_time,
    privacy_score,
    attack_score
):
    findings = []

    # FAR
    if far > 1:
        findings.append("FAR is high.")
    elif far >= 0.5:
        findings.append("FAR requires attention.")

    # FRR
    if frr > 5:
        findings.append("FRR is high.")
    elif frr >= 2:
        findings.append("FRR requires attention.")

    # Accuracy
    if accuracy < 90:
        findings.append("Accuracy is low.")
    elif accuracy < 95:
        findings.append("Accuracy could be improved.")

    # Response time
    if response_time > 3:
        findings.append("Response time is high.")

    # Privacy
    if privacy_score < 60:
        findings.append("Privacy controls need significant improvement.")
    elif privacy_score < 80:
        findings.append("Privacy controls need improvement.")

    # Attack resistance
    if attack_score < 60:
        findings.append("Attack resistance is low.")
    elif attack_score < 80:
        findings.append("Attack resistance could be improved.")

    return findings

# RECOMMENDATIONS

def generate_recommendations(
    far,
    frr,
    accuracy,
    response_time,
    privacy_score,
    attack_score
):
    recommendations = []

    # FAR
    if far > 1:
        recommendations.append(
            "Improve biometric matching and anti-spoofing controls."
        )
    elif far >= 0.5:
        recommendations.append(
            "Review biometric matching thresholds and anti-spoofing controls."
        )

    # FRR
    if frr > 5:
        recommendations.append(
            "Improve biometric matching to reduce false rejections."
        )
    elif frr >= 2:
        recommendations.append(
            "Review matching thresholds to reduce false rejections."
        )

    # Accuracy
    if accuracy < 90:
        recommendations.append(
            "Improve the biometric recognition process and system configuration."
        )
    elif accuracy < 95:
        recommendations.append(
            "Consider improving biometric matching accuracy."
        )

    # Response time
    if response_time > 3:
        recommendations.append(
            "Optimize the biometric authentication process to reduce response time."
        )

    # Privacy
    if privacy_score < 60:
        recommendations.append(
            "Strengthen encryption, access control, retention, deletion, and consent controls."
        )
    elif privacy_score < 80:
        recommendations.append(
            "Improve the implementation of privacy controls."
        )

    # Attack resistance
    if attack_score < 60:
        recommendations.append(
            "Strengthen replay, spoofing, brute-force, bypass, and template attack defenses."
        )
    elif attack_score < 80:
        recommendations.append(
            "Improve attack detection and prevention mechanisms."
        )

    return recommendations
risk_level = calculate_risk_level(overall_score)

findings = generate_findings(
    far,
    frr,
    accuracy,
    response_time,
    privacy_score,
    attack_score
)

recommendations = generate_recommendations(
    far,
    frr,
    accuracy,
    response_time,
    privacy_score,
    attack_score
)
print("\n=== FINDINGS ===")

if len(findings) == 0:
    print("No major weaknesses detected.")
else:
    for finding in findings:
        print("-", finding)


print("\n=== RECOMMENDATIONS ===")

if len(recommendations) == 0:
    print("No major recommendations at this time.")
else:
    for recommendation in recommendations:
        print("-", recommendation)