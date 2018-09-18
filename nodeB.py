#!/usr/bin/env python
## Simple talker demo that listens to std_msgs/Strings published 
## to the 'mann' topic

import rospy
from std_msgs.msg import Int16
global number
global data
data=Int16()
number = Int16()

def callback(data):

	rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
	number.data =data.data
	number.data = ((number.data)/0.15)

def nodeB():
		
	rospy.init_node('nodeB', anonymous=True)
	rospy.Subscriber('mann', Int16, callback)
	rate = rospy.Rate(0.5)
	

	pub = rospy.Publisher('/kthfs/result', Int16, queue_size=10)

	while not rospy.is_shutdown():			

		pub.publish(number)
		rospy.loginfo(number)
		rate.sleep()	

if __name__ == '__main__':
    try:
    	nodeB()
    except rospy.ROSInterruptException:
        pass
