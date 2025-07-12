# WHATSAPP-AUTOMATION

Empower Seamless, Personalized Messaging at Scale

![last commit](https://img.shields.io/badge/last%20commit-today-brightgreen)
![html](https://img.shields.io/badge/html-80%25-orange)
![languages](https://img.shields.io/badge/languages-2-blue)

> Built using:

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

---

## 📚 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Getting Started](#getting-started)

  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
* [CSV Format](#csv-format)
* [License](#license)

---

## 📖 Overview

**whatsapp-automation** is a Python-Flask-based automation tool that helps you send bulk, personalized WhatsApp messages through WhatsApp Web.
It's designed for events, campaigns, and bulk notifications, e.g., for Guru Purnima greetings to teachers.

It includes a frontend form for customizing messages and uploading recipient lists, and a backend that handles scheduling, validation, and dispatch via the `pywhatkit` library.

---

## ✨ Features

* 📊 **Live Status Panel**: Track progress and errors in real time.
* 📂 **CSV Upload**: Import recipients from `.csv` files to avoid manual typing.
* 🕒 **Message Delay Control**: Add delay between messages to manage sending speed.
* 💬 **Template Support**: Use `{name}` and `{title}` placeholders in messages.
* ❌ **Stop Sending Option**: Instantly cancel the process.
* 📱 **Phone Validation**: Validates number format before sending.

---

## ⚙️ Getting Started

### 🧩 Prerequisites

* Python 3.8+
* Google Chrome (logged into WhatsApp Web)
* Git

### 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/whatsapp-automation.git
cd whatsapp-automation

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

### ▶️ Usage

```bash
python main.py
```

1. Open your browser at `http://localhost:5000`
2. Paste your message template using `{name}` and `{title}`.
3. Add recipients manually or upload a CSV.
4. Click **Send All Messages**.
5. Monitor sending status and errors in real time.

---

## 🧾 CSV Format

Use this format for your `.csv` file:

```csv
name,title,phone
John,Sir,+91XXXXXXXXXX
Anita,Ma'am,+91XXXXXXXXXX
```

* Phone must start with `+` and be in international format.

---

## 🪪 License

This project is licensed under the **MIT License**.

---

Created with ❤️ by Pratham
