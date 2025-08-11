## 🔧 Selenium Test Automation for "The Planet Website ##

### 🌐 Project Overview

This project contains automated test scripts written in Python using Selenium WebDriver, the Page Object Model (POM) design pattern for the demo healthcare appointment website.

🔗 [The Planet Website](https://www.automatetheplanet.com/)

The Planet Website is a trusted platform in the test automation industry, offering consulting services, demos, and free resources for automation professionals. The site includes interactive UI elements, dynamic forms, and navigation flows that make it ideal for automation testing practice.

---

## ✅ What This Project Covers

I created **modular, reusable test scripts for each page and section of the website**. Each script covers:

-  Functional testing of form elements, buttons, and inputs  
-  UI element validations and navigations  
-  Dynamic content and user interactions  
-  Positive and negative test flows  
-  Page redirection and link testing  
-  Full coverage of responsive elements and edit features  

Test cases follow **Page Object Model (POM)** architecture for clean structure, reusability, and easy maintenance.

---

## 📄 Pages and Features Tested

Scripts were created **page-by-page** and fully test the following:

-  **Home Page**  
-  **Create meeting page**  
-  **Contact Us Form**  
-  **Sign-Up Page**  
-  **Demo Page**  
-  **Web Automation Page**  
-  **Career Page**  
-  **Resources Section and Articles**  
-  **Read Full Article / Read Full Story Buttons**  
-  **Footer Elements and External Links**

Every feature is automated individually using dedicated test scripts and page classes.

---

## 🧾 Test Case Documentation

All **manual test cases** are well-documented and organized in the file below:

📄 [`Test_cases.md`](./Test_cases.md)

This file includes:

- Field-level validations  
- Button and form behaviors  
- Error handling scenarios  
- Positive and negative test cases  
- Navigation and redirection test cases  
- Responsive UI validations

---

## 🧰 Tools & Technologies Used

    Language: Python 3.x

    Automation Tool: Selenium WebDriver

    Design Pattern: Page Object Model (POM)

    Browser Drivers: ChromeDriver and GeckoDriver (Firefox)
---

## 📁 Project Structure
<pre>

Automate-The-Planet-Automation/
│
├── tests/                            # ✅ Test scripts 
│   ├── home_test.py
│   ├── contact_us_test.py
│   ├── create_meeting_test.py
│   ├── signup_test.py
│   ├── demo_test.py
│   ├── web_automation_test.py
│   ├── private_training_test.py
│   ├── career_test.py
│   ├── resources_test.py
│   └── footer_test.py
│  
│
├── pages/                            # 📄 Page Object classes 
│   ├── home_page.py
│   ├── contact_us_page.py
│   ├── create_meeting_page.py
│   ├── signup_page.py
│   ├── demo_page.py
│   ├── web_automation_page.py
│   ├── private_training_page.py
│   ├── career_page.py
│   ├── resources_page.py
│   └── footer_page.py
│
│
├── Test_cases.md                     #  Manual test case documentation
├── requirements.txt                  #  Python dependencies
├── conftest.py                       # Pytest fixtures (e.g., browser setup)
├── README.md                         #  Project overview and instructions
└── .gitignore                        #  Files to exclude from Git

</pre>

## 🚀 How to Run the Tests

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ecommerce-ui-testing.git
   cd ecommerce-ui-testing






