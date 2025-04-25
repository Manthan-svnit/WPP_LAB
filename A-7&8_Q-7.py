import math

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_with_x_axis(self):
        
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot_product(self, other):
       
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        
        return self.x * other.y - self.y * other.x

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


class Vector3D(Vector2D):
   

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
       
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def distance(self, other):
        
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def dot_product(self, other):
        
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        
        cx = self.y * other.z - self.z * other.y
        cy = self.z * other.x - self.x * other.z
        cz = self.x * other.y - self.y * other.x
        return Vector3D(cx, cy, cz)

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"


if __name__ == "__main__":
    print("🟢 2D Vector Operations:")
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print(f"Vector 1: {v1}")
    print(f"Vector 2: {v2}")
    print(f"📌 Magnitude of v1: {v1.magnitude()}")
    print(f"📌 Angle of v1 with X-axis: {v1.angle_with_x_axis()} degrees")
    print(f"📌 Distance between v1 and v2: {v1.distance(v2)}")
    print(f"📌 Dot product of v1 and v2: {v1.dot_product(v2)}")
    print(f"📌 Cross product of v1 and v2: {v1.cross_product(v2)}")

    print("\n🟢 3D Vector Operations:")
    v3 = Vector3D(3, 4, 5)
    v4 = Vector3D(1, 2, 3)

    print(f"Vector 3: {v3}")
    print(f"Vector 4: {v4}")
    print(f"📌 Magnitude of v3: {v3.magnitude()}")
    print(f"📌 Distance between v3 and v4: {v3.distance(v4)}")
    print(f"📌 Dot product of v3 and v4: {v3.dot_product(v4)}")
    print(f"📌 Cross product of v3 and v4: {v3.cross_product(v4)}")
