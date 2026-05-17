# 🚀 XAMPP Pro Manager (PHP Manager Enterprise)

**The Ultimate All-in-One Control Center for XAMPP: Version Management, Configuration, & Security Tools**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)](https://www.microsoft.com/windows)
[![XAMPP](https://img.shields.io/badge/XAMPP-7.x%2B-green.svg)](https://www.apachefriends.org/)

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

**XAMPP Pro Manager** (formerly PHP Manager Enterprise) is a comprehensive desktop application designed to simplify and enhance the XAMPP development experience. It goes beyond simple version management by providing a unified interface for **PHP Version Control**, **Configuration Editing**, **Developer Tools**, and **Security Settings**.

Built with Python and Tkinter, it eliminates the need to manually edit `php.ini`, struggle with DLL conflicts, or use command-line tools for basic tasks. Whether you are switching PHP versions, increasing upload limits, or securing your MySQL database, this tool does it all with a single click.

**The Problem:** Developers waste hours manually editing configuration files, resolving DLL errors after PHP updates, and toggling settings for debugging vs. production.

**The Solution:** A centralized dashboard that automates version switching, provides a GUI for `php.ini` settings, manages extensions, and offers one-click "Dev Mode" toggles.

### ✨ Key Features

#### 🔄 Advanced Version Management
| Feature | Description |
|---------|-------------|
| **Smart Installation** | Download and install compatible PHP versions automatically. |
| **One-Click Switching** | Switch between installed PHP versions instantly without manual file moving. |
| **Auto-DLL Fixer** | Detects and resolves `libssl`, `libcrypto`, and other DLL conflicts between PHP and Apache. |
| **Apache Integration** | Automatically updates `httpd.conf` and `httpd-xampp.conf` to match the active PHP version. |

#### ⚙️ Configuration & Tools (New!)
| Feature | Description |
|---------|-------------|
| **Extension Manager** | Enable/Disable PHP extensions (curl, gd, openssl, etc.) via checkboxes instead of editing text files. |
| **Upload & Memory Limits** | Easily adjust `upload_max_filesize`, `post_max_size`, and `memory_limit` via input fields. |
| **Dev/Prod Mode Toggle** | One-click switch: **Dev Mode** (Errors ON, OpCache OFF) vs **Prod Mode** (Errors OFF, OpCache ON). |
| **MySQL Security** | Set or change the MySQL `root` password directly from the interface. |

#### 🛡️ Reliability & UX
| Feature | Description |
|---------|-------------|
| **Intelligent Backups** | Automatic timestamped backups of PHP folders before any change. |
| **Bilingual Interface** | Full support for **English** and **Arabic** with RTL layout support. |
| **Real-time Logging** | Color-coded operation logs for easy troubleshooting. |
| **Non-Blocking UI** | Multi-threaded operations ensure the interface remains responsive during downloads. |

### 🖼️ User Interface

<div align="center">
  <img width="946" height="855" alt="XAMPP Pro Manager Interface" src="https://github.com/user-attachments/assets/54a035a9-f8e4-42c4-9f2c-877e79c0261e" />
  <br />
  <em>Main Dashboard: Version Management & Server Status</em>
</div>

<div align="center">
  <img width="946" height="855" alt="Configuration Tools" src="https://github.com/user-attachments/assets/PLACEHOLDER_FOR_CONFIG_SCREENSHOT" />
  <br />
  <em>Configuration Hub: Extensions, Limits, and Dev Tools</em>
</div>

*(Note: Replace the placeholder screenshot URL with your actual new screenshot showing the Config & Tools tab)*

### 📋 System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Operating System** | Windows 7 | Windows 10/11 (64-bit) |
| **XAMPP Version** | 7.x | 8.x or higher |
| **Python Version** | 3.7 | 3.11+ |
| **Internet Connection** | Required (for downloads) | Broadband connection |
| **RAM** | 512 MB | 2 GB |
| **Disk Space** | 500 MB | 2 GB |
| **Administrator Rights** | Not required | Recommended for MySQL/Service changes |

### 🔧 Quick Installation

#### Step 1: Install Python Dependencies

Open Command Prompt or PowerShell and run:

```bash
pip install requests beautifulsoup4
