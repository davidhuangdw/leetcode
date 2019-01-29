import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/student-attendance-record-ii/


class StudentAttendanceRecordII{
  fun checkRecord(n: Int): Int {
    val md = (1e9+7).toInt()
    val dp = Array(2){ longArrayOf(1, 0, 0, 0, 0, 0) }
    for(r in 1..n){
      val pre = dp[(r-1) and 1]
      val cur = r and 1
      dp[cur][0] = pre.slice(0..2).sum() % md
      dp[cur][1] = pre[0]
      dp[cur][2] = pre[1]
      dp[cur][3] = pre.sum() % md
      dp[cur][4] = pre[3]
      dp[cur][5] = pre[4]
    }

    return (dp[n and 1].sum() % md).toInt()
  }

  @Test
  fun test1(){
    assertEquals(8, checkRecord(2))
  }
}