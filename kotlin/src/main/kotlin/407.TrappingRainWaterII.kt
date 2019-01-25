import org.junit.Assert.assertEquals
import org.junit.Test
import java.util.*

//https://leetcode.com/problems/trapping-rain-water-ii/


class TrappingRainWaterII{
  fun trapRainWater(heightMap: Array<IntArray>): Int {
    if(heightMap.isEmpty()) return 0
    val (n, m) = heightMap.size to heightMap[0].size
    val edges = PriorityQueue<Pair<Int, Int>>(compareBy{ heightMap[it.first][it.second]})
    val done = HashSet<Pair<Int, Int>>()
    for(i in 0 until n)
      for(j in 0 until m)
        if(i==0 || i==n-1 || j==0 || j==m-1) {
          edges.add(i to j)
          done.add(i to j)
        }

    var ret = 0
    while(edges.isNotEmpty()){
      val (i,j) = edges.poll()
      for((ni,nj) in listOf(i to j-1, i to j+1, i-1 to j, i+1 to j)){
        if(ni<0 || ni>=n || nj<0 || nj>=m || ni to nj in done)
          continue
        ret += maxOf(0, heightMap[i][j] - heightMap[ni][nj])
        heightMap[ni][nj] = maxOf(heightMap[ni][nj], heightMap[i][j])
        edges.add(ni to nj)
        done.add(ni to nj)
      }
    }
    return ret
  }

  @Test
  fun test1(){
    assertEquals(14, trapRainWater(arrayOf(
        intArrayOf(12,13,1,12),
        intArrayOf(13,4,13,12),
        intArrayOf(13,8,10,12),
        intArrayOf(12,13,12,12),
        intArrayOf(13,13,13,13)
    )))
  }
}