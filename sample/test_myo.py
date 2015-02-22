import sys
sys.path.append('../lib/')

from myo import Myo
from print_pose_listener import PrintPoseListener

def main():
    print('Start Myo for Linux')

    listener = PrintPoseListener()
    myo = Myo()

    try:
        myo.connect()
        myo.add_listener(listener)

        while True:
            myo.run()

    except KeyboardInterrupt:
        pass
    except ValueError as ex:
        print(ex)
    finally:
        myo.safely_disconnect()
        print('Finished.')

if __name__ == '__main__':
    main()