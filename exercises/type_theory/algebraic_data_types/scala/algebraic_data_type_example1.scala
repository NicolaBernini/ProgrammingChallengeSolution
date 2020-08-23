// Here a point is an abstraction which can be Either (summing types) a Point2D or a Point3D
sealed trait Point
case class Point2D(x: Double, y: Double) extends Point {
  def +(that: Point2D) = Point2D(this.x + that.x, this.y + that.y)
  def *(that: Double) : Point2D = Point2D(this.x * that, this.y * that)
  def *(that: Point2D) : Double = this.x * that.x + this.y * that.y
  def unary_-(): Point2D = Point2D(-this.x, -this.y)
  def -(that: Point2D): Point2D = this + (that*(-1))  
}

case class Point3D(x: Double, y: Double, z: Double) extends Point {
  def +(that: Point3D) = Point3D(this.x + that.x, this.y + that.y, this.z + that.z)
  def *(that: Double) : Point3D = Point3D(this.x * that, this.y * that, this.z * that)
  def *(that: Point3D) : Double = this.x * that.x + this.y * that.y + this.z * that.z 
  def unary_-(): Point3D = Point3D(-this.x, -this.y, -this.z)
  def -(that: Point3D): Point3D = this + (that*(-1))
}

def dist(a: Point, b: Point) = {
  (a,b) match {
    case (a:Point2D, b:Point2D) => {
      val p = a-b
      math.sqrt(p*p)
    }
    case (a:Point3D, b:Point3D) => {
      val p=a-b
      math.sqrt(p*p)
    } 
    case _ => 
  }
}

class MyDouble(val x:Double) {
  def *(p: Point) = {
    p match {
      case (p:Point2D) => p*x
      case (p:Point3D) => p*x
    }
  }
}

implicit def d2bd(x: Double) = new MyDouble(x)


print(3*Point2D(1,2)+"\n")
print(Point2D(1,2) - Point2D(3,5)+"\n")
print(dist(Point2D(1,2), Point2D(3,5))+"\n")




