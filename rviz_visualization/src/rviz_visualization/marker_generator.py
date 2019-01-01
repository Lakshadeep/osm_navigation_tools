from osm_map_msgs.msg import *
import rospy
import geometry_msgs.msg
from visualization_msgs.msg import Marker

class MarkerGenerator(object):

    @staticmethod
    def generate_polygon_marker(self, id=0, frame_id='', lifetime=600, scale=0.1, color_rgb=[1,0,0],points=[]):
        marker = Marker()
        marker.id = id
        marker.header.frame_id = frame_id
        marker.header.stamp = rospy.get_rostime()
        marker.type = marker.LINE_LIST
        marker.action = marker.ADD
        marker.lifetime.secs = lifetime
        marker.scale.x = scale
        marker.color.a = 1.0
        marker.color.r = color_rgb[0]
        marker.color.g = color_rgb[1]
        marker.color.b = color_rgb[2]
        marker.points = []
        for i, point in enumerate(points):
            if i != 0:
                marker.points.append(points[i-1])
                marker.points.append(point)
        return marker

    @staticmethod
    def generate_line_marker(self, id=0, frame_id='', lifetime=600, scale=0.1, color_rgb=[1,0,0],points=[]):
        marker = Marker()
        marker.id = id
        marker.header.frame_id = frame_id
        marker.header.stamp = rospy.get_rostime()
        marker.type = marker.LINE_STRIP
        marker.action = marker.ADD
        marker.lifetime.secs = lifetime
        marker.scale.x = scale
        marker.color.a = 1.0
        marker.color.r = color_rgb[0]
        marker.color.g = color_rgb[1]
        marker.color.b = color_rgb[2]
        marker.points = []
        for i, point in enumerate(points):
            if i != 0:
                marker.points.append(points[i-1])
                marker.points.append(point)
        return marker

    @staticmethod
    def generate_point_marker(self, id=0, frame_id='', lifetime=600, scale=0.1, color_rgb=[1,0,0],points=[]):
        marker = Marker()
        marker.id = id
        marker.header.frame_id = frame_id
        marker.header.stamp = rospy.get_rostime()
        marker.type = marker.POINTS
        marker.action = marker.ADD
        marker.lifetime.secs = lifetime
        marker.scale.x = scale
        marker.scale.y = scale
        marker.color.a = 1.0
        marker.color.r = color_rgb[0]
        marker.color.g = color_rgb[1]
        marker.color.b = color_rgb[2]
        marker.points = points
        return marker
        
