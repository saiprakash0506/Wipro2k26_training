'''1️⃣ What is Selenium Grid?

Selenium Grid is a tool that allows you to run Selenium tests:

• On multiple machines
• On multiple browsers
• On multiple operating systems
• In parallel

👉 Main goal: Speed + Cross-Browser Testing

2️⃣ Why Selenium Grid is Needed?
❌ Without Grid

If you have 100 test cases:

Chrome → Run (30 mins)

Firefox → Run (30 mins)

Edge → Run (30 mins)

Total = 90 minutes 😩

✅ With Grid (Parallel Execution)

All 3 browsers run at same time.

Total = 30 minutes ⚡

3️⃣ Core Concepts of Selenium Grid
🔹 Hub

• Central controller
• Receives test requests
• Assigns tests to available nodes

🔹 Node

• Machine that actually runs the browser
• Can have Chrome, Firefox, Edge installed
• Registers itself to the Hub

4️⃣ Selenium Grid 4 Architecture (Latest)
4

Selenium Grid 4 introduced internal components:

• Router – Receives test request
• Distributor – Decides which node gets test
• Session Map – Tracks active sessions
• Event Bus – Communication system
• Node – Executes test

But don’t worry — this is handled internally.

5️⃣ Grid 3 vs Grid 4
Grid 3	Grid 4
Separate hub & node mandatory	Standalone mode available
JSON Wire Protocol	W3C Protocol
Limited UI	Modern UI Dashboard
Less scalable	More scalable
6️⃣ Grid Modes in Selenium 4
🔹 1. Standalone Mode (Easy)

Hub + Node in single command.

Best for beginners.

🔹 2. Hub & Node Mode

Run hub and nodes separately.

🔹 3. Distributed Mode

Enterprise-level scaling.

7️⃣ Installation – Step by Step
Step 1: Install Java (JDK 11+)

Check:

java -version

Step 2: Download Selenium Server

From selenium.dev

You’ll get:

selenium-server-4.x.x.jar

Step 3: Start Grid (Standalone)
java -jar selenium-server-4.x.x.jar standalone


Now open:

http://localhost:4444/ui


You’ll see Grid dashboard.

8️⃣ How Python Connects to Grid

Instead of:

webdriver.Chrome()


We use:

webdriver.Remote()


Because browser runs remotely.

9️⃣ Basic Python Example
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.browser_version = "latest"
options.platform_name = "Windows"

driver = webdriver.Remote(
    command_executor="http://localhost:4444",
    options=options
)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()

🔟 Desired Capabilities / Options

You define:

• browserName
• browserVersion
• platformName
• headless mode
• logging preferences

Example:

options.add_argument("--headless")

1️⃣1️⃣ Running Tests in Parallel

Using pytest:

pip install pytest pytest-xdist
pytest -n 4


This runs 4 tests simultaneously.

1️⃣2️⃣ Real Company Usage

Selenium Grid is used in:

• CI/CD pipelines
• Jenkins
• GitHub Actions
• Cloud environments
• Cross-browser testing

1️⃣3️⃣ Selenium Grid with Docker (Modern Approach)

Instead of manual setup, companies use Docker.

Example:

docker run -d -p 4444:4444 selenium/standalone-chrome


Now Grid runs inside container.

Benefits:

• Easy scaling
• No dependency issues
• Works in cloud
• DevOps friendly

1️⃣4️⃣ Scaling Selenium Grid
Horizontal Scaling

Add more nodes.

Cloud Scaling

Use:
• BrowserStack
• Sauce Labs
• LambdaTest

They provide ready-made Grid.

1️⃣5️⃣ Common Errors & Fixes
❌ SessionNotCreatedException

Browser version mismatch.

❌ Connection Refused

Grid not started.

❌ TimeoutException

Node overloaded.

1️⃣6️⃣ Advantages of Selenium Grid

✅ Faster execution
✅ Parallel testing
✅ Cross-browser testing
✅ Cross-platform testing
✅ CI/CD friendly

1️⃣7️⃣ Disadvantages

❌ Complex setup
❌ Requires infrastructure
❌ Debugging slightly harder

1️⃣8️⃣ Interview Questions

Q: What is Selenium Grid?
Q: What is RemoteWebDriver?
Q: Difference between Grid 3 and 4?
Q: How does parallel execution work?
Q: What is Distributor in Grid 4?

1️⃣9️⃣ Real Framework Structure Example
project/
│
├── tests/
├── pages/
├── conftest.py
├── requirements.txt
└── pytest.ini


Grid URL usually configured inside conftest.py.

2️⃣0️⃣ When Should You Use Grid?

Use Grid when:

• Test cases > 50
• Need cross-browser testing
• Running in CI/CD
• Enterprise-level automation

🎯 Final Summary (Remember This)

Selenium Grid =

👉 Remote execution
👉 Parallel execution
👉 Cross-browser testing
👉 Scalable automation

If Selenium is the engine,
Selenium Grid is the highway system.'''