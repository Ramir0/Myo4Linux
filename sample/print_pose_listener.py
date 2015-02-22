import sys
sys.path.append('../lib/')

from device_listener import DeviceListener
from pose_type import PoseType

class PrintPoseListener(DeviceListener):
	def on_pose(self, pose):
		if pose == PoseType.REST:
			print('REST')
		elif pose == PoseType.FIST:
			print('FIST')
		elif pose == PoseType.WAVE_IN:
			print('WAVE_IN')
		elif pose == PoseType.WAVE_OUT:
			print('WAVE_OUT')
		elif pose == PoseType.FINGERS_SPREAD:
			print('FINGERS_SPREAD')
		elif pose == PoseType.DOUBLE_TAP:
			print('DOUBLE_TAP')
		else:
			print('UNKNOWN')