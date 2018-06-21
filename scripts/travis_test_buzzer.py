#!/usr/bin/env python

import rospy, unittest, rostest
  3 import rosnode
  4 import time
  5 from std_msgs.msg import UInt16

class BuzzerTest(unittest.TestCase):
    def test_node_exit(self):
        nodes = rosnode.get_node_names()
        self.assertIn('/buzzer',nodes, "node does not exist")

    def test_put_value(self):
        pub = rospy.publisher('/buzzer', UInt16)
        for i in range(10):
        pub.publish(1234)
        time.sleep(0.1)

        with open("/dev/rtbuzzer0","r") as f:
        data = f.readline()
        self.assertEqual(data,"1234\n","value does not written to buzzer0")

if __name__ == '__main__':
    time.sleep(3)
    rospy.init_node('travis_test_buzzer')
    rostest.rosrun('pimouse_ros','travis_test_buzzer',BuzzerTest)

