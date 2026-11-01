import sys
import string
from getpass import getpass


# ============================================================
# SECURECHECK - PASSWORD STRENGTH CHECKER
# Run in terminal:  python password_strength_checker.py --terminal
# Run web app:      python -m streamlit run password_strength_checker.py
# ============================================================

COMMON_PASSWORDS = {
    "password",
    "12345678",
    "qwerty123",
    "admin123",
    "welcome123",
    "password123",
}


def analyze_password(password):
    """Apply the same basic password checks to both interfaces."""
    checks = {
        "Minimum 12 characters": len(password) >= 12,
        "Uppercase letter": any(char.isupper() for char in password),
        "Lowercase letter": any(char.islower() for char in password),
        "Number": any(char.isdigit() for char in password),
        "Special symbol": any(char in string.punctuation for char in password),
    }

    is_common = password.lower() in COMMON_PASSWORDS
    score = sum(checks.values()) * 20

    if is_common:
        strength = "WEAK"
        score = min(score, 20)
    elif score <= 40:
        strength = "WEAK"
    elif score <= 80:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    recommendations = [
        name for name, passed in checks.items() if not passed
    ]

    return {
        "checks": checks,
        "score": score,
        "strength": strength,
        "is_common": is_common,
        "recommendations": recommendations,
    }


def run_terminal():
    """Run the password checker in the command-line terminal."""
    print("=" * 52)
    print("                 SECURECHECK")
    print("          PASSWORD STRENGTH CHECKER")
    print("=" * 52)
    print("Educational tool: enter a TEST password, not a real one.")
    print()

    password = getpass("Enter a test password: ")

    if not password:
        print("\nNo password entered. Please run the program again.")
        return

    result = analyze_password(password)

    print("\nPASSWORD ANALYSIS")
    print("-" * 52)
    print(f"Security score : {result['score']}/100")
    print(f"Strength       : {result['strength']}")
    print(
        "Common password: "
        + ("Detected" if result["is_common"] else "Not detected")
    )

    print("\nSECURITY CRITERIA")
    for name, passed in result["checks"].items():
        status = "PASS" if passed else "NEEDS IMPROVEMENT"
        print(f"- {name}: {status}")

    print("\nRECOMMENDATIONS")
    if result["is_common"]:
        print("- This password matches the tool's small common-password list.")
    if result["recommendations"]:
        for recommendation in result["recommendations"]:
            print(f"- Improve: {recommendation}")
    elif not result["is_common"]:
        print("- All five basic security checks passed.")

    print("\nNote: This is a basic educational assessment, not a guarantee")
    print("that a password is safe from guessing or other attacks.")
    print("=" * 52)


def run_streamlit():
    """Run the SecureCheck browser dashboard."""
    import streamlit as st

    st.set_page_config(
        page_title="SecureCheck | Password Intelligence",
        page_icon="🔐",
        layout="wide",
    )

    st.markdown(
        """
        <style>
        .stApp {
            background: #0B1220;
            color: #F4F0E6;
        }
        h1, h2, h3 {
            color: #D6B56D !important;
        }
        p, label, span {
            color: #E6EAF0;
        }
        div[data-testid="stMetric"] {
            background: #17263D;
            padding: 20px;
            border-radius: 12px;
            border: 1px solid #34465F;
        }
        div.stButton > button {
            background: #D6B56D;
            color: #101A2B;
            border-radius: 8px;
            font-weight: bold;
            border: none;
        }
        div.stButton > button:hover {
            background: #E8CA86;
            color: #101A2B;
        }
        section[data-testid="stSidebar"] {
            background: #111D30;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("SECURECHECK")
    st.caption("PASSWORD INTELLIGENCE & SECURITY ANALYSIS")
    st.divider()

    st.sidebar.title("SECURECHECK")
    st.sidebar.caption("Cybersecurity Project 01")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Security Information")
    st.sidebar.info(
        "This educational tool evaluates basic password characteristics "
        "and provides improvement suggestions."
    )
    st.sidebar.markdown("### Assessment Criteria")
    st.sidebar.write("• Password length")
    st.sidebar.write("• Uppercase and lowercase")
    st.sidebar.write("• Numeric characters")
    st.sidebar.write("• Special symbols")
    st.sidebar.write("• Common password detection")

    st.subheader("Password Assessment")
    password = st.text_input(
        "Enter a test password",
        type="password",
        placeholder="Type a test password...",
        help="Use a sample password. Do not enter a real personal password.",
    )

    if st.button("RUN SECURITY ANALYSIS", use_container_width=True):
        if not password:
            st.warning("Please enter a test password.")
        else:
            result = analyze_password(password)
            checks = result["checks"]

            st.divider()
            st.header("Security Intelligence Report")

            col1, col2, col3 = st.columns(3)
            col1.metric("Security Score", f"{result['score']}/100")
            col2.metric("Password Strength", result["strength"])
            col3.metric(
                "Common Password",
                "Detected" if result["is_common"] else "Not Detected",
            )

            st.subheader("Security Strength Meter")
            st.progress(result["score"] / 100)

            st.subheader("Security Criteria")
            left, right = st.columns(2)
            items = list(checks.items())

            with left:
                for name, passed in items[:3]:
                    if passed:
                        st.success(f"✓ {name}")
                    else:
                        st.warning(f"✗ {name}")

            with right:
                for name, passed in items[3:]:
                    if passed:
                        st.success(f"✓ {name}")
                    else:
                        st.warning(f"✗ {name}")

            st.subheader("Security Recommendations")
            if result["is_common"]:
                st.warning(
                    "This password matches the tool's small "
                    "common-password list."
                )

            if result["recommendations"]:
                for recommendation in result["recommendations"]:
                    st.write(f"• Improve: {recommendation}")
            elif not result["is_common"]:
                st.success("All five basic security checks passed!")

            st.caption(
                "Educational assessment only. A high score does not "
                "guarantee resistance to password attacks. The common "
                "password list is small and is not a breached-password database."
            )

    st.divider()
    st.markdown(
        "<center>SECURECHECK | CYBERSECURITY PROJECT 01</center>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    if "--terminal" in sys.argv:
        run_terminal()
    else:
        run_streamlit()
