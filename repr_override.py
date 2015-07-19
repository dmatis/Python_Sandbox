class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    #defines how object is represented when 'print' is called
    def __repr__(self):
        return "(%d, %d, %d)" %(self.x,self.y,self.z)

my_point = Point3D(1,2,3)
print my_point