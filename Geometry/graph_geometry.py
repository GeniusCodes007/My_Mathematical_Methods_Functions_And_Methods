import math


class GraphGeometry:
    basic_linear_graph = "y = mx + c"

    def __init__(self, x_1, y_1 ,x_2, y_2):
        self.coordinate_1 = [x_1, y_1]
        self.coordinate_2 = [x_2, y_2]
        self.x1 = int(self.coordinate_1[0])
        self.x2 = int(self.coordinate_2[0])
        self.y1 = int(self.coordinate_1[1])
        self.y2 = int(self.coordinate_2[1])
        self.delta_x = self.x2 - self.x1
        self.delta_y = self.y2 - self.y1
        self.slope = self.delta_y / self.delta_x
        self.gradient = self.delta_y / self.delta_x 
        self.y_zero_intercept = self.y1- ((self.x1 * self.delta_y )/ self.delta_x)
        self.x_zero_intercept = -(self.y_zero_intercept / self.gradient)

    def midpoint_coordinate(self):
        mid_p_x = int(int(self.coordinate_1[0]) + int(self.coordinate_2[0])) / 2
        mid_p_y = int(int(self.coordinate_1[1]) + int(self.coordinate_2[1])) / 2
        mid_point_coord = [mid_p_x, mid_p_y]
        return mid_point_coord
    
    def distance_between_two_points(self):
        dis_x = int(int(self.coordinate_2[0]) - int(self.coordinate_1[0]))
        dis_y = int(int(self.coordinate_2[1]) - int(self.coordinate_1[1]))
        dis_btw_two_points = ((dis_x**2) + (dis_y**2))**(1/2)
        return dis_btw_two_points
    
    def angle_of_slope(self):
        angle = math.atan(self.slope)
        angle_in_degrees = math.degrees(angle)
        if angle_in_degrees < 0:
            new = abs(angle_in_degrees) + 90
            return new
        else:
            return angle_in_degrees
    def equation_of_straight_line(self):
        y_part = "y "
        x_part = str(self.gradient) + "x + " + str(self.y1- ((self.x1 * self.delta_y )/ self.delta_x))
        equation = y_part + " = " + x_part
        return equation

line = GraphGeometry(1, -1, -2, -13)
print(line.basic_linear_graph)
print(line.midpoint_coordinate())
print(line.distance_between_two_points())
print(line.gradient)
print(line.slope)
print(line.delta_x)
print(line.delta_y)
print(line.angle_of_slope())
print(line.equation_of_straight_line())
print(line.y_zero_intercept)
print(line.x_zero_intercept)