# 🖥️ System Health Check Scripts (Python)

This repository contains a collection of small Python utilities designed to monitor basic system health conditions, such as **disk space** and **pending reboots**. These tools are ideal for basic system administration and automation tasks.

---

## 📂 Scripts Included

### 1. `all_checks.py`

Checks:
- If the system has a **pending reboot** (based on `/run/reboot-required`)
- If the **root partition** (`/`) has **less than 2 GB** or **less than 10%** free space

📌 Exits with:
- Code `1` if any issue is detected
- Code `0` if everything is OK

---

### 2. `all_checks2.py`

A variant of the script above, but split into more granular functions:
- `check_reboot()` – checks for `/run/reboot-required`
- `check_disk_full()` – reusable function to check any partition
- `check_root_full()` – specifically checks the root (`/`) partition

📌 Helpful if you want to reuse `check_disk_full()` for other disks later.

---

### 3. `disk_usage.py`

Standalone script that checks:
- If **`/`** has **at least 2 GB** and **10% free space**

📌 Simpler and cleaner if you only care about disk space usage and not reboot status.

---

## ▶️ How to Use

Run any script from the terminal using Python 3:

```
python3 all_checks.py
```
Or for the reboot and disk check:
```
python3 all_checks2.py

```
Scripts return meaningful exit codes, making them easy to use in cron jobs or systemd services.

---

## 🛠️ Requirements
- Python 3.x
- Unix-based system (Linux, macOS) — shutil and os.path.exists() are platform-safe, but /run/reboot-required exists only on Linux.

## ⚠️ Notes
- These scripts are tailored for Linux systems.
- Windows paths like C:\\ would need to be used if adapted for Windows.

---
