import org.junit.Assert.assertEquals
import org.junit.Test
//https://leetcode.com/problems/lfu-cache/


class LFUCache(val capacity: Int) {
  class Node<T>(val value: T){
    var prev: Node<T>?=null
    var next: Node<T>?=null

    fun append(node: Node<T>){
      node.next = next
      next?.prev = node
      next = node
      node.prev = this
    }

    fun remove(){
      prev?.next = next
      next?.prev = prev
    }
  }

  data class Data(val key: Int, var value: Int, var freq: Int=1)
  data class FreqInfo(val freq: Int, val dataHead: Node<Data>, val dataTail: Node<Data>){
    init { dataHead.append(dataTail) }
  }

  private fun buildFreqNode(freq: Int) = Node(FreqInfo(freq, Node(Data(-1, -1)), Node(Data(-1, -1))))

  var count = 0
  val map = HashMap<Int, Node<Data>>()
  val freqMap = HashMap<Int, Node<FreqInfo>>()
  val freqHead = buildFreqNode(-1)

  fun get(key: Int): Int {
    if(!map.contains(key)) return -1
    val dataNode = map[key]!!
    val prevFreqNode = remove(dataNode)
    dataNode.value.freq ++
    insert(dataNode, prevFreqNode)
    return dataNode.value.value
  }

  fun put(key: Int, value: Int) {
    if(capacity == 0) return
    if(map.containsKey(key)){
      val node = map[key]!!
      node.value.value = value
      get(key)
    } else {
      if (count == capacity) pop()
      val node = Node(Data(key, value))
      insert(node)
    }
  }

  private fun emptyFreq(freqInfo: FreqInfo) = freqInfo.dataHead.next == freqInfo.dataTail
  private fun remove(dataNode: Node<Data>): Node<FreqInfo>{  // return prev freqNode
    dataNode.remove()
    map.remove(dataNode.value.key)
    count -= 1

    val freq = dataNode.value.freq
    val freqNode = freqMap[freq]!!
    if(emptyFreq(freqNode.value)) {
      freqNode.remove()
      freqMap.remove(freq)
      return freqNode.prev!!
    }else
      return freqNode
  }
  private fun insert(node: Node<Data>, prevFreqNode: Node<FreqInfo> = freqHead){
    assert(!map.contains(node.value.key))
    map[node.value.key] = node
    count += 1

    val freq = node.value.freq
    if(!freqMap.contains(freq))
      freqMap[freq] = buildFreqNode(freq).also{ prevFreqNode.append(it) }
    val freqNode = freqMap[freq]!!
    freqNode.value.dataHead.append(node)
  }

  private fun pop(){
    val leastFreqNode = freqHead.next!!
    val dataNode = leastFreqNode.value.dataTail.prev!!
    remove(dataNode)
  }

}

class LFUCacheTests{
  @Test
  fun test1(){
    val cache = LFUCache( 2)
    cache.put(1, 1)
    cache.put(2, 2)
    assertEquals(1, cache.get(1))
    cache.put(3, 3)
    assertEquals(-1, cache.get(2))
    assertEquals(3, cache.get(3))
    cache.put(4, 4)
    assertEquals(-1, cache.get(1))
    assertEquals(3, cache.get(3))
    assertEquals(4, cache.get(4))
  }

  @Test
  fun test2(){
    val cache = LFUCache( 3)
    cache.put(2, 2)
    cache.put(1, 1)
    assertEquals(2, cache.get(2))
    assertEquals(1, cache.get(1))
    assertEquals(2, cache.get(2))
    cache.put(3, 3)
    cache.put(4, 4)
    assertEquals(-1, cache.get(3))
    assertEquals(2, cache.get(2))
    assertEquals(1, cache.get(1))
    assertEquals(4, cache.get(4))
  }
}