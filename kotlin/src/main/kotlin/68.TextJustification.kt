import org.junit.Assert.assertEquals
import org.junit.Test
// https://leetcode.com/problems/text-justification


class TextJustification {
  fun buildLine(words: List<String>, maxWidth: Int, lastLine: Boolean): String{
    var (n, rem) = words.size to maxWidth - words.map{it.length}.sum()
    if(lastLine || n == 1)
      return words.joinToString(" ") + " ".repeat(rem - (n-1))

    val k = rem - rem/(n-1)*(n-1)
    val (shorter, longer) = " ".repeat(rem/(n-1)) to " ".repeat((rem+n-2)/(n-1))
    return words.slice(0..k).joinToString(longer) +
        words.slice(k+1 until n).joinToString(shorter, prefix=shorter)
  }
  fun fullJustify(words: Array<String>, maxWidth: Int): List<String> {
    var (i, n) = 0 to words.size
    val res = mutableListOf<String>()
    while(i < n){
      var (j, wid) = i+1 to words[i].length
      while(j < n && wid + 1 + words[j].length <= maxWidth){
        wid += 1 + words[j].length
        j += 1
      }
      res.add(buildLine(words.slice(i until j), maxWidth, j==n))
      i = j
    }
    return res
  }

  @Test
  fun test1(){
    assertEquals(listOf(
        "This    is    an",
        "example  of text",
        "justification.  "
    ), fullJustify(
        arrayOf("This", "is", "an", "example", "of", "text", "justification."),
        16
    ))
  }

  @Test
  fun test2(){
    assertEquals(listOf(
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ), fullJustify(
        arrayOf("What","must","be","acknowledgment","shall","be"),
        16
    ))
  }

}

