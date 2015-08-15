import sys
sys.path.append('../lib/')

from device_listener import DeviceListener
from pose_type import PoseType

class PrintPoseListener(DeviceListener):
	def on_pose(self, pose):
		pose_type = PoseType(pose)
		print(pose_type.name)
