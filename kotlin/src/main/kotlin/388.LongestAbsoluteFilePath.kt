import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/longest-absolute-file-path/


class LongestAbsoluteFilePath{
  fun lengthLongestPath(input: String): Int {
    val sums = mapOf(0 to 0).toMutableMap()
    var max = 0
    for(line in input.split("\n")){
      val words = line.split("\t")
      val k = words.size - 1
      val name = words.last()
      sums[k+1] = sums[k]!! + name.length + 1
      if(name.contains('.'))
        max = maxOf(max, sums[k+1]!!-1)
    }
    return max
  }

  @Test
  fun test1(){
    assertEquals(32, lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
  }

  @Test
  fun test2(){
    assertEquals(9, lengthLongestPath("dir\n file.txt"))
  }
}