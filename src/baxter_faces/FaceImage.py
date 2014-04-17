import roslib
roslib.load_manifest('baxter_faces')
import rospy

import cv
import cv_bridge
import sensor_msgs.msg


class FaceImage(object):
    def __init__(self):
        self.images = {
            'indifferent': self._get_image('gerty_indifferent.png'),
            'happy': self._get_image('gerty_happy.png'),
            'smile': self._get_image('gerty_goodnews.png'),
            'excited': self._get_image('gerty_excited.png'),
            'winking': self._get_image('gerty_winking.png'),
            'surprised': self._get_image('gerty_surprised.png'),
            'thinking_left': self._get_image('gerty_thinking_left.png'),
            'thinking_right': self._get_image('gerty_thinking_right.png'),
            'confused': self._get_image('gerty_confused.png'),
            'unhappy': self._get_image('gerty_unhappy.png'),
            'sad': self._get_image('gerty_sad.png'),
            'dead': self._get_image('gerty_dead.png'),
            'big_lemongrab': self._get_image('big_lemongrab.png'),
        }
        self.current_image = ''
        self.pub = rospy.Publisher(
            '/robot/xdisplay', sensor_msgs.msg.Image, latch=True)
        self.set_image('indifferent')

    def _get_image(self, path):
        img = cv.LoadImage(
            roslib.packages.get_pkg_dir('baxter_faces') + '/img/' + path)
        return cv_bridge.CvBridge().cv_to_imgmsg(img)

    def set_image(self, img_name):
        if self.current_image != img_name:
            self.current_image = img_name
            rospy.logdebug("Setting Head Image: %s" % img_name)
            self.pub.publish(self.images[img_name])
