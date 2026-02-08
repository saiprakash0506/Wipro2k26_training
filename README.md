# Wipro 2026 Training Repository 🚀

[![GitHub Stars](https://img.shields.io/github/stars/saiprakash0506/Wipro2k26_training?style=social)](https://github.com/saiprakash0506/Wipro2k26_training/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/saiprakash0506/Wipro2k26_training?style=social)](https://github.com/saiprakash0506/Wipro2k26_training/network/members)
[![Languages](https://img.shields.io/github/languages/count/saiprakash0506/Wipro2k26_training)](https://github.com/saiprakash0506/Wipro2k26_training)

This repository contains comprehensive learning materials, assignments, case studies, and practical implementations from the Wipro 2026 Training Program focused on Software Testing and Test Automation.

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Technologies Covered](#technologies-covered)
- [Getting Started](#getting-started)
- [Project Contents](#project-contents)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Learning Path](#learning-path)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🎯 Overview

This repository serves as a comprehensive collection of test automation learning resources, practical exercises, and real-world case studies completed during the Wipro 2026 Training Program. It covers fundamental to advanced concepts in software testing, with a strong emphasis on automation using industry-standard tools and frameworks.

## 📁 Repository Structure

```
Wipro2k26_training/
│
├── Assignment/                          # Training assignments and solutions
│
├── Case_Study_1/                        # First case study implementation
│
├── Case_Study_2/                        # Second case study implementation
│
├── Case_Study_3/                        # Third case study implementation
│
├── Python_Selenium_Notes/               # Python & Selenium reference notes
│
├── RobotFramework/                      # Robot Framework implementations
│
├── Sai Prakash/                         # Personal projects and exercises
│
├── Selenium IDE exports labs/           # Selenium IDE lab exercises
│
├── Selenium Webdriver Labs/             # Selenium WebDriver practical labs
│
├── Selenium ide Project/                # Complete Selenium IDE projects
│
└── jan2026.robot                        # Robot Framework test file
```

## 💻 Technologies Covered

### Testing Frameworks
- **Selenium WebDriver** - Web application automation
- **Selenium IDE** - Record and playback testing
- **Robot Framework** - Keyword-driven test automation

### Programming Languages
- **Python** - Primary scripting language for automation
- **HTML** - Web technologies and page object implementations

### Tools & Methodologies
- Test case design and execution
- Page Object Model (POM)
- Data-driven testing
- Keyword-driven testing
- Cross-browser testing
- Test reporting and analysis

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

```bash
# Python 3.x
python --version

# pip (Python package manager)
pip --version

# Git
git --version
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/saiprakash0506/Wipro2k26_training.git
   cd Wipro2k26_training
   ```

2. **Install Selenium**
   ```bash
   pip install selenium
   ```

3. **Install Robot Framework**
   ```bash
   pip install robotframework
   pip install robotframework-seleniumlibrary
   ```

4. **Download WebDrivers**
   - [ChromeDriver](https://chromedriver.chromium.org/downloads)
   - [GeckoDriver (Firefox)](https://github.com/mozilla/geckodriver/releases)
   - [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

5. **Add WebDrivers to PATH** or place them in your project directory

## 📚 Project Contents

### Assignments
Contains various testing assignments covering:
- Basic Selenium operations
- Locator strategies
- Handling web elements
- Test assertions and validations
- Framework implementation

### Case Studies
Real-world testing scenarios including:
- **Case Study 1**: E-commerce application testing
- **Case Study 2**: Form validation and data handling
- **Case Study 3**: End-to-end workflow automation

### Selenium Labs
Hands-on practical exercises covering:
- Element identification and interaction
- Wait mechanisms (Implicit, Explicit, Fluent)
- Handling alerts, frames, and windows
- File uploads and downloads
- Screenshot capture
- Advanced user interactions

### Robot Framework
Implementation of test automation using Robot Framework:
- Test suites and test cases
- Custom keywords
- Resource files
- Test libraries integration
- Reporting and logging

## 🎓 Learning Path

1. **Fundamentals** (Week 1-2)
   - Understanding Selenium architecture
   - Basic Python programming
   - Web element identification

2. **Intermediate** (Week 3-4)
   - Advanced locators
   - Wait strategies
   - Page Object Model
   - Data-driven testing

3. **Advanced** (Week 5-6)
   - Framework design
   - Robot Framework
   - CI/CD integration
   - Test reporting

## 📖 Usage

### Running Selenium Tests

```bash
# Navigate to Selenium Webdriver Labs
cd "Selenium Webdriver Labs"

# Run a Python test file
python test_login.py
```

### Running Robot Framework Tests

```bash
# Run a Robot Framework test
robot jan2026.robot

# Run with specific browser
robot -v BROWSER:Chrome jan2026.robot

# Generate detailed reports
robot --outputdir results jan2026.robot
```

### Using Selenium IDE

1. Install Selenium IDE browser extension
2. Open Selenium IDE projects from `Selenium ide Project/`
3. Execute recorded test cases
4. Export tests to Python/Java/C# as needed

## 🏆 Key Features

- ✅ Comprehensive test automation examples
- ✅ Industry-standard framework implementations
- ✅ Well-documented code with comments
- ✅ Real-world case study implementations
- ✅ Reusable test libraries and utilities
- ✅ Best practices and design patterns

## 🔧 Best Practices Implemented

- **Page Object Model (POM)**: Separation of test logic and page elements
- **Modular Design**: Reusable test components
- **Data-Driven Testing**: External test data management
- **Exception Handling**: Robust error management
- **Logging**: Comprehensive test execution logs
- **Reporting**: Detailed test reports with screenshots

## 📈 Skills Developed

Through this training program, the following skills were developed:

- Test automation strategy and planning
- Python programming for test automation
- Web application testing using Selenium
- Framework design and implementation
- Robot Framework test development
- Cross-browser testing techniques
- Continuous Integration/Continuous Deployment (CI/CD) concepts
- Test reporting and metrics analysis

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/saiprakash0506/Wipro2k26_training/issues).

To contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Notes

- All test data used is for educational purposes only
- WebDriver executables are not included; download separately
- Some tests may require internet connection
- Update WebDriver versions as needed for browser compatibility

## 🐛 Troubleshooting

### Common Issues

**Issue**: WebDriver not found
```bash
# Solution: Add WebDriver to PATH or specify path in code
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
```

**Issue**: Element not found
```bash
# Solution: Add proper wait conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))
```

## 📚 Additional Resources

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Python Official Documentation](https://docs.python.org/3/)
- [Wipro Training Materials](https://www.wipro.com/)

## 📄 License

This project is licensed for educational purposes as part of the Wipro 2026 Training Program.

## 👤 Contact

**Sai Prakash**

- GitHub: [@saiprakash0506](https://github.com/saiprakash0506)
- Repository: [Wipro2k26_training](https://github.com/saiprakash0506/Wipro2k26_training)

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Made with ❤️ during Wipro 2026 Training Program**

</div>
