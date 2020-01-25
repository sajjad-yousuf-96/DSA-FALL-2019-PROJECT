#====================================================================================================
#The Free Edition of C# to C++ Converter limits conversion output to 100 lines per file.

#To purchase the Premium Edition, our website:
#https:#www.tangiblesoftwaresolutions.com/order/order-csharp-to-cplus.html
#====================================================================================================

import Octree.sec
Point.Point() : Point(-1)


Point.Point(a, b, c) : Point(c)


Octree.Octree()
	# to declare empty node
point = Point()


Octree.Octree(x, y, z)
	# to declare point node
point = Point(x, y, z)


Octree.Octree(x1, y1, z1, x2, y2, z2)
if x2 < x1 or y2 < y1 or z2 < z1:
        return

point = nullptr_Keyword
top_left_front = Point(x1, y1, z1)
bottom_right_back = Point(x2, y2, z2)
children.assign(8, nullptr_Keyword)
	for i in range():
                children[i] = Octree()
def insert(self, x, y, z):
	if x < top_left_front. x or x > bottom_right_back. x or y < top_left_front. y or y > bottom_right_back. y or z < top_left_front. z or z > bottom_right_back. z:
		return

	midx = (top_left_front. x + bottom_right_back. x) >> 1, midy = (top_left_front. y + bottom_right_back. y) >> 1, midz = (top_left_front. z + bottom_right_back. z) >> 1
	pos = -1
	if x <= midx:
		if y <= midy:
			if z <= midz:
				pos = TLF

			elif:
				pos = TLB


		else:
			if z <= midz:
				pos = BLF

			elif:
				pos = BLB



	else:
		if y <= midy:
			if z <= midz:
				pos = TRF

			elif:
				pos = TRB


		else:
			if z <= midz:
				pos = BRF

			eli:
				pos = BRB




	if children[pos]. point == nullptr_Keyword:
	   # if region node
		children[pos]. insert(x, y, z)
		return

	elif children[pos]. point. x == -1:
		# if empty node
		delete_Keyword children[pos]
		children[pos] = Octree(x, y, z)
		return

	else:
		x_ = children[pos]. point. x, y_ = children[pos]. point. y, z_ = children[pos]. point. z
		delete_Keyword children[pos]
		children[pos] = nullptr_Keyword
		if pos == TLF:
			children[pos] = Octree(top_left_front. x, top_left_front. y, top_left_front. z, midx, midy, midz)

		elif pos == TRF:
			children[pos] = Octree(midx + 1, top_left_front. y, top_left_front. z, bottom_right_back. x, midy, midz)

		elif pos == BRF:
			children[pos] = Octree(midx + 1, midy + 1, top_left_front. z, bottom_right_back. x, bottom_right_back. y, midz)

		elif pos == BLF:
			children[pos] = Octree(top_left_front. x, midy + 1, top_left_front. z, midx, bottom_right_back. y, midz)

		elif pos == TLB:
			children[pos] = Octree(top_left_front. x, top_left_front. y, midz + 1, midx, midy, bottom_right_back. z)

		elif pos == TRB:
			children[pos] = Octree(midx + 1, top_left_front. y, midz + 1, bottom_right_back. x, midy, bottom_right_back. z)

		elif pos == BRB:
			children[pos] = Octree(midx + 1, midy + 1, midz + 1, bottom_right_back. x, bottom_right_back. y, bottom_right_back. z)

		elif pos == BLB:
			children[pos] = Octree(top_left_front. x, midy + 1, midz + 1, midx, bottom_right_back. y, bottom_right_back. z)

		children[pos]. insert(x_, y_, z_)
		children[pos]. insert(x, y, z)



def find(self, x, y, z):
	if x < top_left_front. x or x > bottom_right_back. x or y < top_left_front. y or y > bottom_right_back. y or z < top_left_front. z or z > bottom_right_back. z:
		return 0

	midx = (top_left_front. x + bottom_right_back. x) >> 1, midy = (top_left_front. y + bottom_right_back. y) >> 1, midz = (top_left_front. z + bottom_right_back. z) >> 1
	pos = -1
	if x <= midx:
		if y <= midy:
			if z <= midz:
				pos = TLF

			elif:
				pos = TLB


		elif:
			if z <= midz:
				pos = BLF

			else:
				pos = BLB



	else:
		if y <= midy:
			if z <= midz:
				pos = TRF

			elif:
				pos = TRB


		elif:
			if z <= midz:
				pos = BRF

			elif:
				pos = BRB



	if children[pos]. point == nullptr_Keyword:
	   # if region node
		return children[pos]. find(x, y, z)


#====================================================================================================
#End of the allowed output for the Free Edition of C# to C++ Converter.

#To purchase the Premium Edition, our website:
#https:#www.tangiblesoftwaresolutions.com/order/order-csharp-to-cplus.html
#====================================================================================================
