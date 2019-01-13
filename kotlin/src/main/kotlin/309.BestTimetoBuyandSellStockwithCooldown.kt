import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/


class BestTimetoBuyandSellStockwithCooldown{
  data class Result(val maxBuy: Long, val maxSell: Long)

  fun maxProfit(prices: IntArray): Int {
    val MIN = Int.MIN_VALUE.toLong()
    val last = mutableListOf(Result(MIN, 0), Result(MIN, 0)) // or maintain a queue
    for((i,v) in prices.withIndex()){
      val k = i and 1
      val pre = last[k xor 1]
      val prepre = last[k]
      val maxSell = maxOf(pre.maxSell, pre.maxBuy+v)
      val maxBuy = maxOf(prepre.maxSell - v, pre.maxBuy)
      last[k] = Result(maxBuy, maxSell)
    }

    return last[(prices.size-1) and 1].maxSell.toInt()
  }

  @Test
  fun test1(){
      assertEquals(3, maxProfit(intArrayOf(1,2,3,0,2)))
  }
}