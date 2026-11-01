# Password-strength-cheacker# 🔐 SecureCheck — Password Strength Checker

## Project Overview

SecureCheck is a Python-based cybersecurity project designed to evaluate password strength through basic security checks.

The application analyzes password characteristics and classifies passwords as Weak, Medium, or Strong.

## Project Objectives

- Evaluate password length.
- Identify uppercase and lowercase letters.
- Detect numeric characters.
- Identify special symbols.
- Detect selected commonly used passwords.
- Provide password improvement recommendations.

## Features

### 1. Python Terminal Application
- Password strength assessment.
- Security condition checking.
- Password score calculation.
- Common password detection.
- Security recommendations.
- Hidden password input.

### 2. Streamlit Web Application
- Professional interactive interface.
- Password strength assessment.
- Security score out of 100.
- Visual strength meter.
- Security checklist.
- Improvement recommendations.

## Technologies Used

- Python
- Streamlit
- String module
- Getpass module

## Project Structure

```text
Password_Strength_Checker/
│
├── Terminal_Version/
│   └── password_checker.py
│
├── Streamlit_Version/
│   └── app.py
│
├── Screenshots/
│
├── README.md
│
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Terminal Application

```bash
python Terminal_Version/password_checker.py
```

## Run the Streamlit Application

```bash
python -m streamlit run Streamlit_Version/app.py
```

## Learning Outcomes

Through this project, I practiced:

- Python programming fundamentals.
- String handling.
- Conditional statements.
- Password validation.
- Basic cybersecurity concepts.
- Building interactive applications using Streamlit.

## Security Disclaimer

This project is an educational demonstration of basic password-strength checks. Its small common-password list is not a comprehensive breached-password database. It does not guarantee password security and should not be used as a production password auditing service.

## Project Information

**Project:** Cyber Security Project 01  
**Title:** Password Strength Checker  
**Training Organization:** DecodeLabs  
**Batch:** 2026
