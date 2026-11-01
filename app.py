
import streamlit as st
import string

st.set_page_config(
    page_title="SecureCheck | Password Intelligence",
    page_icon="🔐",
    layout="wide"
)

# ---------------- PAGE DESIGN ----------------

st.markdown("""
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
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.title("SECURECHECK")
st.caption("PASSWORD INTELLIGENCE & SECURITY ANALYSIS")
st.divider()

# ---------------- SIDEBAR ----------------

st.sidebar.title("SECURECHECK")
st.sidebar.caption("Cybersecurity Project 01")

st.sidebar.markdown("---")
st.sidebar.markdown("### Security Information")
st.sidebar.info(
    "This educational tool evaluates basic password "
    "characteristics and provides improvement suggestions."
)

st.sidebar.markdown("### Assessment Criteria")
st.sidebar.write("• Password length")
st.sidebar.write("• Uppercase and lowercase")
st.sidebar.write("• Numeric characters")
st.sidebar.write("• Special symbols")
st.sidebar.write("• Common password detection")

# ---------------- PASSWORD INPUT ----------------

st.subheader("Password Assessment")

password = st.text_input(
    "Enter a test password",
    type="password",
    placeholder="Type a test password..."
)

# ---------------- ANALYSIS ----------------

COMMON_PASSWORDS = {
    "password",
    "12345678",
    "qwerty123",
    "admin123",
    "welcome123",
    "password123"
}

if st.button("RUN SECURITY ANALYSIS", use_container_width=True):

    if not password:
        st.warning("Please enter a password.")

    else:

        checks = {
            "Minimum 12 characters": len(password) >= 12,
            "Uppercase letter": any(c.isupper() for c in password),
            "Lowercase letter": any(c.islower() for c in password),
            "Number": any(c.isdigit() for c in password),
            "Special symbol": any(c in string.punctuation for c in password)
        }

        score = sum(checks.values()) * 20
        is_common = password.lower() in COMMON_PASSWORDS

        if is_common:
            strength = "WEAK"
            color = "🔴"
        elif score <= 40:
            strength = "WEAK"
            color = "⚠️"
        elif score <= 80:
            strength = "MEDIUM"
            color = "🟡"
        else:
            strength = "STRONG"
            color = "🟢"

        if is_common:
            score = min(score, 20)

        st.divider()
        st.header("Security Intelligence Report")

        col1, col2, col3 = st.columns(3)

        col1.metric("Security Score", f"{score}/100")
        col2.metric("Password Strength", strength)
        col3.metric(
            "Common Password",
            "Detected" if is_common else "Not Detected"
        )

        # ---------------- STRENGTH METER ----------------

        st.subheader("Security Strength Meter")
        st.progress(score / 100)

        # ---------------- CHECKLIST ----------------

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

        # ---------------- RECOMMENDATIONS ----------------

        st.subheader("Security Recommendations")

        if is_common:
            st.error("This password matches our small common-password list.")

        recommendations = [
            name for name, passed in checks.items()
            if not passed
        ]

        if recommendations:
            for recommendation in recommendations:
                st.write(f"• Improve: {recommendation}")
        else:
            st.success("All five basic security checks passed!")

        st.caption(
            "Educational assessment only. A high score does not "
            "guarantee resistance to password attacks."
        )

# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    "<center>SECURECHECK | CYBERSECURITY PROJECT 01</center>",
    unsafe_allow_html=True
)
