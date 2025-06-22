# Embedded Test Automation Framework

A Python-based test automation framework designed for embedded sensor validation. Originally built to test MEMS IMU sensors (accelerometer and gyroscope), this framework allows automated data collection, validation, and diagnostics using a pluggable architecture and persistent logging.

---

## 📌 Features

- Modular sensor interface (mock or real hardware)
- Automated unit and integration testing with `pytest`
- Sensor data acquisition via I2C/UART (mocked for Windows)
- Result logging to an SQLite database
- Optional export to Google BigQuery
- Support for visualizing test trends

---

## 📁 Project Structure
embedded_test_framework/
├── sensors/
│ ├── imu_interface.py # Sensor abstraction (real or mock)
│
├── tests/
│ └── test_imu.py # Pytest-based test suite
│
├── logger/
│ └── sqlite_logger.py # Logs sensor data into SQLite
│
├── config.py # Sensor configuration and constants
├── main.py # Test runner entry point
├── view_logs.py # Script to view test results
├── requirements.txt # Required Python packages
└── README.md
