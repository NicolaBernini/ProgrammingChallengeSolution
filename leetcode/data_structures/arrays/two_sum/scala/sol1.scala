import scala.collection.mutable.Map
object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        var m: Map[Int, Int] = Map()
        for ((e,i) <- nums.view.zipWithIndex) {
                if (m.contains(target-e)) {
                    return Array(i, m(target-e))
                }
            m(e) = i                            
        }
        // Should never happen 
        return Array(0,0)
    }
}
