#!/usr/bin/env python
## Simple talker demo that published std_msgs/Strings messages
## to the 'mann' topic

import rospy
from std_msgs.msg import Int16
global add
def nodeA():
	pub = rospy.Publisher('mann', Int16, queue_size=10)
	rospy.init_node('nodeA', anonymous=True)
	rate = rospy.Rate(0.5)
	data=Int16()
	data.data=5
	add=Int16()
	add.data=4
	while not rospy.is_shutdown():
		rospy.loginfo(data)
		pub.publish(data)
		data.data = data.data + add.data
		rate.sleep()			

if __name__ == '__main__':
    try:
        nodeA()
    except rospy.ROSInterruptException:
        pass
