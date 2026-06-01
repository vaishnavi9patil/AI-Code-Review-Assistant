# AI-Code-Review-Assistant
AI-Powered Code Review Assistant built with Python and Streamlit for automated code quality analysis.


## Project Overview

This project analyzes Python source code and identifies:

- Hardcoded passwords
- User input validation issues
- Debug print statements

The application also calculates a code quality score and categorizes findings by severity.

## Tech Stack

- Python
- Streamlit

## Progress

### Version 1 - File Upload Feature
- Python file upload functionality
- Rule-based code review engine
- Detection of:
  - Hardcoded passwords
  - User input usage
  - Print statements
- Code review results display

### Version 2 - Rule-Based Code Analysis
- Added Code Quality Score system
- Implemented Progress Bar visualization
- Added Code Quality Status (Excellent / Moderate / Poor)
- Created Dashboard Summary with issue counters
- Added High, Medium, and Low severity metrics
- Implemented Issue Distribution Bar Chart
- Improved Streamlit UI for better visualization
- Enhanced project structure for future AI-based reviews

### Version 3 - Code Quality Score

- Smart code review recommendations
- Severity-based issue classification
- Dashboard analytics
- Code quality scoring
- Visual issue distribution charts

## Version 4 Features

- Downloadable Code Review Report
- Automatic report generation
- Report includes:
  - Code Quality Score
  - Detected Issues
  - Severity Levels
- Export review results as TXT file

### Version 5 - Line Number Detection

Enhancements:
- Added line-by-line code scanning.
- Detects the exact location of issues.
- Displays line numbers for security and code quality findings.
- Improves debugging and review experience.

Example:
High: Hardcoded password detected (Line 1)
Medium: User input should be validated (Line 3)
Low: Print statements found (Line 5)

## Version 6 - Advanced Static Analysis

### New Features Added
- Line number detection for issues
- TODO comment detection
- Wildcard import detection (`import *`)
- Empty exception handling detection (`except:`)
- Dynamic recommendations based on issue type
- Score floor protection (cannot go below 0)
- Improved code review report generation

### Result
The assistant now performs deeper static code analysis and provides more accurate issue reporting with exact line references.

## Version 7 - Advanced Dashboard Analytics

### New Features Added

- Total Issues Counter
- Highest Severity Indicator
- Analysis Summary Section
- Enhanced Dashboard Layout
- Professional Security Analysis Summary

### Metrics Displayed

- High Severity Issues
- Medium Severity Issues
- Low Severity Issues
- Total Issues Found
- Highest Severity Level

### Outcome

The AI Code Review Assistant now provides a professional dashboard with detailed security insights, issue categorization, severity analysis, and actionable recommendations.

## Version 8 - Pie Chart Visualization

### New Features Added

- Pie Chart for Issue Distribution
- Visual Severity Breakdown
- Percentage-based Issue Analysis

### Dashboard Improvements

- Bar Chart Visualization
- Pie Chart Visualization
- Severity Metrics
- Analysis Summary

### Outcome

Users can now visualize issue severity distribution through both bar charts and pie charts, making the dashboard more interactive and professional.

## Version 9 - Code Statistics Dashboard

### New Features Added

- Total Lines of Code
- Function Count
- Import Count
- Comment Count
- Class Count
- Comment Percentage

### Benefits

- Provides quick insights into code structure
- Improves maintainability analysis
- Gives users a better understanding of code composition

### Outcome

The AI Code Review Assistant now performs both issue detection and code statistics analysis, making it closer to a professional static code analysis tool.

### Version 10 – Multiple File Upload Support
Objective

Enhanced the AI Code Review Assistant to support uploading and reviewing multiple Python files simultaneously.

Features Added
- Multiple .py file upload capability.
- Individual code preview for each uploaded file.
- Separate analysis for every uploaded file.
- Improved scalability for reviewing larger projects containing multiple source files.


### Version 11 – AI Review Summary Engine
Objective

Introduced an AI-style review engine that generates an overall assessment of uploaded code based on detected issues.

Features Added
- AI-generated review summary
- Severity-based recommendations
- Automated deployment readiness assessment
- Security-focused feedback

Benefits
- Makes the application feel AI-driven
- Provides actionable feedback
- Improves user understanding of code quality
- Simulates professional code review reports

