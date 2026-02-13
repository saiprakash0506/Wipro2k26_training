# 🎓 Wipro 2026 Training - Test Automation Track

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)](https://selenium.dev)
[![Robot Framework](https://img.shields.io/badge/Robot%20Framework-6.0+-red.svg)](https://robotframework.org)
[![HTML](https://img.shields.io/badge/HTML5-85.8%25-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/HTML)

> **Comprehensive repository documenting my learning journey in Software Test Automation during Wipro's 2026 Training Program**

---

## 📋 Table of Contents

- [About](#-about)
- [Repository Structure](#-repository-structure)
- [Technology Stack](#-technology-stack)
- [Projects & Assignments](#-projects--assignments)
- [Capstone Project](#-capstone-project---foodie-app)
- [Learning Path](#-learning-path)
- [Key Skills Acquired](#-key-skills-acquired)
- [How to Use This Repository](#-how-to-use-this-repository)
- [Installation & Setup](#-installation--setup)
- [Contact](#-contact)

---

## 🚀 About

This repository contains all the **assignments, case studies, projects, and learning materials** from Wipro's comprehensive Test Automation Training Program (2026 Batch). The training focuses on building industry-ready automation testing skills using modern tools and frameworks.

### Training Highlights

- ✅ **Duration**: Multiple months of intensive training
- ✅ **Focus Areas**: Selenium WebDriver, Robot Framework, Python, API Testing
- ✅ **Approach**: Hands-on learning with real-world projects
- ✅ **Outcome**: Industry-ready automation test engineer

---

## 📁 Repository Structure

```
Wipro2k26_training/
│
├── Assignment/                      # Regular training assignments
│   └── Various automation tasks and exercises
│
├── Case_Study_1/                    # Case Study 1 - Web Testing
│   └── Comprehensive web automation scenarios
│
├── Case_Study_2/                    # Case Study 2 - Advanced Concepts
│   └── Complex testing scenarios
│
├── Case_Study_3/                    # Case Study 3 - Integration Testing
│   └── End-to-end automation workflows
│
├── Python_Selenium_Notes/           # Study materials and notes
│   └── Detailed notes on Python & Selenium
│
├── RobotFramework/                  # Robot Framework projects
│   └── Keyword-driven test automation
│
├── Selenium IDE exports labs/       # Selenium IDE test cases
│   └── Recorded and exported test scripts
│
├── Selenium Webdriver Labs/         # WebDriver practical labs
│   └── Hands-on WebDriver exercises
│
├── Selenium ide Project/            # Complete IDE projects
│   └── Full test suites using Selenium IDE
│
├── Sai Prakash/                     # Personal work and experiments
│   └── Custom projects and practice
│
├── jan2026.robot                    # Robot Framework test file
│
└── README.md                        # This file
```

---

## 🛠️ Technology Stack

### Core Technologies

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Programming** | Python 3.8+ | Test script development |
| **Web Automation** | Selenium WebDriver 4.0+ | Browser automation |
| **Test Framework** | Robot Framework 6.0+ | Keyword-driven testing |
| **IDE** | Selenium IDE | Record & playback testing |
| **Markup** | HTML5 | Test reports and documentation |
| **Testing Types** | API, UI, E2E | Comprehensive test coverage |

### Additional Tools & Libraries

- **pytest** - Python testing framework
- **requests** - HTTP library for API testing
- **jsonschema** - JSON validation
- **unittest** - Python's built-in test framework
- **pandas** - Data manipulation (if used)

---

## 📚 Projects & Assignments

### 1. Regular Assignments

**Location**: `/Assignment`

Foundational exercises covering:
- Basic Selenium commands
- Locator strategies (ID, Name, XPath, CSS)
- WebDriver actions (click, type, navigate)
- Assertions and validations
- Wait mechanisms (implicit, explicit, fluent)

### 2. Case Study 1 - Web Application Testing

**Location**: `/Case_Study_1`

**Objective**: Test a complete web application

**Skills Demonstrated**:
- Page Object Model (POM) design pattern
- Data-driven testing
- Test suite organization
- Reporting and logging

### 3. Case Study 2 - Advanced Automation

**Location**: `/Case_Study_2`

**Objective**: Complex testing scenarios

**Skills Demonstrated**:
- Handling dynamic web elements
- File uploads/downloads
- JavaScript execution
- Window/frame handling
- Alert handling

### 4. Case Study 3 - Integration & E2E Testing

**Location**: `/Case_Study_3`

**Objective**: End-to-end workflow testing

**Skills Demonstrated**:
- Multi-page workflows
- Database validation
- API integration testing
- Cross-browser testing
- Performance considerations

### 5. Selenium IDE Projects

**Location**: `/Selenium IDE exports labs` & `/Selenium ide Project`

**Features**:
- Record and playback test cases
- Export to Python/Java
- Quick regression testing
- UI test automation without coding

### 6. Selenium WebDriver Labs

**Location**: `/Selenium Webdriver Labs`

**Hands-on Practice**:
- WebDriver API exploration
- Browser interactions
- Element identification techniques
- Action chains
- Screenshot capture

### 7. Robot Framework Tests

**Location**: `/RobotFramework` & `jan2026.robot`

**Implementation**:
- Keyword-driven test cases
- Data-driven testing
- Test libraries and keywords
- HTML test reports
- Reusable test components

---

## 📖 Reference Project - Foodie App

### Overview

The **Foodie App** is a comprehensive REST API backend application used as a **reference/practice project** for learning Flask development and automation testing. It demonstrates enterprise-grade software development and automation testing practices.

### Project Details

**Type**: Reference/Learning Project  
**Technology**: Flask REST API  
**Architecture**: Layered (Routes → Services → Models)  
**Testing**: Pytest + Robot Framework  
**Documentation**: Complete API documentation

### Features Implemented

#### 1️⃣ Restaurant Module
- ✅ Register Restaurant
- ✅ Update Restaurant Details
- ✅ Disable Restaurant
- ✅ View Restaurant Information

#### 2️⃣ Dish Module
- ✅ Add New Dish
- ✅ Update Dish Details
- ✅ Enable/Disable Dish Availability
- ✅ Delete Dish

#### 3️⃣ Admin Module
- ✅ Approve Restaurant Registrations
- ✅ Disable Restaurant Operations
- ✅ View Customer Feedback
- ✅ View All Orders

#### 4️⃣ User Module
- ✅ User Registration
- ✅ Search Restaurants
- ✅ Place Orders
- ✅ Submit Ratings & Reviews

#### 5️⃣ Order Module
- ✅ View Orders by Restaurant
- ✅ View Orders by User

**Total APIs**: 18 RESTful endpoints

### API Endpoints Summary

```
# Restaurant APIs
POST   /api/v1/restaurants              # Register restaurant
GET    /api/v1/restaurants/{id}         # Get restaurant details
PUT    /api/v1/restaurants/{id}         # Update restaurant
PUT    /api/v1/restaurants/{id}/disable # Disable restaurant

# Dish APIs
POST   /api/v1/restaurants/{id}/dishes  # Add dish
PUT    /api/v1/dishes/{id}              # Update dish
PUT    /api/v1/dishes/{id}/status       # Change availability
DELETE /api/v1/dishes/{id}              # Delete dish

# User APIs
POST   /api/v1/users/register           # Register user
GET    /api/v1/restaurants/search       # Search restaurants
POST   /api/v1/orders                   # Place order
POST   /api/v1/ratings                  # Submit rating

# Admin APIs
PUT    /api/v1/admin/restaurants/{id}/approve   # Approve restaurant
PUT    /api/v1/admin/restaurants/{id}/disable   # Disable restaurant
GET    /api/v1/admin/feedback                   # View all feedback
GET    /api/v1/admin/orders                     # View all orders

# Order APIs
GET    /api/v1/restaurants/{id}/orders  # Orders by restaurant
GET    /api/v1/users/{id}/orders        # Orders by user
```

### Testing Strategy

#### Pytest Automation
- ✅ Unit tests for all API endpoints
- ✅ Integration testing
- ✅ JSON schema validation
- ✅ Fixtures for test data setup
- ✅ Parametrized tests for multiple scenarios
- ✅ Code coverage reports

#### Robot Framework Testing
- ✅ Keyword-driven test cases
- ✅ Data-driven testing
- ✅ BDD-style readable tests
- ✅ HTML test reports
- ✅ RequestsLibrary for API calls

#### Manual Testing
- ✅ Postman collection
- ✅ API documentation
- ✅ Test scenarios documentation

### Architecture

```
┌─────────────────────────────────────┐
│         Routes Layer                │  ← HTTP Request Handling
│  (API Endpoints & Request/Response) │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│        Service Layer                │  ← Business Logic
│   (Validation, Processing, Rules)   │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│         Models Layer                │  ← Data Management
│      (Data Storage & Retrieval)     │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│         Tests Layer                 │  ← Quality Assurance
│   (Pytest & Robot Framework Tests)  │
└─────────────────────────────────────┘
```

### Project Highlights

✅ **REST Principles**: Resource-based URIs, proper HTTP methods  
✅ **Clean Architecture**: Separation of concerns  
✅ **Comprehensive Testing**: 100% API coverage  
✅ **Industry Standards**: Following best practices  
✅ **Documentation**: Complete code documentation  
✅ **Automation**: Full test automation suite  

> **Note**: This is a reference/practice project used for learning REST API development and automation testing concepts. It serves as a comprehensive example of industry best practices.

---

## 🎯 Learning Path

### Phase 1: Python Fundamentals
- Variables, data types, control structures
- Functions, modules, packages
- File handling and exceptions
- Object-oriented programming

### Phase 2: Selenium Basics
- WebDriver setup and configuration
- Browser interactions
- Element locators (8 types)
- Basic automation scripts

### Phase 3: Advanced Selenium
- Page Object Model (POM)
- Data-driven testing
- Frameworks and test organization
- Screenshot and reporting

### Phase 4: Robot Framework
- Keyword-driven testing
- Test libraries
- Data-driven approaches
- Custom keywords creation

### Phase 5: API Testing
- REST API concepts
- Python requests library
- JSON handling
- API test automation

### Phase 6: Integration & Frameworks
- Pytest framework
- Test fixtures and parametrization
- CI/CD integration concepts
- Reporting and analysis

### Phase 7: Reference Project & Practice
- Full-stack API development
- Comprehensive test automation
- Professional documentation
- Real-world application practice

---

## 💡 Key Skills Acquired

### Technical Skills

#### Automation Testing
- ✅ Selenium WebDriver (Python)
- ✅ Robot Framework
- ✅ Pytest framework
- ✅ API testing with requests
- ✅ Test data management
- ✅ Test reporting

#### Programming
- ✅ Python programming
- ✅ Object-oriented concepts
- ✅ Design patterns (POM)
- ✅ Code organization
- ✅ Version control (Git)

#### Web Technologies
- ✅ HTML/CSS/JavaScript basics
- ✅ DOM manipulation
- ✅ Browser DevTools
- ✅ XPath and CSS selectors
- ✅ REST API concepts

#### Testing Concepts
- ✅ Test planning and design
- ✅ Test case development
- ✅ Defect reporting
- ✅ Test automation frameworks
- ✅ CI/CD basics

### Soft Skills

- ✅ Problem-solving
- ✅ Analytical thinking
- ✅ Documentation
- ✅ Time management
- ✅ Continuous learning

---

## 🔧 How to Use This Repository

### For Learning

1. **Start with basics**: Review `/Python_Selenium_Notes`
2. **Practice assignments**: Work through `/Assignment` folder
3. **Study case studies**: Analyze `/Case_Study_1`, `/Case_Study_2`, `/Case_Study_3`
4. **Explore frameworks**: Check `/RobotFramework` examples
5. **Review reference project**: Study the Foodie App implementation as a learning example

### For Reference

- **Selenium examples**: See `/Selenium Webdriver Labs`
- **IDE scripts**: Check `/Selenium IDE exports labs`
- **Robot tests**: Browse `/RobotFramework`
- **API testing**: Review Foodie App test suites

### For Recruiters

This repository demonstrates:
- **Technical proficiency** in automation testing
- **Hands-on experience** with industry tools
- **Project completion** capability
- **Clean code** practices
- **Documentation** skills
- **Learning agility**

---

## 📦 Installation & Setup

### Prerequisites

```bash
# Python 3.8 or higher
python --version

# pip package manager
pip --version
```

### Install Dependencies

```bash
# Clone the repository
git clone https://github.com/saiprakash0506/Wipro2k26_training.git
cd Wipro2k26_training

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install selenium
pip install robotframework
pip install robotframework-seleniumlibrary
pip install pytest
pip install requests
pip install jsonschema
pip install flask  # For Foodie App
```

### WebDriver Setup

```bash
# Install WebDriver Manager (automatically handles driver downloads)
pip install webdriver-manager

# Or manually download drivers:
# Chrome: https://chromedriver.chromium.org/
# Firefox: https://github.com/mozilla/geckodriver/releases
# Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
```

### Running Tests

```bash
# Run Selenium tests
python your_test_file.py

# Run Robot Framework tests
robot test_suite.robot

# Run Pytest tests
pytest -v

# Run with coverage
pytest --cov=. --cov-report=html
```

---

## 📊 Progress Tracking

| Module | Status | Completion |
|--------|--------|------------|
| Python Fundamentals | ✅ Complete | 100% |
| Selenium Basics | ✅ Complete | 100% |
| Selenium Advanced | ✅ Complete | 100% |
| Robot Framework | ✅ Complete | 100% |
| API Testing | ✅ Complete | 100% |
| Case Study 1 | ✅ Complete | 100% |
| Case Study 2 | ✅ Complete | 100% |
| Case Study 3 | ✅ Complete | 100% |
| Reference Project (Foodie App) | ✅ Complete | 100% |

---

## 🎓 Certifications & Achievements

- ✅ Completed Wipro 2026 Test Automation Training
- ✅ Practiced with full-stack REST API application (Foodie App)
- ✅ Implemented comprehensive test automation
- ✅ Mastered Selenium WebDriver
- ✅ Proficient in Robot Framework
- ✅ API testing expertise

---

## 📝 Best Practices Followed

### Code Quality
- ✅ Clean, readable code
- ✅ Proper naming conventions
- ✅ Code comments where needed
- ✅ DRY (Don't Repeat Yourself) principle
- ✅ Modular design

### Testing
- ✅ Comprehensive test coverage
- ✅ Independent test cases
- ✅ Proper assertions
- ✅ Test data separation
- ✅ Clear test reports

### Documentation
- ✅ README files
- ✅ Code comments
- ✅ API documentation
- ✅ Test case descriptions
- ✅ Setup instructions

---

## 🤝 Contributing

This is a personal learning repository. However, if you find any issues or have suggestions:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📞 Contact

**Name**: Sai Prakash  
**Training**: Wipro 2026 Batch  
**GitHub**: [@saiprakash0506](https://github.com/saiprakash0506)  
**Repository**: [Wipro2k26_training](https://github.com/saiprakash0506/Wipro2k26_training)

---

## 📄 License

This project is created for educational and training purposes as part of Wipro's 2026 Training Program.

---

## 🙏 Acknowledgments

- **Wipro Training Team** - For comprehensive training program
- **Trainers & Mentors** - For guidance and support
- **Selenium Community** - For excellent documentation
- **Robot Framework Community** - For helpful resources
- **Python Community** - For amazing libraries and tools

---

## 📚 Additional Resources

### Learning Materials
- [Selenium Official Documentation](https://www.selenium.dev/documentation/)
- [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Pytest Documentation](https://docs.pytest.org/)
- [REST API Best Practices](https://restfulapi.net/)

### Tools & Utilities
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)
- [Postman](https://www.postman.com/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- [VS Code](https://code.visualstudio.com/)

---

## 🎯 Future Enhancements

- [ ] Add CI/CD pipeline integration
- [ ] Implement parallel test execution
- [ ] Add performance testing
- [ ] Database integration for test data
- [ ] Cloud testing (BrowserStack/Sauce Labs)
- [ ] Visual regression testing
- [ ] Mobile automation with Appium
- [ ] Security testing basics

---

## 📈 Repository Statistics

![GitHub Stars](https://img.shields.io/github/stars/saiprakash0506/Wipro2k26_training?style=social)
![GitHub Forks](https://img.shields.io/github/forks/saiprakash0506/Wipro2k26_training?style=social)
![GitHub Watchers](https://img.shields.io/github/watchers/saiprakash0506/Wipro2k26_training?style=social)

**Languages Distribution**:
- HTML: 85.8%
- Python: 12.2%
- RobotFramework: 2.0%

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

**Made with ❤️ during Wipro 2026 Training**

</div>
