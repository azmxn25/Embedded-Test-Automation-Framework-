import pytest
from sensors.imu_interface import IMUSensor
from logger.sqlite_logger import log_result
from config import TEST_CASE_ID

sensor = IMUSensor()
sensor.initialize()

@pytest.mark.parametrize("i", range(5))  # 5 test samples
def test_sensor_readings(i):
    accel = sensor.read_accel()
    gyro = sensor.read_gyro()

    # Basic validation
    is_valid = all(-32768 <= x <= 32767 for x in (*accel, *gyro))
    log_result(TEST_CASE_ID, accel, gyro, "PASS" if is_valid else "FAIL")

    assert is_valid
