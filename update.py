import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests
import zipfile
import os
import shutil
import subprocess
import threading
import re
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
import sys
import tempfile
import ctypes
import platform
import secrets


class Localization:
    LANGUAGES = {
        'en': 'English',
        'ar': 'العربية'
    }
    
    TEXTS = {
        'en': {
            'window_title': "PHP Manager Enterprise - DLL & Apache Fix",
            'main_title': "PHP Manager Enterprise",
            'subtitle': "Manage PHP versions with automatic Apache & phpMyAdmin compatibility fixes",
            'server_info': "Server Information",
            'php_management': "PHP Version Management",
            'process_status': "Process Status",
            'operation_log': "Operation & Diagnostic Log",
            'change_path': "📁 Change XAMPP Path",
            'refresh_info': "🔄 Refresh Info",
            'check_compat': "🔧 Check Compatibility",
            'load_versions': "🔄 Load Available Versions",
            'install': "📦 Install Version (with DLL Fix)",
            'switch': "🚀 Switch to Version",
            'rollback': "🔙 Restore Backup",
            'clear_log': "Clear Log",
            'fix_dll': "🔧 Fix Current DLL Issues",
            'fix_phpmyadmin': "🐘 Fix phpMyAdmin Issues",
            'restart_apache': "🔄 Restart Apache",
            'no_path': "❌ XAMPP path not selected",
            'path_info': "✅ Path: {path}\n📌 Current PHP Version: {version}\n📁 Apache Folder: {apache}",
            'no_php': "⚠️ Path: {path}\n❌ PHP not found",
            'select_path': "Select XAMPP Installation Folder (Example: C:/xampp)",
            'warning_admin': "It is recommended to run the program as Administrator to avoid permission issues",
            'warning_select_path': "Please select XAMPP path to start management",
            'confirm_install': "Do you want to install PHP {version}?\n\nThis will:\n• Download version compatible with Apache\n• Automatically fix DLL issues\n• Fix phpMyAdmin mysqli extension\n• Update Apache settings\n\nThis may take a few minutes.",
            'confirm_switch': "Do you want to switch to PHP {version}?\n\nThis will:\n• Backup current version\n• Automatically fix DLL issues\n• Fix phpMyAdmin mysqli extension\n• Update Apache settings",
            'confirm_rollback': "Do you want to restore the latest backup?\n\nCompatibility issues will also be fixed automatically.",
            'install_success': "✅ PHP {version} installed successfully!\n\n• DLL issues fixed\n• phpMyAdmin mysqli extension enabled\n• Apache settings updated\n\nPlease restart Apache to apply changes.",
            'switch_success': "✅ Switched to PHP {version} successfully!\n\n• All compatibility issues fixed\n• phpMyAdmin mysqli extension enabled\n\nPlease restart Apache.",
            'rollback_success': "✅ Backup restored successfully!\n\nAll compatibility issues fixed.",
            'fix_success': "DLL issues and phpMyAdmin settings fixed successfully!",
            'phpmyadmin_fix_success': "phpMyAdmin mysqli extension enabled successfully!\n\nPlease restart Apache.",
            'apache_restart_success': "Apache restarted successfully!",
            'error_title': "Error",
            'warning_title': "Warning",
            'success_title': "Success",
            'no_path_error': "Please select XAMPP path first",
            'no_version_error': "Please select PHP version",
            'no_backup_error': "No backups available",
            'install_failed': "Installation failed:\n{error}",
            'switch_failed': "Switch failed:\n{error}",
            'rollback_failed': "Restore failed:\n{error}",
            'fix_failed': "Fix failed:\n{error}",
            'apache_restart_failed': "Apache restart failed. Please restart manually from XAMPP Control Panel.",
            'log_apache_info': "📌 Apache Info: {info}",
            'log_apache_arch': "🏗️ Apache Architecture: {arch}",
            'log_recommend_64': "✅ Recommended to use PHP 64-bit (x64) versions",
            'log_recommend_32': "⚠️ Recommended to use PHP 32-bit (x86) versions for compatibility",
            'log_fetching_versions': "Fetching available PHP versions...",
            'log_versions_fetched': "✅ Fetched {count} PHP versions (compatible with Apache)",
            'log_no_versions': "⚠️ No versions found",
            'log_install_start': "Starting PHP {version} installation with compatibility fixes",
            'log_switch_start': "Starting switch to PHP {version}",
            'log_rollback_start': "Starting backup restore with compatibility fixes",
            'log_fix_start': "Starting DLL fix for version {version}",
            'log_fix_complete': "✅ DLL issues fixed successfully",
            'log_phpmyadmin_fix': "Fixing phpMyAdmin mysqli extension...",
            'log_phpmyadmin_enabled': "✅ mysqli extension enabled in php.ini",
            'log_phpmyadmin_secret': "✅ Updated phpMyAdmin blowfish secret",
            'log_phpmyadmin_tmp': "✅ Created phpMyAdmin temp directory",
            'log_apache_stopped': "Apache stopped",
            'log_apache_started': "✅ Apache started successfully",
            'log_apache_restart_warning': "⚠️ Apache restart failed: {error}",
            'log_manual_restart': "Please restart Apache manually from XAMPP Control Panel",
            'log_php_working': "✅ PHP working correctly: {version}",
            'log_module_loaded': "✅ Module {module} loaded",
            'log_module_warning': "⚠️ Module {module} not loaded",
            'log_apache_config_ok': "✅ Apache configuration is correct",
            'log_apache_config_warning': "⚠️ Apache configuration warning: {error}",
            'log_clear': "Log cleared",
            'log_ready': "Ready",
            'log_mysqli_fixed': "✅ mysqli extension fixed for phpMyAdmin",
            'progress_checking': "Checking compatibility...",
            'progress_downloading': "Downloading PHP...",
            'progress_extracting': "Extracting files...",
            'progress_preparing': "Preparing files...",
            'progress_fixing_dll': "Fixing DLL conflicts...",
            'progress_fixing_phpmyadmin': "Fixing phpMyAdmin mysqli extension...",
            'progress_updating_apache': "Updating Apache settings...",
            'progress_verifying': "Verifying installation...",
            'progress_complete': "Installation complete!",
            'progress_switch': "Switching to PHP {version}...",
            'progress_rollback': "Restoring backup...",
            'progress_fix': "Fixing DLL issues...",
            'progress_loading': "Loading versions..."
        },
        'ar': {
            'window_title': "مدير PHP المتقدم - إصلاح مشاكل DLL و Apache و phpMyAdmin",
            'main_title': "مدير PHP المتقدم",
            'subtitle': "إدارة إصدارات PHP مع إصلاح تلقائي لمشاكل التوافق مع Apache و phpMyAdmin",
            'server_info': "معلومات السيرفر",
            'php_management': "إدارة إصدارات PHP",
            'process_status': "حالة العملية",
            'operation_log': "سجل العمليات والتشخيص",
            'change_path': "📁 تغيير مسار XAMPP",
            'refresh_info': "🔄 تحديث المعلومات",
            'check_compat': "🔧 فحص التوافق",
            'load_versions': "🔄 جلب الإصدارات المتاحة",
            'install': "📦 تثبيت الإصدار (مع إصلاح شامل)",
            'switch': "🚀 التبديل إلى الإصدار",
            'rollback': "🔙 استعادة نسخة احتياطية",
            'clear_log': "مسح السجل",
            'fix_dll': "🔧 إصلاح مشاكل DLL",
            'fix_phpmyadmin': "🐘 إصلاح مشاكل phpMyAdmin",
            'restart_apache': "🔄 إعادة تشغيل Apache",
            'no_path': "❌ لم يتم اختيار مسار XAMPP",
            'path_info': "✅ المسار: {path}\n📌 الإصدار الحالي: {version}\n📁 مجلد Apache: {apache}",
            'no_php': "⚠️ المسار: {path}\n❌ لم يتم العثور على PHP",
            'select_path': "اختر مجلد تثبيت XAMPP (مثال: C:/xampp)",
            'warning_admin': "يوصى بتشغيل البرنامج كمسؤول (Administrator) لتجنب مشاكل الصلاحيات",
            'warning_select_path': "الرجاء تحديد مسار XAMPP لبدء الإدارة",
            'confirm_install': "هل تريد تثبيت PHP {version}؟\n\nسيتم:\n• تحميل الإصدار المتوافق مع Apache\n• إصلاح مشاكل DLL تلقائياً\n• تفعيل mysqli لـ phpMyAdmin\n• تحديث إعدادات Apache\n\nقد يستغرق هذا بضع دقائق.",
            'confirm_switch': "هل تريد التبديل إلى PHP {version}؟\n\nسيتم:\n• عمل نسخة احتياطية للإصدار الحالي\n• إصلاح مشاكل DLL تلقائياً\n• تفعيل mysqli لـ phpMyAdmin\n• تحديث إعدادات Apache",
            'confirm_rollback': "هل تريد استعادة آخر نسخة احتياطية؟\n\nسيتم أيضاً إصلاح مشاكل التوافق تلقائياً.",
            'install_success': "✅ تم تثبيت PHP {version} بنجاح!\n\n• تم إصلاح مشاكل DLL\n• تم تفعيل mysqli لـ phpMyAdmin\n• تم تحديث إعدادات Apache\n\nيرجى إعادة تشغيل Apache لتطبيق التغييرات.",
            'switch_success': "✅ تم التبديل إلى PHP {version} بنجاح!\n\n• تم إصلاح جميع مشاكل التوافق\n• تم تفعيل mysqli لـ phpMyAdmin\n\nيرجى إعادة تشغيل Apache.",
            'rollback_success': "✅ تمت استعادة النسخة الاحتياطية بنجاح!\n\nتم إصلاح جميع مشاكل التوافق.",
            'fix_success': "تم إصلاح مشاكل DLL و phpMyAdmin بنجاح!",
            'phpmyadmin_fix_success': "تم تفعيل mysqli لـ phpMyAdmin بنجاح!\n\nيرجى إعادة تشغيل Apache.",
            'apache_restart_success': "تم إعادة تشغيل Apache بنجاح!",
            'error_title': "خطأ",
            'warning_title': "تحذير",
            'success_title': "نجاح",
            'no_path_error': "الرجاء اختيار مسار XAMPP أولاً",
            'no_version_error': "الرجاء اختيار إصدار PHP",
            'no_backup_error': "لا توجد نسخ احتياطية متاحة",
            'install_failed': "فشل التثبيت:\n{error}",
            'switch_failed': "فشل التبديل:\n{error}",
            'rollback_failed': "فشل الاستعادة:\n{error}",
            'fix_failed': "فشل الإصلاح:\n{error}",
            'apache_restart_failed': "فشل إعادة تشغيل Apache. الرجاء إعادة التشغيل يدوياً من لوحة تحكم XAMPP.",
            'log_apache_info': "📌 معلومات Apache: {info}",
            'log_apache_arch': "🏗️ بنية Apache: {arch}",
            'log_recommend_64': "✅ يوصى باستخدام إصدارات PHP 64-bit (x64)",
            'log_recommend_32': "⚠️ يوصى باستخدام إصدارات PHP 32-bit (x86) للتوافق",
            'log_fetching_versions': "جاري جلب إصدارات PHP المتاحة...",
            'log_versions_fetched': "✅ تم جلب {count} إصداراً من PHP (متوافقة مع Apache)",
            'log_no_versions': "⚠️ لم يتم العثور على إصدارات",
            'log_install_start': "بدء تثبيت PHP {version} مع إصلاح التوافق",
            'log_switch_start': "بدء التبديل إلى PHP {version}",
            'log_rollback_start': "بدء استعادة النسخة الاحتياطية مع إصلاح التوافق",
            'log_fix_start': "بدء إصلاح مشاكل DLL للإصدار {version}",
            'log_fix_complete': "✅ تم إصلاح مشاكل DLL بنجاح",
            'log_phpmyadmin_fix': "جاري إصلاح mysqli لـ phpMyAdmin...",
            'log_phpmyadmin_enabled': "✅ تم تفعيل mysqli في php.ini",
            'log_phpmyadmin_secret': "✅ تم تحديث مفتاح phpMyAdmin",
            'log_phpmyadmin_tmp': "✅ تم إنشاء مجلد مؤقت لـ phpMyAdmin",
            'log_apache_stopped': "تم إيقاف Apache",
            'log_apache_started': "✅ تم تشغيل Apache بنجاح",
            'log_apache_restart_warning': "⚠️ فشل إعادة تشغيل Apache: {error}",
            'log_manual_restart': "يرجى إعادة تشغيل Apache يدوياً من لوحة تحكم XAMPP",
            'log_php_working': "✅ PHP يعمل بشكل صحيح: {version}",
            'log_module_loaded': "✅ تم تحميل وحدة {module}",
            'log_module_warning': "⚠️ لم يتم تحميل وحدة {module}",
            'log_apache_config_ok': "✅ تكوين Apache صحيح",
            'log_apache_config_warning': "⚠️ تحذير في تكوين Apache: {error}",
            'log_clear': "تم مسح السجل",
            'log_ready': "جاهز",
            'log_mysqli_fixed': "✅ تم إصلاح mysqli لـ phpMyAdmin",
            'progress_checking': "جاري التحقق من التوافق...",
            'progress_downloading': "جاري تحميل PHP...",
            'progress_extracting': "جاري استخراج الملفات...",
            'progress_preparing': "جاري تحضير الملفات...",
            'progress_fixing_dll': "جاري إصلاح تعارضات DLL...",
            'progress_fixing_phpmyadmin': "جاري إصلاح mysqli لـ phpMyAdmin...",
            'progress_updating_apache': "جاري تحديث إعدادات Apache...",
            'progress_verifying': "جاري التحقق من التثبيت...",
            'progress_complete': "اكتمل التثبيت!",
            'progress_switch': "جاري التبديل إلى PHP {version}...",
            'progress_rollback': "جاري استعادة النسخة الاحتياطية...",
            'progress_fix': "جاري إصلاح مشاكل DLL...",
            'progress_loading': "جاري جلب الإصدارات..."
        }
    }
    
    def __init__(self, language='en'):
        self.current_language = language
    
    def get(self, key, **kwargs):
        text = self.TEXTS[self.current_language].get(key, key)
        if kwargs:
            text = text.format(**kwargs)
        return text
    
    def set_language(self, language):
        if language in self.LANGUAGES:
            self.current_language = language
            return True
        return False


