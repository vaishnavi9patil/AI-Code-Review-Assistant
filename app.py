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