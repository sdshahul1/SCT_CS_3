import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("⚠️ 12+ characters makes it stronger")

    # Check uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")

    # Check lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters (a-z)")

    # Check numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add numbers (0-9)")

    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$%)")

    # Result
    print("\n===== Password Strength Result =====")
    if score <= 2:
        print("Strength: 🔴 WEAK")
    elif score <= 4:
        print("Strength: 🟡 MODERATE")
    else:
        print("Strength: 🟢 STRONG")

    print(f"Score: {score}/6")

    if feedback:
        print("\nSuggestions:")
        for tip in feedback:
            print(tip)
    else:
        print("✅ Excellent password!")

def main():
    print("===== Password Strength Checker =====")
    password = input("Enter your password: ")
    check_password_strength(password)

main()