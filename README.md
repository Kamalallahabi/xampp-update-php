# 🚀 XAMPP Pro Manager (XPM)
### The Ultimate Desktop Utility for Managing PHP Versions & XAMPP Configuration

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Windows%2010/11-blue)](https://www.microsoft.com/windows)
[![Python](https://img.shields.io/badge/Built%20with-Python%203.x-3776AB?logo=python)](https://www.python.org/)
[![Release](https://img.shields.io/badge/Version-1.0.0-green)](https://github.com/KamalAllahabi/XAMPP-Pro-Manager/releases)

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/c1d8a80b-58d0-4b75-8127-307569a1e5b8" alt="Main Dashboard Interface" width="800"/>
</p>

## 📖 Overview

**XAMPP Pro Manager (XPM)** is a powerful, standalone desktop application designed to eliminate the headaches of managing local development environments. Built with Python and Tkinter, it provides a modern Graphical User Interface (GUI) to handle complex tasks like switching PHP versions, resolving DLL conflicts, editing `php.ini`, and securing MySQL—without touching a single line of code or command prompt.

Whether you are a beginner struggling with configuration files or a senior developer needing quick environment switches, XPM automates the entire workflow.

### 💡 Why Use XPM?
*   **No More Manual Edits:** Stop opening `php.ini` in Notepad++. Change settings via intuitive toggles.
*   **One-Click Version Switching:** Install and switch between PHP 7.x and 8.x instantly.
*   **Auto-Fix Compatibility:** Automatically resolves common Apache/PHP DLL errors (`libssl`, `libcrypto`).
*   **Bilingual Support:** Fully supports **English** and **Arabic** (RTL) interfaces.

---

## ✨ Key Features

### 🔄 PHP Version Management
*   **Smart Installer:** Fetches compatible PHP versions directly from windows.php.net based on your Apache architecture (x86/x64).
*   **Safe Switching:** Creates automatic backups before switching versions, allowing instant rollback if needed.
*   **Apache Integration:** Automatically updates `httpd.conf` and `httpd-xampp.conf` to ensure Apache recognizes the new PHP version.

### ⚙️ Advanced Configuration Tool
*   **Extension Manager:** Enable/Disable extensions (curl, gd, mysqli, openssl, etc.) with simple checkboxes.
*   **Resource Limits:** Adjust `upload_max_filesize`, `post_max_size`, and `memory_limit` visually.
*   **Dev/Prod Mode:** 
    *   🛠️ **Dev Mode:** Enables error reporting, disables OpCache.
    *   🚀 **Prod Mode:** Hides errors, enables OpCache for performance.

### 🛡️ Security & Maintenance
*   **MySQL Security:** Set or change the MySQL `root` password directly from the app.
*   **DLL Conflict Resolver:** One-click fix for missing or mismatched DLL files in the Apache bin folder.
*   **PhpMyAdmin Fixer:** Automatically configures `mysqli` extensions and generates secure blowfish secrets.

### 🌍 User Experience
*   **Real-time Logging:** Color-coded logs track every action for easy debugging.
*   **Non-Blocking UI:** Downloads and installations run in background threads, keeping the interface responsive.
*   **Portable:** No installation required for the `.exe` version. Just run and manage.

---

## 📸 Screenshots

| Main Dashboard | Configuration Tool |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/c1d8a80b-58d0-4b75-8127-307569a1e5b8" width="400"/> | <img src="https://github.com/user-attachments/assets/a250d2e5-fa78-406e-8306-8a26a3088d1d" width="400"/> |

---

## 📋 System Requirements

| Component | Requirement |
|-----------|-------------|
| **OS** | Windows 10 / 11 (64-bit recommended) |
| **XAMPP** | Any standard XAMPP installation (C:/xampp or custom path) |
| **Permissions** | **Administrator Rights Required** 🔑 |
| **Internet** | Required for downloading PHP versions |

> ⚠️ **Important Note:** The application modifies system files within the XAMPP directory. You **MUST** run `XPM.exe` as **Administrator** (Right-click -> Run as Administrator) to avoid permission errors.

---

## 🚀 Installation & Usage

### Option 1: Using the Executable (Recommended)

1.  Download the latest `XPM.exe` from the [Releases Page](https://github.com/KamalAllahabi/XAMPP-Pro-Manager/releases).
2.  Place the file in a convenient location.
3.  **Right-click** on `XPM.exe` and select **"Run as Administrator"**.
4.  Select your XAMPP installation folder when prompted.
5.  Start managing your server!

### Option 2: Running from Source Code (For Developers)

If you want to modify the code or run it without compiling:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/KamalAllahabi/XAMPP-Pro-Manager.git
    cd XAMPP-Pro-Manager
    ```

2.  **Install Dependencies:**
    Ensure you have Python 3.7+ installed, then run:
    ```bash
    pip install requests beautifulsoup4
    ```

3.  **Run the Application:**
    ```bash
    python update.py
    ```
    *(Note: On Windows, right-click your terminal/command prompt and "Run as Administrator" before executing the python command to ensure full permissions.)*

---

## 📂 Project Structure

```text
XAMPP-Pro-Manager/
├── XPM.exe             # Compiled executable (Ready to use)
├── update.py           # Source code (Python script)
└── README.md           # Documentation
