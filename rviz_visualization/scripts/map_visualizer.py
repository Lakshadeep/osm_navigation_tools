#!/usr/bin/env python

PACKAGE = 'rviz_visualization'
NODE = 'map_visualizer_node'


from osm_map_msgs.msg import *
import rospy
from visualization_msgs.msg import MarkerArray, Marker
from rviz_visualization.marker_generator import  MarkerGenerator

class MapVisualizerNode(object):

    def __init__(self):
        self.geometric_map_sub = rospy.Subscriber("/geometric_map", GeometricMap, self._geometric_map_callback)
        self.geometric_map_sub = rospy.Subscriber("/semantic_map", SemanticMap, self._semantic_map_callback)
        self.geometric_map_markers_pub = rospy.Publisher('/geometric_map_markers', MarkerArray, queue_size=10, latch=True)
        self.semantic_map_markers_pub = rospy.Publisher('/semantic_map_markers', MarkerArray, queue_size=10, latch=True)

    def _geometric_map_callback(self, data):
        self._visualize_geometric_map(data)

    def _visualize_geometric_map(self, data):
        marker_array = MarkerArray()
        id_count = 0
        for pillar in data.pillars:
            marker_array.markers.append(MarkerGenerator.generate_polygon_marker(self, id=id_count, frame_id='/map', lifetime=3600, scale=0.1, color_rgb=[0,0,1],points=pillar.points))
            id_count = id_count + 1

        for wall in data.walls:
            marker_array.markers.append(MarkerGenerator.generate_polygon_marker(self, id=id_count, frame_id='/map', lifetime=3600, scale=0.1, color_rgb=[0,0,1],points=wall.points))
            id_count = id_count + 1

        for door in data.doors:
            marker_array.markers.append(MarkerGenerator.generate_polygon_marker(self, id=id_count, frame_id='/map', lifetime=3600, scale=0.1, color_rgb=[1,0,0],points=door.points))
            id_count = id_count + 1

        self.geometric_map_markers_pub.publish(marker_array)

    def _semantic_map_callback(self, data):
        self._visualize_semantic_map(data)

    def _visualize_semantic_map(self, data):
        marker_array = MarkerArray()
        id_count = 0
        for pillar in data.pillars:
            marker_array.markers.append(MarkerGenerator.generate_polygon_marker(self, id=id_count, frame_id='/map', lifetime=3600, scale=0.1, color_rgb=[0,0,1],points=pillar.shape.points))
            id_count = id_count + 1

        for wall_side in data.wall_sides:
            marker_array.markers.append(MarkerGenerator.generate_line_marker(self, id=id_count, frame_id='/map', lifetime=3600, scale=0.1, color_rgb=[1,1,1],points=wall_side.corners))
            id_count = id_count + 1

        for door_side in data.door_sides:
            marker_array.markers.append(MarkerGenerator.generate_line_marker(self, id=id_count, frame_id='/map', lifetime=3600, scale=0.1, color_rgb=[0.5,0.5,0.5],points=door_side.corners))
            id_count = id_count + 1

        for features in data.features:
            marker_array.markers.append(MarkerGenerator.generate_point_marker(self, id=id_count, frame_id='/map', lifetime=3600, scale=0.1, color_rgb=[0,1.0,0],points=feature.position))
            id_count = id_count + 1

        self.semantic_map_markers_pub.publish(marker_array)



if __name__ == "__main__":
    rospy.init_node(NODE)
    map_server_node = MapVisualizerNode()
    rospy.spin()
