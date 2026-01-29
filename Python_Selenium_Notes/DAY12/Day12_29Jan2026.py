#! ROBOT FRAMEWORK
'''
1. Introduction to Robot Framework
Robot Framework is an open-source test automation framework mainly used for:
Acceptance testing
Regression testing
RPA (Robotic Process Automation)
Key Features
Keyword-driven testing
Easy-to-read, tabular syntax
Supports Selenium, API, Database, Appium, etc.
Platform and language independent (written in Python)
File Types

#! .robot → test cases
#! .resource → reusable keywords
#! .py → custom libraries

2. Environment Setup & Required Packages
Step 1: Install Python
Check installation:

#~ python --version

Step 2: Install Robot Framework

#~ pip install robotframework

Verify:

#~ robot --version

Step 3: Install Selenium Library

#~ pip install robotframework-seleniumlibrary

Step 4: Install WebDriver

Use ChromeDriver / EdgeDriver
(or use WebDriverManager manually if preferred)

3. Robot Framework – RIDE Tool
What is RIDE?
RIDE (Robot IDE) is a GUI tool to:
Write test cases
Manage keywords
Execute tests

Install RIDE

#~ pip install robotframework-ride

Launch RIDE:

#~ ride.py

'''


