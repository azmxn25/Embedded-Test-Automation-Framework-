import random
import time

class IMUSensor:
    def __init__(self):
        pass

    def initialize(self):
        time.sleep(0.1)  # Simulate sensor init delay

    def read_accel(self):
        return (
            random.randint(-16000, 16000),
            random.randint(-16000, 16000),
            random.randint(-16000, 16000)
        )

    def read_gyro(self):
        return (
            random.randint(-30000, 30000),
            random.randint(-30000, 30000),
            random.randint(-30000, 30000)
        )
