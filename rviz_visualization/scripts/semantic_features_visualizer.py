#!/usr/bin/env python

PACKAGE = 'rviz_visualization'
NODE = 'semantic_features_visualizer_node'

import rospy
from osm_map_msgs.msg import *
from visualization_msgs.msg import MarkerArray, Marker
from rviz_visualization.marker_generator import MarkerGenerator


class SemanticFeaturesVisualizerNode(object):

    def __init__(self):
        self.semantic_features_sub = rospy.Subscriber(
            "/semantic_features_detected", SemanticMap, self._semantic_features_callback)
        self.semantic_features_markers_pub = rospy.Publisher(
            '/semantic_features_markers', MarkerArray, queue_size=10, latch=True)

    def _semantic_features_callback(self, data):
        self._visualize_semantic_features(data)

    def _visualize_semantic_features(self, data):
        marker_array = MarkerArray()
        id_count = 0
        for pillar in data.pillars:
            marker_array.markers.append(MarkerGenerator.generate_point_marker(
                self, id=id_count, frame_id='/rslidar', lifetime=3600, scale=0.1, color_rgb=[0, 0, 1.0], points=[pillar.point]))
            id_count = id_count + 1

        for wall_side in data.wall_sides:
            marker_array.markers.append(MarkerGenerator.generate_line_marker(
                self, id=id_count, frame_id='/rslidar', lifetime=3600, scale=0.1, color_rgb=[1, 1, 1], points=wall_side.corners))
            id_count = id_count + 1

        for door_side in data.door_sides:
            marker_array.markers.append(MarkerGenerator.generate_line_marker(
                self, id=id_count, frame_id='/rslidar', lifetime=3600, scale=0.1, color_rgb=[0.5, 0.5, 0.5], points=door_side.corners))
            id_count = id_count + 1

        for features in data.features:
            marker_array.markers.append(MarkerGenerator.generate_point_marker(
                self, id=id_count, frame_id='/rslidar', lifetime=3600, scale=0.1, color_rgb=[0, 1.0, 0], points=[feature.position]))
            id_count = id_count + 1

        self.semantic_features_markers_pub.publish(marker_array)


if __name__ == "__main__":
    rospy.init_node(NODE)
    map_server_node = SemanticFeaturesVisualizerNode()
    rospy.spin()
