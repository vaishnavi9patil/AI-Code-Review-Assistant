from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def generate_pdf(score, issues, ai_summary, file_count):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI CODE REVIEW REPORT",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Score: {score}/100",
            styles["Heading2"]
        )
    )
    content.append(
        Paragraph(
            f"Files Analyzed: {file_count}",
            styles["BodyText"]
        )
    )
    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Detected Issues",
            styles["Heading2"]
        )
    )

    for severity, issue in issues:
        content.append(
            Paragraph(
                f"{severity}: {issue}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "AI Review Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            ai_summary,
            styles["BodyText"]
        )
    )

    doc.build(content)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf

st.set_page_config(page_title="AI Code Review Assistant", layout="wide")

st.title("🤖 AI Code Review Assistant")

uploaded_files = st.file_uploader(
    "Upload a Python files",
    type=["py"],
    accept_multiple_files=True
)

if uploaded_files:

    issues = []
    score = 100

    all_code = ""

    total_lines = 0
    function_count = 0
    import_count = 0
    comment_count = 0
    class_count = 0
    long_function_count = 0
    nested_loop_count = 0
    large_file_count = 0

    for uploaded_file in uploaded_files:
        code = uploaded_file.read().decode("utf-8")
        lines = code.split("\n")

        st.subheader(f"📄 {uploaded_file.name}")

        st.code(code, language="python")

    
    
  
    # Code Statistics

    total_lines += len(lines)
    if len(lines) > 100:
        large_file_count += 1

    function_count += sum(
        1 for line in lines
        if line.strip().startswith("def ")
    )

    import_count += sum(
        1 for line in lines
        if line.strip().startswith("import ")
        or line.strip().startswith("from ")
    )

    comment_count += sum(
        1 for line in lines
        if line.strip().startswith("#")
    )
    class_count += sum(
    1 for line in lines
    if line.strip().startswith("class ")
    )

    blank_lines = sum(
        1 for line in lines
        if line.strip() == ""
    )

    if total_lines > 0:
        comment_ratio = round(
            (comment_count / total_lines) * 100,
            1
        )
    else:
        comment_ratio = 0



    for line_number, line in enumerate(lines, start=1):
        for i in range(len(lines) - 1):
            if (
                lines[i].strip().startswith("for ")
                and lines[i + 1].startswith("    for ")
            ):
                nested_loop_count += 1

        # Hardcoded password
        if "password =" in line:
            issues.append(
                (
                    "High",
                    f"{uploaded_file.name}: Hardcoded password detected (Line {line_number})"
                )
            )
            score -= 30

        # User input
        if "input(" in line:
            issues.append(
                (
                    "Medium",
                    f"User input should be validated (Line {line_number})"
                )
            )
            score -= 20

        # Print statements
        if "print(" in line:
            issues.append(
                (
                    "Low",
                    f"Print statements found (Line {line_number})"
                )
            )
            score -= 10

        # TODO comments
        if "TODO" in line:
            issues.append(
                (
                    "Low",
                    f"TODO comment found (Line {line_number})"
                )
            )
            score -= 5

        # Wildcard imports
        if "import *" in line:
            issues.append(
                (
                    "Medium",
                    f"Wildcard import detected (Line {line_number})"
                )
            )
            score -= 15

        # Empty exception handling
        if "except:" in line:
            issues.append(
                (
                    "High",
                    f"Empty exception handling detected (Line {line_number})"
                )
            )
            score -= 25

    # Prevent negative score
    score = max(score, 0)

    # Generate report
    report = f"""
AI CODE REVIEW REPORT

Score: {score}/100
Files Analyzed: {len(uploaded_files)}

Issues Found:
-------------------------
"""

    if len(issues) == 0:
        report += "No issues detected.\n"
    else:
        for severity, issue in issues:
            report += f"{severity} - {issue}\n"

    # Download Report Button
    st.download_button(
        label="📥 Download Review Report",
        data=report,
        file_name="code_review_report.txt",
        mime="text/plain"
    )
    


    # Score Section
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

    total_issues = len(issues)

    highest_severity = "None"

    if high_count > 0:
        highest_severity = "High"

    elif medium_count > 0:
        highest_severity = "Medium"

    elif low_count > 0:
        highest_severity = "Low"

    complexity_score = "Low"

    if long_function_count >= 2 or nested_loop_count >= 2:
        complexity_score = "High"

    elif long_function_count >= 1 or nested_loop_count >= 1:
        complexity_score = "Medium"

    # Chart
    st.subheader("📈 Issue Distribution")

    chart_data = pd.DataFrame(
        {
            "Issues": [high_count, medium_count, low_count]
        },
        index=["High", "Medium", "Low"]
    )

    st.bar_chart(chart_data)

    st.subheader("🥧 Issue Distribution Pie Chart")

    labels = ["High", "Medium", "Low"]
    sizes = [high_count, medium_count, low_count]

