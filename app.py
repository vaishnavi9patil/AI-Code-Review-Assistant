import streamlit as st
import pandas as pd

st.title("🤖 AI Code Review Assistant")

uploaded_file = st.file_uploader(
    "Upload a Python file",
    type=["py"]
)

if uploaded_file:

    # Read uploaded code
    code = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Uploaded Code")
    st.code(code, language="python")

    # Initialize variables
    issues = []
    score = 100

    # Detect issues
    lines = code.split("\n")

    for line_number, line in enumerate(lines, start=1):
        if "password =" in line:
            issues.append(
                (
                    "High",
                    f"Hardcoded password detected (Line {line_number})"
                )
            )
            score -= 30

        if "input(" in line:
            issues.append(
                (
                    "Medium",
                    f"User input should be validated (Line {line_number})"
                )
            )
            score -= 20

        if "print(" in line:
            issues.append(
                (
                    "Low",
                    f"Print statements found (Line {line_number})"
                )
            )
            score -= 10

    # Generate report
    report = f"""
AI CODE REVIEW REPORT

Score: {score}/100

Issues Found:
-------------------------
"""

    if len(issues) == 0:
        report += "No issues detected.\n"
    else:
        for severity, issue in issues:
            report += f"{severity} - {issue}\n"

    # Download button
    st.download_button(
        label="📥 Download Review Report",
        data=report,
        file_name="code_review_report.txt",
        mime="text/plain"
    )

    # Code Quality Score
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

    # Chart
    st.subheader("📈 Issue Distribution")

    chart_data = pd.DataFrame(
        {
            "Issues": [high_count, medium_count, low_count]
        },
        index=["High", "Medium", "Low"]
    )

    st.bar_chart(chart_data)

    # Dashboard Summary
    st.subheader("📊 Dashboard Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🔴 High Issues", high_count)

    with col2:
        st.metric("🟡 Medium Issues", medium_count)

    with col3:
        st.metric("🟢 Low Issues", low_count)

    # Code Review
    st.subheader("🔍 Code Review")

    if len(issues) == 0:
        st.success("No obvious issues detected.")

    else:

        for severity, issue in issues:

            if severity == "High":

                st.error(f"{severity}: {issue}")

                st.write(
                    "💡 Recommendation: Store passwords in environment variables instead of source code."
                )

            elif severity == "Medium":

                st.warning(f"{severity}: {issue}")

                st.write(
                    "💡 Recommendation: Validate and sanitize user input before processing."
                )

            else:

                st.info(f"{severity}: {issue}")

                st.write(
                    "💡 Recommendation: Use logging instead of print statements in production."
                )