#pragma once

#include <vector>
#include <iostream>

'''
 * Code for an octree that demonstrates insertion and search
 '''
#include <iostream>
#include <vector>

#define TLF 0 # top left front
#define TRF 1 # top right front
#define BRF 2 # bottom right front
#define BLF 3 # bottom left front
#define TLB 4 # top left back
#define TRB 5 # top right back
#define BRB 6 # bottom right back
#define BLB 7 # bottom left back

class Point():
        def __init__(self):
                self.__x=0
                self.__y=0
                self.__z=0
class Octree():
	# if point == NULL, is regional.
	# if point == (-1, -1, -1), is empty.
	Point * point

	Point * top_left_front, bottom_right_back; # represents the space.
	std.vector<Octree*> children

	Octree()

	Octree(int x, y, z)

	Octree(int x1, y1, z1, x2, y2, z2)

	Octree.insert(int x, y, z)

	bool find(int x, y, z)
def main(self):