# Remove categories with 0 issues
    filtered_labels = []
    filtered_sizes = []

    for label, size in zip(labels, sizes):
        if size > 0:
            filtered_labels.append(label)
            filtered_sizes.append(size)

    fig, ax = plt.subplots()

    ax.pie(
        filtered_sizes,
        labels=filtered_labels,
        autopct="%1.1f%%"
        )

    ax.axis("equal")

    st.pyplot(fig)

    
    st.subheader("📊 Code Statistics")

    s1, s2, s3, s4, s5, s6 = st.columns(6)

    with s1:
        st.metric("📄 Lines", total_lines)

    with s2:
        st.metric("🔧 Functions", function_count)

    with s3:
        st.metric("📦 Imports", import_count)

    with s4:
        st.metric("💬 Comments", comment_count)

    with s5:
        st.metric("🏛 Classes", class_count)

    with s6:
        st.metric("📏 Comment %", f"{comment_ratio}%")
    
    current_function_lines = 0

    inside_function = False

    for line in lines:

        if line.strip().startswith("def "):
            inside_function = True
            current_function_lines = 1

        elif inside_function:

            if line.startswith("    "):
                current_function_lines += 1

        else:

            if current_function_lines > 20:
                long_function_count += 1

            inside_function = False
    

    st.subheader("🧠 Complexity Analysis")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("📈 Complexity", complexity_score)

    with c2:
        st.metric("🔧 Long Functions", long_function_count)

    with c3:
        st.metric("🔄 Nested Loops", nested_loop_count)

    with c4:
        st.metric("📄 Large Files", large_file_count)


    # Summary
    st.subheader("📊 Dashboard Summary")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("🔴 High", high_count)

    with col2:
        st.metric("🟡 Medium", medium_count)

    with col3:
        st.metric("🟢 Low", low_count)

    with col4:
        st.metric("📌 Total", total_issues)

    with col5:
        st.metric("⚠ Highest", highest_severity)


    st.subheader("📋 Analysis Summary")

    summary_text = f"""
    📌 Total Issues Found: {total_issues}

    ⚠ Highest Severity: {highest_severity}

    📊 Code Score: {score}/100

    Security, quality and maintainability issues were detected.
    Review all findings before production deployment.
    """

    st.info(summary_text)


    st.subheader("🤖 AI Review Summary")

    if high_count >= 2:
        ai_summary = """
    This code contains serious security concerns.

    Critical issues such as hardcoded credentials and improper exception handling were detected.

    The code should not be deployed until these issues are resolved.
    """
    elif high_count >= 1:
        ai_summary = """
    This code contains important security and maintainability issues.

    Several improvements are recommended before production deployment.
    """
    elif medium_count >= 2:
        ai_summary = """
    This code has moderate quality concerns.

    Input validation, imports, and code structure should be improved.
    """
    else:
        ai_summary = """
    The code quality appears acceptable.

    Only minor improvements are recommended.
    """

    st.info(ai_summary)

    # PDF Generation
    pdf_file = generate_pdf(
        score,
        issues,
        ai_summary,
        len(uploaded_files)
    )

    # PDF Download Button
    st.download_button(
        label="📄 Download PDF Report",
        data=pdf_file,
        file_name="AI_Code_Review_Report.pdf",
        mime="application/pdf"
    )

    # Code Review
    st.subheader("🔍 Code Review")

    if len(issues) == 0:
        st.success("No obvious issues detected.")
    else:
        for severity, issue in issues:

            if severity == "High":

                st.error(f"{severity}: {issue}")

                if "password" in issue.lower():
                    st.write(
                        "💡 Recommendation: Store passwords in environment variables instead of source code."
                    )

                elif "exception" in issue.lower():
                    st.write(
                        "💡 Recommendation: Handle exceptions explicitly and log errors."
                    )

            elif severity == "Medium":

                st.warning(f"{severity}: {issue}")

                if "input" in issue.lower():
                    st.write(
                        "💡 Recommendation: Validate and sanitize user input before processing."
                    )

                elif "import" in issue.lower():
                    st.write(
                        "💡 Recommendation: Avoid wildcard imports. Import only required modules."
                    )

            else:

                st.info(f"{severity}: {issue}")

                if "todo" in issue.lower():
                    st.write(
                        "💡 Recommendation: Complete or remove TODO comments before production release."
                    )

                elif "print" in issue.lower():
                    st.write(
                        "💡 Recommendation: Use logging instead of print statements in production."
                    )