#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
import gaze_msgs.msg
import explore_msgs.msg


class NodeExample():

    # Initialization happens when the object is created:
    def __init__(self):

        # Set up a publisher called "publish", for an int
        #self.pub = rospy.Publisher(
        #        "pepper/gaze",
        #        gaze_msgs.msg.face_detection,
        #        queue_size=1)

        # Set up a subscriber called "subscribe" as a String
        #self.sub = rospy.Subscriber(
        #        "subscribe",
        #        String,
        #        self.callback)


        self.pub = rospy.Publisher(
                "pepper/explore_msgs",
                explore_msgs.msg.exploreNav,
                queue_size=1)

        self.sub = rospy.Subscriber(
                "subscribe",
                String,
                self.callback)

        rate = rospy.Rate(2)
        #Wait until the connections are stablished
        while self.pub.get_num_connections() == 0:
            rate.sleep() #sleep for 500ms

#    def example_function(self):

        # val = gaze_msgs.msg.face_detection()
    #    rate = rospy.Rate(1) # update rate of 1hz
        # val.state = True
        # val.targetName = "Face"
        # val.faceWidth = 0.1
        # while not rospy.is_shutdown():

        #rospy.loginfo("publishing value: " + str(self.val))
        # publish the value val to the topic
        #self.pub.publish(self.val)

        # rate.sleep()
        # self.pub.publish(self.val)

                            # sleep the amount of time needed to achieve the 1hz rate set above
            # rate.sleep()


    def explore_function(self):
        val = explore_msgs.msg.exploreNav()
        rate = rospy.Rate(1)
        val.state = True
        val.radius = 2

        rospy.loginfo("Publishing value: " + str(val))
        self.pub.publish(val)
        rate.sleep()

    def callback(self, data):

        # Print the string stored in the ROS String msg:
        rospy.loginfo("I heard: " + data.data)



if __name__ == '__main__':
    # initialization of the ros node
    rospy.init_node("nodeexample", anonymous=True)

    n = NodeExample()
    NodeExample.val = gaze_msgs.msg.face_detection()
    #Change to True or False depending on activation pr desactivation preference
    NodeExample.val.state = True
    NodeExample.val.targetName = "Face"
    NodeExample.val.faceWidth = 0.1
    #n.example_function()
    n.explore_function()


    rospy.spin()
