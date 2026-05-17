# 🚀 PHP Manager Enterprise

**Professional PHP Version Manager for XAMPP with Automatic DLL Conflict Resolution**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)](https://www.microsoft.com/windows)
[![XAMPP](https://img.shields.io/badge/XAMPP-7.x%2B-green.svg)](https://www.apachefriends.org/)

[English](#english) | [العربية](#arabic)

---

## 📊 Statistics & Status

![GitHub stars](https://img.shields.io/github/stars/yourusername/php-manager-enterprise?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/php-manager-enterprise?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/yourusername/php-manager-enterprise?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/yourusername/php-manager-enterprise)
![GitHub issues](https://img.shields.io/github/issues/yourusername/php-manager-enterprise)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/php-manager-enterprise)

---

<a name="english"></a>
## 📖 English Documentation

### 🎯 Overview

**PHP Manager Enterprise** is a professional-grade desktop application that revolutionizes PHP version management in XAMPP environments. Built with Python and Tkinter, it provides a seamless solution for developers and system administrators to install, switch, and manage multiple PHP versions while automatically resolving DLL conflicts and ensuring Apache compatibility.

**The Problem:** Manually updating PHP in XAMPP often leads to frustrating DLL mismatches, Apache configuration errors, and hours of troubleshooting.

**The Solution:** PHP Manager Enterprise automates the entire process - from downloading compatible versions to fixing conflicts and updating configurations - saving you countless hours of manual work.

### ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔄 **Smart Version Management** | Install, switch, and maintain multiple PHP versions with zero configuration hassle |
| 🔧 **Automatic DLL Resolution** | Intelligently detects and resolves conflicts between PHP and Apache DLLs (libssl, libcrypto, libssh2, etc.) |
| 🏗️ **Seamless Apache Integration** | Automatically updates Apache configurations (httpd.conf, httpd-xampp.conf) for perfect compatibility |
| 💾 **Intelligent Backup System** | Creates timestamped backups before any critical operation with one-click restoration |
| 🎯 **Architecture Detection** | Automatically detects Apache architecture (32-bit/64-bit) and recommends compatible PHP versions |
| 📊 **Real-time Progress Tracking** | Visual progress bar with detailed status updates for all operations |
| 🌐 **Bilingual Interface** | Full support for English and Arabic with instant language switching |
| 🛡️ **Safe Rollback Mechanism** | Instant recovery from any backup point with automatic conflict resolution |
| 📝 **Comprehensive Logging** | Detailed operation logs with timestamp and color-coded severity levels |
| ⚡ **Multi-threaded Operations** | Non-blocking UI during downloads and installations |

### 🖼️ User Interface

<div align="center">
  <img width="946" height="855" alt="PHP Manager Enterprise Interface" src="https://github.com/user-attachments/assets/54a035a9-f8e4-42c4-9f2c-877e79c0261e" />
  <br />
  <em>Main Application Interface - Clean, Professional, and Intuitive</em>
</div>

### 📋 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Operating System** | Windows 7 | Windows 10/11 (64-bit) |
| **XAMPP Version** | 7.x | 8.x or higher |
| **Python Version** | 3.7 | 3.11+ |
| **Internet Connection** | Required (for downloads) | Broadband connection |
| **RAM** | 512 MB | 2 GB |
| **Disk Space** | 500 MB | 2 GB |
| **Administrator Rights** | Not required | Recommended for best experience |

### 🔧 Quick Installation

#### Step 1: Install Python Dependencies

Open Command Prompt or PowerShell and run:

```bash
pip install requests beautifulsoup4
