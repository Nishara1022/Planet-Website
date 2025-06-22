<pre>
## 🔧 Selenium Test Automation for "Automate The Planet Website ##

# 🌐 Project Overview

This repository contains **automated UI and functional test scripts** developed using **Python, Selenium WebDriver**, and the **Page Object Model (POM)** for:

🔗 [Automate The Planet](https://www.automatetheplanet.com/)

> Automate The Planet is a trusted platform in the test automation industry, offering consulting services, demos, and free resources for automation professionals. The site includes interactive UI elements, dynamic forms, and navigation flows that make it ideal for automation testing practice.

---

## ✅ What This Project Covers

I created **modular, reusable test scripts for each page and section of the website**. Each script covers:

- ✅ Functional testing of form elements, buttons, and inputs  
- ✅ UI element validations and navigations  
- ✅ Dynamic content and user interactions  
- ✅ Positive and negative test flows  
- ✅ Page redirection and link testing  
- ✅ Full coverage of responsive elements and edit features  

Test cases follow **Page Object Model (POM)** architecture for clean structure, reusability, and easy maintenance.

---

## 📄 Pages and Features Tested

Scripts were created **page-by-page** and fully test the following:

- 🏠 **Home Page**  
- 📅 **Book a Meeting Page**  
- 🔁 **Meeting Section – Edit Date/Time**  
- 📩 **Contact Us Form**  
- 📝 **Sign-Up Page**  
- 🧪 **Demo Booking Page**  
- 🌍 **Web Automation Services Page**  
- 🎯 **Career Page**  
- 📚 **Resources Section and Articles**  
- 📖 **Read Full Article / Read Full Story Buttons**  
- 📥 **Footer Elements and External Links**

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

## 🧰 Tech Stack Used

| Tool/Library         | Description                             |
|----------------------|-----------------------------------------|
| 🐍 Python 3.x         | Main programming language               |
| 🧪 Selenium WebDriver | For browser automation                  |
| 🧱 POM Pattern        | For structured page-level automation    |
| 🧪 Pytest             | For test execution                      |
| 🌐 ChromeDriver       | For Chrome browser testing              |
| 🧩 GitHub             | Version control and project hosting     |

---

## 📁 Project Structure

Automate-The-Planet-Automation/
│
├── tests/
│ ├── test_home_page.py
│ ├── test_book_meeting.py
│ ├── test_meeting_section.py
│ ├── test_contact_us.py
│ ├── test_signup.py
│ ├── test_demo_page.py
│ ├── test_web_automation.py
│ ├── test_career_page.py
│ └── test_resources_page.py
│
├── pages/
│ ├── home_page.py
│ ├── book_meeting_page.py
│ ├── meeting_section_page.py
│ ├── contact_us_page.py
│ ├── signup_page.py
│ ├── demo_page.py
│ ├── web_automation_page.py
│ ├── career_page.py
│ └── resources_page.py
│
│
├── Test_cases.md # ✔️ Manual test scenarios
├── requirements.txt # Python dependencies
├── README.md # 📄 Project documentation
└── .gitignore # System and virtual env files

</pre>