import pytest
from logger.sqlite_logger import init_db

if __name__ == "__main__":
    init_db()
    pytest.main(["tests/test_imu.py"])
