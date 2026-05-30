import streamlit as st

st.title("🤖 AI Code Review Assistant")

uploaded_file = st.file_uploader(
    "Upload a Python file",
    type=["py"]
)

if uploaded_file:

    code = uploaded_file.read().decode("utf-8")

    st.subheader("Uploaded Code")
    st.code(code, language="python")

    issues = []
    score = 100

    if "password =" in code:
        issues.append(("High", "Hardcoded password detected"))
        score -= 30

    if "input(" in code:
        issues.append(("Medium", "User input should be validated"))
        score -= 20

    if "print(" in code:
        issues.append(("Low", "Print statements found"))
        score -= 10


    st.subheader("📊 Code Quality Score")
    st.metric("Score", f"{score}/100")
    st.progress(score / 100)

    if score >= 80:
        st.success("Excellent Code Quality")
    elif score >= 60:
        st.warning("Moderate Code Quality")
    else:
        st.error("Poor Code Quality")

    # Dashboard Metrics
    high_count = sum(1 for s, i in issues if s == "High")
    medium_count = sum(1 for s, i in issues if s == "Medium")
    low_count = sum(1 for s, i in issues if s == "Low")

    st.subheader("📊 Dashboard Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🔴 High Issues", high_count)

    with col2:
        st.metric("🟡 Medium Issues", medium_count)

    with col3:
        st.metric("🟢 Low Issues", low_count)

    st.subheader("🔍 Code Review")

    if len(issues) == 0:
        st.success("No obvious issues detected.")
    else:
        for severity, issue in issues:

            if severity == "High":
                st.error(f"{severity}: {issue}")

            elif severity == "Medium":
                st.warning(f"{severity}: {issue}")

            else:
                st.info(f"{severity}: {issue}")