class PHPManager:
    def __init__(self, xampp_path=None, translator=None):
        self.translator = translator
        
        if xampp_path is None:
            xampp_path = self._auto_detect_xampp()
        
        self.xampp = Path(xampp_path) if xampp_path else None
        
        if self.xampp and self.xampp.exists():
            self.versions_dir = self.xampp / "php_versions"
            self.backups_dir = self.xampp / "php_backups"
            self.temp_dir = self.xampp / "php_temp"
            self.log_file = self.xampp / "php_manager.log"
            self.apache_dir = self.xampp / "apache"
            self.apache_bin = self.apache_dir / "bin"
            self.phpmyadmin_dir = self.xampp / "phpMyAdmin"

            self.versions_dir.mkdir(exist_ok=True, parents=True)
            self.backups_dir.mkdir(exist_ok=True, parents=True)
            self.temp_dir.mkdir(exist_ok=True, parents=True)
        else:
            self.versions_dir = None
            self.backups_dir = None
            self.temp_dir = None
            self.log_file = None
            self.apache_dir = None
            self.apache_bin = None
            self.phpmyadmin_dir = None

    def _auto_detect_xampp(self):
        common_paths = [
            Path("C:/xampp"),
            Path("D:/xampp"),
            Path("E:/xampp"),
            Path("C:/Program Files/xampp"),
            Path("C:/xampp-php8"),
            Path.home() / "xampp"
        ]
        
        for path in common_paths:
            if path.exists() and (path / "php").exists():
                return str(path)
        return None

    def log(self, msg, level="INFO"):
        if self.log_file:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] [{level}] {msg}\n")
        print(f"[{level}] {msg}")

    def get_current_version(self):
        if not self.xampp:
            return None
            
        php = self.xampp / "php" / "php.exe"
        if not php.exists():
            return None

        try:
            out = subprocess.check_output([str(php), "-v"], text=True, timeout=5, stderr=subprocess.STDOUT)
            match = re.search(r"PHP (\d+\.\d+\.\d+)", out)
            return match.group(1) if match else out.split("\n")[0]
        except:
            return None

    def get_apache_info(self):
        try:
            httpd_path = self.apache_bin / "httpd.exe"
            if httpd_path.exists():
                result = subprocess.run([str(httpd_path), "-v"], capture_output=True, text=True, timeout=5)
                version_line = result.stdout.split('\n')[0]
                arch = "x64" if "64" in version_line or "x64" in version_line else "x86"
                return version_line, arch
            return None, None
        except Exception as e:
            self.log(f"Error checking Apache: {str(e)}", "WARNING")
            return None, None

    def fetch_versions(self, stable_only=True):
        versions = set()
        apache_info, apache_arch = self.get_apache_info()
        
        urls = [
            "https://windows.php.net/downloads/releases/releases.json",
            "https://windows.php.net/downloads/releases/"
        ]
        
        for url in urls:
            try:
                if "releases.json" in url:
                    response = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
                    if response.status_code == 200:
                        data = response.json()
                        for version, info in data.items():
                            if version and re.match(r'^\d+\.\d+\.\d+$', version):
                                if apache_arch:
                                    if apache_arch == "x64" and "x64" in str(info):
                                        if stable_only and info.get('stable'):
                                            versions.add(version)
                                    elif apache_arch == "x86" and "x86" in str(info):
                                        if stable_only and info.get('stable'):
                                            versions.add(version)
                                else:
                                    if stable_only and info.get('stable'):
                                        versions.add(version)
                else:
                    response = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.text, "html.parser")
                        for a in soup.find_all("a"):
                            href = a.get("href", "")
                            m = re.search(r"php-(\d+\.\d+\.\d+)-Win32", href)
                            if m:
                                version = m.group(1)
                                if apache_arch == "x64" and "x64" in href:
                                    versions.add(version)
                                elif apache_arch == "x86" and "x86" in href:
                                    versions.add(version)
                                elif not apache_arch:
                                    versions.add(version)
            except Exception as e:
                self.log(f"Failed to fetch from {url}: {str(e)}", "WARNING")
                continue
        
        if not versions:
            versions = self._get_fallback_versions()
        
        return sorted(versions, key=lambda v: [int(x) for x in v.split('.')], reverse=True)

    def _get_fallback_versions(self):
        return [
            "8.3.8", "8.3.7", "8.3.6",
            "8.2.20", "8.2.19", "8.2.18",
            "8.1.29", "8.1.28",
            "8.0.30"
        ]

    def find_download_url(self, version, apache_arch="x64"):
        system_arch = "x64" if platform.machine().endswith('64') else "x86"
        target_arch = apache_arch if apache_arch else system_arch
        
        url_patterns = [
            f"https://windows.php.net/downloads/releases/php-{version}-Win32-vs16-{target_arch}.zip",
            f"https://windows.php.net/downloads/releases/php-{version}-Win32-vs16-{target_arch}_TS.zip",
            f"https://windows.php.net/downloads/releases/php-{version}-nts-Win32-vs16-{target_arch}.zip",
            f"https://windows.php.net/downloads/releases/php-{version}-Win32-vs16-x86.zip",
            f"https://windows.php.net/downloads/releases/php-{version}-Win32-vs16-x64.zip"
        ]
        
        for url in url_patterns:
            try:
                response = requests.head(url, timeout=10, allow_redirects=True)
                if response.status_code == 200:
                    return url
            except:
                continue
        
        try:
            url = "https://windows.php.net/downloads/releases/"
            response = requests.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                for a in soup.find_all("a"):
                    href = a.get("href", "")
                    if version in href and href.endswith(".zip"):
                        if target_arch in href and "nts" not in href:
                            return "https://windows.php.net/downloads/releases/" + href
        except Exception as e:
            self.log(f"Error in manual search: {str(e)}", "WARNING")
        
        return None

    def download(self, version, progress_callback=None):
        apache_info, apache_arch = self.get_apache_info()
        url = self.find_download_url(version, apache_arch)
        
        if not url:
            raise Exception(f"No valid download URL found for PHP {version} (Apache: {apache_arch})")

        file_path = self.temp_dir / f"php_{version}.zip"

        try:
            response = requests.get(url, stream=True, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
            
            if response.status_code != 200:
                raise Exception(f"Download failed: HTTP {response.status_code}")

            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0

            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if progress_callback and total_size > 0:
                            progress = (downloaded / total_size) * 100
                            progress_callback(progress)

            self.log(f"PHP {version} downloaded successfully")
            return file_path

        except Exception as e:
            self.log(f"Download failed: {str(e)}", "ERROR")
            raise

    def fix_phpmyadmin(self):
        php_ini_path = self.xampp / "php" / "php.ini"
        
        msg = self.translator.get('log_phpmyadmin_fix') if self.translator else "Fixing phpMyAdmin mysqli extension..."
        self.log(msg, "INFO")
        
        try:
            modified = False
            
            if not php_ini_path.exists():
                php_ini_prod = self.xampp / "php" / "php.ini-production"
                if php_ini_prod.exists():
                    shutil.copy(php_ini_prod, php_ini_path)
                    self.log("Created php.ini from php.ini-production", "INFO")
                    modified = True
            
            if php_ini_path.exists():
                with open(php_ini_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                mysqli_patterns = [
                    (';extension=mysqli', 'extension=mysqli'),
                    (';extension=php_mysqli.dll', 'extension=mysqli'),
                    ('extension=mysqli', 'extension=mysqli'),
                ]
                
                mysqli_found = False
                for search, replace in mysqli_patterns:
                    if search in content:
                        content = content.replace(search, replace)
                        mysqli_found = True
                        modified = True
                        self.log("Enabled mysqli extension in php.ini", "SUCCESS")
                        break
                
                if not mysqli_found and 'extension=mysqli' not in content:
                    content += "\n; Extensions for phpMyAdmin\nextension=mysqli\n"
                    modified = True
                    self.log("Added mysqli extension to php.ini", "SUCCESS")
                
                if ';extension=pdo_mysql' in content:
                    content = content.replace(';extension=pdo_mysql', 'extension=pdo_mysql')
                    modified = True
                    self.log("Enabled pdo_mysql extension", "SUCCESS")
                
                if ';extension_dir = "ext"' in content:
                    content = content.replace(';extension_dir = "ext"', 'extension_dir = "ext"')
                    modified = True
                
                if 'memory_limit = 128M' in content:
                    content = content.replace('memory_limit = 128M', 'memory_limit = 256M')
                    modified = True
                
                if modified:
                    with open(php_ini_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    self.log("php.ini updated for phpMyAdmin compatibility", "SUCCESS")
            
            if self.phpmyadmin_dir and self.phpmyadmin_dir.exists():
                phpmyadmin_tmp = self.phpmyadmin_dir / "tmp"
                if not phpmyadmin_tmp.exists():
                    phpmyadmin_tmp.mkdir(parents=True, exist_ok=True)
                    self.log("Created phpMyAdmin temp directory", "SUCCESS")
                
                config_file = self.phpmyadmin_dir / "config.inc.php"
                if config_file.exists():
                    with open(config_file, 'r', encoding='utf-8', errors='ignore') as f:
                        config_content = f.read()
                    
                    if "blowfish_secret" in config_content:
                        if "''" in config_content or "''" in config_content:
                            new_secret = secrets.token_hex(32)
                            config_content = re.sub(
                                r"\$cfg\['blowfish_secret'\]\s*=\s*['\"][^'\"]*['\"];",
                                f"$cfg['blowfish_secret'] = '{new_secret}';",
                                config_content
                            )
                            with open(config_file, 'w', encoding='utf-8') as f:
                                f.write(config_content)
                            self.log("Updated phpMyAdmin blowfish secret", "SUCCESS")
            
            return True
            
        except Exception as e:
            self.log(f"Error fixing phpMyAdmin: {str(e)}", "WARNING")
            return False

    def fix_dll_conflicts(self, php_version):
        php_path = self.xampp / "php"
        apache_bin = self.apache_bin
        
        self.log("Starting DLL conflict fixes...", "INFO")
        
        conflict_files = [
            "libssl-1_1-x64.dll",
            "libssl-1_1-x86.dll",
            "libcrypto-1_1-x64.dll",
            "libcrypto-1_1-x86.dll",
            "libssh2.dll",
            "libcurl.dll",
            "zlib1.dll",
            "libpng.dll",
            "libjpeg.dll"
        ]
        
        try:
            for file in conflict_files:
                php_dll = php_path / file
                apache_dll = apache_bin / file
                
                if php_dll.exists():
                    shutil.copy2(php_dll, apache_dll)
                    self.log(f"Updated {file} in Apache folder", "INFO")
            
            self._optimize_php_ini(php_version)
            self.fix_phpmyadmin()
            
            self.log("DLL conflicts fixed successfully", "SUCCESS")
            return True
            
        except Exception as e:
            self.log(f"Error fixing DLL: {str(e)}", "ERROR")
            return False

    def _optimize_php_ini(self, php_version):
        php_ini_path = self.xampp / "php" / "php.ini"
        php_ini_production = self.xampp / "php" / "php.ini-production"
        
        if php_ini_production.exists():
            shutil.copy(php_ini_production, php_ini_path)
        
        if php_ini_path.exists():
            try:
                with open(php_ini_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                compatibility_settings = {
                    ';extension_dir = "ext"': 'extension_dir = "ext"',
                    ';extension=php_mysqli.dll': 'extension=mysqli',
                    ';extension=php_pdo_mysql.dll': 'extension=pdo_mysql',
                    ';extension=php_openssl.dll': 'extension=openssl',
                    ';extension=php_mbstring.dll': 'extension=mbstring',
                    ';extension=php_curl.dll': 'extension=curl',
                    ';extension=php_gd2.dll': 'extension=gd',
                    'max_execution_time = 30': 'max_execution_time = 300',
                    'max_input_time = 60': 'max_input_time = 300',
                    'memory_limit = 128M': 'memory_limit = 256M',
                    'post_max_size = 8M': 'post_max_size = 100M',
                    'upload_max_filesize = 2M': 'upload_max_filesize = 100M',
                    ';date.timezone =': 'date.timezone = "Asia/Riyadh"',
                    'display_errors = Off': 'display_errors = On',
                    'log_errors = Off': 'log_errors = On',
                    'enable_dl = Off': 'enable_dl = On',
                    ';cgi.fix_pathinfo=1': 'cgi.fix_pathinfo=1',
                }
                
                for search, replace in compatibility_settings.items():
                    if search in content:
                        content = content.replace(search, replace)
                    elif replace.split('=')[0].strip() not in content:
                        content += f"\n{replace}"
                
                xampp_specific = """
; XAMPP specific settings
[Apache]
engine = 1
cgi.fix_pathinfo = 1

; phpMyAdmin specific settings
[phpMyAdmin]
mysqli.allow_local_infile = On
mysqli.reconnect = On

; Thread Safety
zend_extension=opcache
opcache.enable=1
opcache.memory_consumption=128
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=4000
opcache.revalidate_freq=60
opcache.fast_shutdown=1
"""
                content += xampp_specific
                
                with open(php_ini_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.log("Optimized php.ini created for compatibility", "SUCCESS")
                return True
                
            except Exception as e:
                self.log(f"Error creating php.ini: {str(e)}", "WARNING")
                return False
        
        return False

    def update_apache_config(self, php_version):
        httpd_conf = self.apache_dir / "conf" / "httpd.conf"
        xampp_conf = self.apache_dir / "conf" / "extra" / "httpd-xampp.conf"
        
        php_path = self.xampp / "php"
        
        try:
            php_module = None
            for file in php_path.glob("php*apache*.dll"):
                php_module = file.name
                break
            
            if not php_module:
                self.log("No suitable Apache module found", "WARNING")
                return False
            
            if httpd_conf.exists():
                with open(httpd_conf, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                php_module_pattern = r'LoadModule php_module .*\.dll'
                new_php_module = f'LoadModule php_module "{php_path / php_module}"'
                content = re.sub(php_module_pattern, new_php_module, content)
                
                php_ini_pattern = r'PHPIniDir .*'
                new_php_ini = f'PHPIniDir "{php_path}"'
                content = re.sub(php_ini_pattern, new_php_ini, content)
                
                if r'<FilesMatch "\.php$">' not in content:
                    php_handler = r"""
<FilesMatch "\.php$">
    SetHandler application/x-httpd-php
</FilesMatch>
"""
                    content += php_handler 
                with open(httpd_conf, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.log("httpd.conf updated", "SUCCESS")
            
            if xampp_conf.exists():
                with open(xampp_conf, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                content = re.sub(r'PHPINIDir .*', f'PHPINIDir "{php_path}"', content)
                content = re.sub(r'LoadModule php_module .*\.dll', new_php_module, content)
                
                with open(xampp_conf, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                self.log("httpd-xampp.conf updated", "SUCCESS")
            
            return True
            
        except Exception as e:
            self.log(f"Error updating Apache: {str(e)}", "ERROR")
            return False

    def install(self, version, progress_callback=None):
        try:
            if progress_callback:
                msg = self.translator.get('progress_checking') if self.translator else "Checking compatibility..."
                progress_callback(5, msg)
            
            apache_info, apache_arch = self.get_apache_info()
            self.log(f"Apache Info: {apache_info} (Arch: {apache_arch})", "INFO")
            
            if progress_callback:
                msg = self.translator.get('progress_downloading') if self.translator else "Downloading PHP..."
                progress_callback(10, msg)
            
            zip_path = self.download(version, 
                lambda p: progress_callback(10 + p * 0.3, "Downloading...") if progress_callback else None)

            install_path = self.versions_dir / f"php_{version}"

            if install_path.exists():
                shutil.rmtree(install_path)

            if progress_callback:
                msg = self.translator.get('progress_extracting') if self.translator else "Extracting files..."
                progress_callback(50, msg)

            self._extract_zip(zip_path, install_path)
            
            if progress_callback:
                msg = self.translator.get('progress_preparing') if self.translator else "Preparing files..."
                progress_callback(70, msg)

            current_php = self.xampp / "php"
            if current_php.exists():
                backup = self.backups_dir / f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                shutil.copytree(current_php, backup)
                self.log(f"Backup created at {backup}", "INFO")
                
                for item in current_php.iterdir():
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir() and item.name not in ['ext', 'dev', 'include']:
                        shutil.rmtree(item)
            
            for item in install_path.iterdir():
                dest = current_php / item.name
                if item.is_dir():
                    if dest.exists():
                        shutil.rmtree(dest)
                    shutil.copytree(item, dest)
                else:
                    shutil.copy2(item, dest)
            
            if progress_callback:
                msg = self.translator.get('progress_fixing_dll') if self.translator else "Fixing DLL conflicts..."
                progress_callback(80, msg)
            
            self.fix_dll_conflicts(version)
            
            if progress_callback:
                msg = self.translator.get('progress_updating_apache') if self.translator else "Updating Apache settings..."
                progress_callback(90, msg)
            
            self.update_apache_config(version)
            
            if progress_callback:
                msg = self.translator.get('progress_verifying') if self.translator else "Verifying installation..."
                progress_callback(95, msg)
            
            self._verify_installation(version)
            
            if zip_path.exists():
                zip_path.unlink()

            self.log(f"PHP {version} installed successfully with full compatibility", "SUCCESS")
            
            if progress_callback:
                msg = self.translator.get('progress_complete') if self.translator else "Installation complete!"
                progress_callback(100, msg)
            
            return install_path

        except Exception as e:
            self.log(f"Installation failed: {str(e)}", "ERROR")
            raise

    def _verify_installation(self, version):
        php_path = self.xampp / "php" / "php.exe"
        
        try:
            result = subprocess.run([str(php_path), "-v"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                version_text = result.stdout.split()[1] if len(result.stdout.split()) > 1 else version
                self.log(f"✅ PHP working correctly: {version_text}", "SUCCESS")
            
            result = subprocess.run([str(php_path), "-m"], capture_output=True, text=True, timeout=5)
            modules = result.stdout
            required_modules = ['mysqli', 'pdo_mysql', 'openssl', 'mbstring', 'curl']
            
            mysqli_found = False
            for module in required_modules:
                if module in modules:
                    self.log(f"✅ Module {module} loaded", "SUCCESS")
                    if module == 'mysqli':
                        mysqli_found = True
                else:
                    self.log(f"⚠️ Module {module} not loaded", "WARNING")
            
            if not mysqli_found:
                self.log("⚠️ mysqli extension not loaded - phpMyAdmin may not work", "WARNING")
                self.fix_phpmyadmin()
            
            httpd_path = self.apache_bin / "httpd.exe"
            if httpd_path.exists():
                result = subprocess.run([str(httpd_path), "-t"], capture_output=True, text=True, timeout=5)
                if "Syntax OK" in result.stdout:
                    self.log("✅ Apache configuration is correct", "SUCCESS")
                else:
                    self.log(f"⚠️ Apache configuration warning: {result.stderr}", "WARNING")
            
            return True
            
        except Exception as e:
            self.log(f"Verification error: {str(e)}", "ERROR")
            return False

    def _extract_zip(self, zip_path, target):
        target = Path(target)
        target.mkdir(exist_ok=True, parents=True)

        try:
            with zipfile.ZipFile(zip_path, "r") as z:
                for file in z.namelist():
                    out_path = target / file
                    if not str(out_path.resolve()).startswith(str(target.resolve())):
                        raise Exception("Unsafe zip detected")
                z.extractall(target)
            
            self.log(f"Files extracted to {target}")
            return True

        except Exception as e:
            self.log(f"Extraction failed: {str(e)}", "ERROR")
            raise

    def switch_version(self, version):
        target_version_dir = self.versions_dir / f"php_{version}"
        current_php = self.xampp / "php"

        if not target_version_dir.exists():
            raise Exception(f"Version {version} not installed. Please install it first")

        try:
            if current_php.exists():
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                backup = self.backups_dir / f"pre_switch_backup_{timestamp}"
                shutil.copytree(current_php, backup)
                self.log(f"Backup created before switch", "INFO")

            if current_php.exists():
                for item in current_php.iterdir():
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir() and item.name not in ['ext', 'dev', 'include', 'pear']:
                        shutil.rmtree(item)

            for item in target_version_dir.iterdir():
                dest = current_php / item.name
                if item.is_dir():
                    if dest.exists():
                        shutil.rmtree(dest)
                    shutil.copytree(item, dest)
                else:
                    shutil.copy2(item, dest)

            self.fix_dll_conflicts(version)
            self.update_apache_config(version)
            self._verify_installation(version)

            self.log(f"Switched to PHP {version} successfully", "SUCCESS")
            return True

        except Exception as e:
            self.log(f"Switch failed: {str(e)}", "ERROR")
            raise

    def rollback(self):
        backups = sorted(self.backups_dir.glob("*"), key=os.path.getctime, reverse=True)

        if not backups:
            raise Exception("No backups available")

        latest = backups[0]
        current = self.xampp / "php"

        try:
            if current.exists():
                shutil.rmtree(current)

            shutil.copytree(latest, current)
            
            version = self.get_current_version()
            if version:
                version_num = version.split()[1] if ' ' in version else version
                self.fix_dll_conflicts(version_num)
                self.update_apache_config(version_num)
            
            self.log(f"Restored from backup: {latest.name}", "SUCCESS")
            return True
            
        except Exception as e:
            self.log(f"Restore failed: {str(e)}", "ERROR")
            raise

    def get_installed_versions(self):
        if not self.versions_dir.exists():
            return []
        
        versions = []
        for version_dir in self.versions_dir.glob("php_*"):
            version = version_dir.name.replace("php_", "")
            versions.append(version)
        
        return sorted(versions, key=lambda v: [int(x) for x in v.split('.')], reverse=True)


class AppUI:
    def __init__(self, root):
        self.root = root
        self.translator = Localization('en')
        
        self.root.title(self.translator.get('window_title'))
        self.root.geometry("950x800")
        
        self.manager = None
        self.xampp_path = tk.StringVar()
        self.version_var = tk.StringVar()
        self.progress_var = tk.DoubleVar()
        
        self._build_ui()
        self.root.after(100, self._prompt_xampp_path)

    def change_language(self):
        current_lang = self.translator.current_language
        new_lang = 'ar' if current_lang == 'en' else 'en'
        self.translator.set_language(new_lang)
        
        self.root.title(self.translator.get('window_title'))
        self._update_texts()
        self.status_label.config(text=self.translator.get('log_ready'))
        
        if self.manager and self.manager.xampp:
            self.update_info()
        
        self._log_msg(self.translator.get('log_clear') if new_lang == 'en' else "تم تغيير اللغة", "info")

    def _update_texts(self):
        self.title_label.config(text=self.translator.get('main_title'))
        self.subtitle_label.config(text=self.translator.get('subtitle'))
        self.info_frame.config(text=self.translator.get('server_info'))
        self.version_frame.config(text=self.translator.get('php_management'))
        self.progress_frame.config(text=self.translator.get('process_status'))
        self.log_frame.config(text=self.translator.get('operation_log'))
        
        self.btn_change_path.config(text=self.translator.get('change_path'))
        self.btn_refresh_info.config(text=self.translator.get('refresh_info'))
        self.btn_check_compat.config(text=self.translator.get('check_compat'))
        self.btn_load_versions.config(text=self.translator.get('load_versions'))
        self.btn_install.config(text=self.translator.get('install'))
        self.btn_switch.config(text=self.translator.get('switch'))
        self.btn_rollback.config(text=self.translator.get('rollback'))
        self.btn_clear_log.config(text=self.translator.get('clear_log'))
        self.btn_fix_dll.config(text=self.translator.get('fix_dll'))
        self.btn_fix_phpmyadmin.config(text=self.translator.get('fix_phpmyadmin'))
        self.btn_restart_apache.config(text=self.translator.get('restart_apache'))
        
        self.btn_language.config(text=f"🌐 {self.translator.LANGUAGES[self.translator.current_language]}")
        self.select_label.config(text="Select version:" if self.translator.current_language == 'en' else "اختر الإصدار:")

    def _build_ui(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        header_frame = tk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.title_label = tk.Label(header_frame, text=self.translator.get('main_title'), 
                                    font=("Arial", 18, "bold"), fg="#2c3e50")
        self.title_label.pack(side=tk.LEFT)
        
        self.btn_language = tk.Button(header_frame, text="🌐 English", 
                                     command=self.change_language,
                                     bg="#3498db", fg="white", padx=15, pady=5)
        self.btn_language.pack(side=tk.RIGHT)
        
        self.subtitle_label = tk.Label(main_frame, text=self.translator.get('subtitle'), 
                                       font=("Arial", 10), fg="#7f8c8d")
        self.subtitle_label.pack(pady=(0, 20))
        
        self.info_frame = tk.LabelFrame(main_frame, text=self.translator.get('server_info'), 
                                        font=("Arial", 11, "bold"))
        self.info_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.info_label = tk.Label(self.info_frame, text=self.translator.get('no_path'), 
                                   font=("Arial", 9), justify=tk.LEFT)
        self.info_label.pack(padx=10, pady=10, anchor=tk.W)
        
        control_frame = tk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.btn_change_path = tk.Button(control_frame, text=self.translator.get('change_path'), 
                                        command=self._prompt_xampp_path,
                                        bg="#3498db", fg="white", padx=15, pady=5)
        self.btn_change_path.pack(side=tk.LEFT, padx=5)
        
        self.btn_refresh_info = tk.Button(control_frame, text=self.translator.get('refresh_info'), 
                                         command=self.update_info,
                                         bg="#95a5a6", fg="white", padx=15, pady=5)
        self.btn_refresh_info.pack(side=tk.LEFT, padx=5)
        
        self.btn_check_compat = tk.Button(control_frame, text=self.translator.get('check_compat'), 
                                         command=self._check_apache_compat,
                                         bg="#e67e22", fg="white", padx=15, pady=5)
        self.btn_check_compat.pack(side=tk.LEFT, padx=5)
        
        self.version_frame = tk.LabelFrame(main_frame, text=self.translator.get('php_management'), 
                                          font=("Arial", 11, "bold"))
        self.version_frame.pack(fill=tk.X, pady=(0, 15))
        
        select_frame = tk.Frame(self.version_frame)
        select_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.select_label = tk.Label(select_frame, text="Select version:", font=("Arial", 10))
        self.select_label.pack(side=tk.LEFT, padx=5)
        
        self.combo = ttk.Combobox(select_frame, textvariable=self.version_var, width=35, state="readonly")
        self.combo.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        button_frame = tk.Frame(self.version_frame)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.btn_load_versions = tk.Button(button_frame, text=self.translator.get('load_versions'), 
                                          command=self.load_versions,
                                          bg="#3498db", fg="white", padx=15, pady=5)
        self.btn_load_versions.pack(side=tk.LEFT, padx=5)
        
        self.btn_install = tk.Button(button_frame, text=self.translator.get('install'), 
                                    command=self.install,
                                    bg="#27ae60", fg="white", padx=15, pady=5)
        self.btn_install.pack(side=tk.LEFT, padx=5)
        
        self.btn_switch = tk.Button(button_frame, text=self.translator.get('switch'), 
                                   command=self.switch,
                                   bg="#e67e22", fg="white", padx=15, pady=5)
        self.btn_switch.pack(side=tk.LEFT, padx=5)
        
        self.btn_rollback = tk.Button(button_frame, text=self.translator.get('rollback'), 
                                     command=self.rollback,
                                     bg="#e74c3c", fg="white", padx=15, pady=5)
        self.btn_rollback.pack(side=tk.LEFT, padx=5)
        
        self.progress_frame = tk.LabelFrame(main_frame, text=self.translator.get('process_status'), 
                                           font=("Arial", 11, "bold"))
        self.progress_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.progress_bar = ttk.Progressbar(self.progress_frame, variable=self.progress_var, 
                                           mode="determinate", length=500)
        self.progress_bar.pack(padx=10, pady=10, fill=tk.X)
        
        self.status_label = tk.Label(self.progress_frame, text=self.translator.get('log_ready'), 
                                     font=("Arial", 9), fg="#2c3e50")
        self.status_label.pack(pady=(0, 10))
        
        self.log_frame = tk.LabelFrame(main_frame, text=self.translator.get('operation_log'), 
                                      font=("Arial", 11, "bold"))
        self.log_frame.pack(fill=tk.BOTH, expand=True)
        
        text_frame = tk.Frame(self.log_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.log_box = tk.Text(text_frame, height=15, yscrollcommand=scrollbar.set,
                              font=("Consolas", 9), wrap=tk.WORD)
        self.log_box.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.log_box.yview)
        
        extra_buttons = tk.Frame(self.log_frame)
        extra_buttons.pack(fill=tk.X, padx=5, pady=5)
        
        self.btn_clear_log = tk.Button(extra_buttons, text=self.translator.get('clear_log'), 
                                      command=self.clear_log,
                                      bg="#95a5a6", fg="white", padx=10)
        self.btn_clear_log.pack(side=tk.LEFT, padx=5)
        
        self.btn_fix_dll = tk.Button(extra_buttons, text=self.translator.get('fix_dll'), 
                                    command=self._fix_dll_threaded,
                                    bg="#e67e22", fg="white", padx=10)
        self.btn_fix_dll.pack(side=tk.LEFT, padx=5)
        
        self.btn_fix_phpmyadmin = tk.Button(extra_buttons, text=self.translator.get('fix_phpmyadmin'), 
                                           command=self._fix_pma_threaded,
                                           bg="#9b59b6", fg="white", padx=10)
        self.btn_fix_phpmyadmin.pack(side=tk.LEFT, padx=5)
        
        self.btn_restart_apache = tk.Button(extra_buttons, text=self.translator.get('restart_apache'), 
                                           command=self.restart_apache,
                                           bg="#3498db", fg="white", padx=10)
        self.btn_restart_apache.pack(side=tk.LEFT, padx=5)

    def _prompt_xampp_path(self):
        path = filedialog.askdirectory(title=self.translator.get('select_path'))
        if path:
            self.xampp_path.set(path)
            self.manager = PHPManager(path, self.translator)
            self.update_info()
            self._check_apache_compat()
            self.load_versions()
        else:
            temp_manager = PHPManager(None, self.translator)
            if temp_manager.xampp and temp_manager.xampp.exists():
                self.xampp_path.set(str(temp_manager.xampp))
                self.manager = temp_manager
                self.update_info()
                self._check_apache_compat()
                self.load_versions()
            else:
                messagebox.showwarning(self.translator.get('warning_title'), 
                                      self.translator.get('warning_select_path'))

    def _check_apache_compat(self):
        if self.manager:
            apache_info, arch = self.manager.get_apache_info()
            if apache_info:
                self._log_msg(self.translator.get('log_apache_info', info=apache_info), "info")
                self._log_msg(self.translator.get('log_apache_arch', arch=arch), "info")
                
                if arch == "x64":
                    self._log_msg(self.translator.get('log_recommend_64'), "success")
                else:
                    self._log_msg(self.translator.get('log_recommend_32'), "warning")

    def update_info(self):
        if self.manager and self.manager.xampp:
            current = self.manager.get_current_version()
            if current:
                self.info_label.config(text=self.translator.get('path_info', 
                    path=self.manager.xampp, version=current, apache=self.manager.apache_bin))
            else:
                self.info_label.config(text=self.translator.get('no_php', path=self.manager.xampp))
        else:
            self.info_label.config(text=self.translator.get('no_path'))

    def _fix_dll_threaded(self):
        if not self.manager:
            messagebox.showerror(self.translator.get('error_title'), self.translator.get('no_path_error'))
            return
        
        def task():
            try:
                self._update_progress(0, self.translator.get('progress_fix'))
                current_version = self.manager.get_current_version()
                if current_version:
                    version_num = current_version.split()[1] if ' ' in current_version else current_version
                    self._log_msg(self.translator.get('log_fix_start', version=version_num))
                    
                    self.manager.fix_dll_conflicts(version_num)
                    self.manager.update_apache_config(version_num)
                    
                    self._log_msg(self.translator.get('log_fix_complete'), "success")
                    self._update_progress(100, self.translator.get('log_ready'))
                    messagebox.showinfo(self.translator.get('success_title'), self.translator.get('fix_success'))
                else:
                    self._log_msg(self.translator.get('no_version_error'), "error")
            except Exception as e:
                self._log_msg(self.translator.get('fix_failed', error=str(e)), "error")
            finally:
                self.root.after(2000, lambda: self._update_progress(0, self.translator.get('log_ready')))
        
        threading.Thread(target=task, daemon=True).start()

    def _fix_pma_threaded(self):
        if not self.manager:
            messagebox.showerror(self.translator.get('error_title'), self.translator.get('no_path_error'))
            return
        
        def task():
            try:
                self._update_progress(0, self.translator.get('progress_fixing_phpmyadmin'))
                self._log_msg(self.translator.get('log_phpmyadmin_fix'), "info")
                
                result = self.manager.fix_phpmyadmin()
                
                if result:
                    self._log_msg(self.translator.get('log_mysqli_fixed'), "success")
                    self._update_progress(100, self.translator.get('log_ready'))
                    messagebox.showinfo(self.translator.get('success_title'), 
                                       self.translator.get('phpmyadmin_fix_success'))
                else:
                    self._log_msg("Failed to fix phpMyAdmin issues", "error")
            except Exception as e:
                self._log_msg(f"Error: {str(e)}", "error")
            finally:
                self.root.after(2000, lambda: self._update_progress(0, self.translator.get('log_ready')))
        
        threading.Thread(target=task, daemon=True).start()

    def restart_apache(self):
        if not self.manager:
            messagebox.showerror(self.translator.get('error_title'), self.translator.get('no_path_error'))
            return
        
        try:
            subprocess.run(["net", "stop", "Apache2.4"], capture_output=True, timeout=10)
            self._log_msg(self.translator.get('log_apache_stopped'), "info")
            
            subprocess.run(["net", "start", "Apache2.4"], capture_output=True, timeout=10)
            self._log_msg(self.translator.get('log_apache_started'), "success")
            
            messagebox.showinfo(self.translator.get('success_title'), self.translator.get('apache_restart_success'))
        except Exception as e:
            self._log_msg(self.translator.get('log_apache_restart_warning', error=str(e)), "warning")
            self._log_msg(self.translator.get('log_manual_restart'), "warning")

    def clear_log(self):
        self.log_box.delete(1.0, tk.END)
        self._log_msg(self.translator.get('log_clear'), "info")

    def _log_msg(self, msg, level="INFO"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        tag = level.lower()
        if tag not in self.log_box.tag_names():
            if tag == "error":
                self.log_box.tag_config(tag, foreground="#e74c3c")
            elif tag == "warning":
                self.log_box.tag_config(tag, foreground="#f39c12")
            elif tag == "success":
                self.log_box.tag_config(tag, foreground="#27ae60")
            else:
                self.log_box.tag_config(tag, foreground="#2c3e50")
        
        self.log_box.insert(tk.END, f"[{timestamp}] {msg}\n", tag)
        self.log_box.see(tk.END)
        
        if self.manager:
            self.manager.log(msg, level)

    def _update_progress(self, value, message=None):
        self.progress_var.set(value)
        if message:
            self.status_label.config(text=message)
        self.root.update_idletasks()

    def load_versions(self):
        if not self.manager:
            messagebox.showerror(self.translator.get('error_title'), self.translator.get('no_path_error'))
            return
            
        def task():
            try:
                self._update_progress(0, self.translator.get('progress_loading'))
                self._log_msg(self.translator.get('log_fetching_versions'), "info")
                versions = self.manager.fetch_versions()
                self.root.after(0, lambda: self.combo.configure(values=versions))
                if versions:
                    self.root.after(0, lambda: self.version_var.set(versions[0]))
                    self._log_msg(self.translator.get('log_versions_fetched', count=len(versions)), "success")
                else:
                    self._log_msg(self.translator.get('log_no_versions'), "warning")
                self._update_progress(100, self.translator.get('log_ready'))
                self.root.after(2000, lambda: self._update_progress(0, self.translator.get('log_ready')))
            except Exception as e:
                self._log_msg(self.translator.get('install_failed', error=str(e)), "error")
                self._update_progress(0, "Error")

        threading.Thread(target=task, daemon=True).start()

    def install(self):
        if not self.manager:
            messagebox.showerror(self.translator.get('error_title'), self.translator.get('no_path_error'))
            return
            
        version = self.version_var.get()
        if not version:
            messagebox.showerror(self.translator.get('error_title'), self.translator.get('no_version_error'))
            return
        
        if not messagebox.askyesno("Confirm", self.translator.get('confirm_install', version=version)):
            return
        
        def task():
            try:
                self._update_progress(0, self.translator.get('progress_switch', version=version))
                self._log_msg(self.translator.get('log_install_start', version=version))
                
                self.manager.install(version, self._update_progress)
                
                self.root.after(0, lambda: messagebox.showinfo(self.translator.get('success_title'), 
                    self.translator.get('install_success', version=version)))
                
                self._log_msg(self.translator.get('log_fix_complete'), "success")
                self.update_info()
                self._update_progress(100, self.translator.get('progress_complete'))
                
            except Exception as e:
                self._log_msg(self.translator.get('install_failed', error=str(e)), "error")
                self._update_progress(0, "Failed")
                self.root.after(0, lambda: messagebox.showerror(self.translator.get('error_title'), 
                    self.translator.get('install_failed', error=str(e))))
        
        threading.Thread(target=task, daemon=True).start()

    def switch(self):
        if not self.manager:
            messagebox.showerror(self.translator.get('error_title'), self.translator.get('no_path_error'))
            return
            
        version = self.version_var.get()
        if not version:
            messagebox.showerror(self.translator.get('error_title'), self.translator.get('no_version_error'))
            return
        
        if not messagebox.askyesno("Confirm", self.translator.get('confirm_switch', version=version)):
            return
        
        def task():
            try:
                self._update_progress(0, self.translator.get('progress_switch', version=version))
                self._log_msg(self.translator.get('log_switch_start', version=version))
                
                self.manager.switch_version(version)
                
                self.root.after(0, lambda: messagebox.showinfo(self.translator.get('success_title'), 
                    self.translator.get('switch_success', version=version)))
                
                self._log_msg(self.translator.get('log_fix_complete'), "success")
                self.update_info()
                self._update_progress(100, self.translator.get('log_ready'))
                
            except Exception as e:
                self._log_msg(self.translator.get('switch_failed', error=str(e)), "error")
                self._update_progress(0, "Failed")
                self.root.after(0, lambda: messagebox.showerror(self.translator.get('error_title'), 
                    self.translator.get('switch_failed', error=str(e))))
        
        threading.Thread(target=task, daemon=True).start()

    def rollback(self):
        if not self.manager:
            messagebox.showerror(self.translator.get('error_title'), self.translator.get('no_path_error'))
            return
        
        if not messagebox.askyesno("Confirm", self.translator.get('confirm_rollback')):
            return
        
        def task():
            try:
                self._update_progress(0, self.translator.get('progress_rollback'))
                self._log_msg(self.translator.get('log_rollback_start'))
                
                self.manager.rollback()
                
                self.root.after(0, lambda: messagebox.showinfo(self.translator.get('success_title'), 
                    self.translator.get('rollback_success')))
                
                self._log_msg(self.translator.get('log_fix_complete'), "success")
                self.update_info()
                self._update_progress(100, self.translator.get('log_ready'))
                
            except Exception as e:
                self._log_msg(self.translator.get('rollback_failed', error=str(e)), "error")
                self._update_progress(0, "Failed")
                self.root.after(0, lambda: messagebox.showerror(self.translator.get('error_title'), 
                    self.translator.get('rollback_failed', error=str(e))))
        
        threading.Thread(target=task, daemon=True).start()


if __name__ == "__main__":
    if platform.system() == "Windows":
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if not is_admin:
                temp_translator = Localization('en')
                messagebox.showwarning("Warning", 
                    "It is recommended to run the program as Administrator to avoid permission issues")
        except:
            pass
    
    root = tk.Tk()
    app = AppUI(root)
    root.mainloop()
