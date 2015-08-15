from enum import Enum

class PoseType(Enum):
	REST = 0
	FIST = 1
	WAVE_IN = 2
	WAVE_OUT = 3
	FINGERS_SPREAD = 4
	DOUBLE_TAP = 5
	UNKNOWN = 255