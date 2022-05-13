import time

from robomaster import robot, led
import cv2


def play_music():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_robot.play_audio(filename="demo.wav").wait_for_completed()
    ep_robot.close()


def test_wheel():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_chassis = ep_robot.chassis
    x_val = 0.5
    y_val = 0.6
    z_val = 90
    ep_chassis.move(x=x_val, y=0, z=0, xy_speed=0.7).wait_for_completed()
    ep_chassis.move(x=-x_val, y=0, z=0, xy_speed=0.7).wait_for_completed()
    ep_chassis.move(x=0, y=-y_val, z=0, xy_speed=0.7).wait_for_completed()
    ep_chassis.move(x=0, y=y_val, z=0, xy_speed=0.7).wait_for_completed()
    ep_chassis.move(x=0, y=0, z=z_val, z_speed=45).wait_for_completed()
    ep_chassis.move(x=0, y=0, z=-z_val, z_speed=45).wait_for_completed()
    ep_robot.close()


def test_led():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_led = ep_robot.led
    bright = 1
    for i in range(0, 8):
        ep_led.set_led(comp=led.COMP_ALL, r=bright << i, g=bright << i, b=bright << i, effect=led.EFFECT_ON)
        time.sleep(1)
        print("brightness: {0}".format(bright << i))
    ep_robot.close()


def move_to(x, y, z):
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")
    ep_chassis = ep_robot.chassis
    ep_chassis.move(x=x, y=0, z=0, xy_speed=1).wait_for_completed()
    ep_chassis.move(x=0, y=y, z=0, xy_speed=1).wait_for_completed()
    ep_chassis.move(x=0, y=0, z=z, z_speed=200).wait_for_completed()
    ep_robot.close()


def test_camera():
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="ap")

    ep_camera = ep_robot.camera
    ep_camera.start_video_stream(display=False)
    for i in range(200):
        img = ep_camera.read_cv2_image()
        cv2.imshow("Robot", img)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
    ep_camera.stop_video_stream()
    ep_robot.close()

def main():
    while True:
        print("-------------------- Test SDK Robomaster --------------------")
        print(
            "Choose:\n1. Play sound\n2. Movement test\n3. Led test\n4. Move to  "
            "\n5. Camera test\n0. Close")
        x = int(input("Your choose: "))

        if x == 1:
            try:
                play_music()
            except Exception as ex:
                print("Error")
            finally:
                print("Completed")
        if x == 2:
            try:
                test_wheel()
            except Exception as ex:
                print("Error")
            finally:
                print("Completed")
        if x == 3:
            try:
                test_led()
            except Exception as ex:
                print("Error")
            finally:
                print("Completed")
        if x == 4:
            try:
                x_wheel = int(input("Forward: "))
                y_wheel = int(input("Left(for right use minus): "))
                z_wheel = int(input("Rotate: "))
                move_to(x_wheel, y_wheel, z_wheel)
            except Exception as ex:
                print("Error")
            finally:
                print("Completed")
        if x == 5:
            try:
                test_camera()
            except Exception as ex:
                print("Error")
            finally:
                print("Completed")
        if x == 0:
            break


if __name__ == '__main__':
    main()
