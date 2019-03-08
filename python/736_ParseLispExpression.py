from unittest import TestCase
# https://leetcode.com/problems/parse-lisp-expression


class ParseLispExpression(TestCase):
    def evaluate(self, expression: 'str') -> 'int':
        DIGITS = "-0123456789"
        contexts, n, i = [], len(expression), 0

        def forward():
            nonlocal i
            j = i
            while expression[i] not in ' )':
                i += 1
            word = expression[j:i]
            return word

        def parseInt(word):
            if not isinstance(word, str) or word[0] in DIGITS:
                return int(word)
            for c in reversed(contexts):
                if word in c:
                    return c[word]
            raise RuntimeError(f"not exist: {word}")

        def eval():
            nonlocal i
            first = forward()
            if first[0] != '(':
                return parseInt(first)

            operands, op = [], first[1:]
            contexts.append({})
            while i < n:
                c = expression[i]
                if c == ')':
                    i += 1
                    break
                elif c == ' ':
                    i += 1
                    continue
                elif c == '(':
                    operands.append(eval())
                else:
                    operands.append(forward())
                if op == 'let' and len(operands) > 1:
                    contexts[-1][operands.pop()] = parseInt(operands.pop())

            if op == 'let':
                res = parseInt(operands.pop())
            elif op == 'add':
                res = parseInt(operands.pop()) + parseInt(operands.pop())
            elif op == 'mult':
                res = parseInt(operands.pop()) * parseInt(operands.pop())
            else:
                assert False

            contexts.pop()
            return res

        return eval()

    # # iterative by stack: tokens & context
    # def evaluate(self, expression: 'str') -> 'int':
    #     DIGITS = "-0123456789"
    #     n, i, st = len(expression), 0, []
    #     tokens, context = [], {}
    #
    #     def forward():
    #         nonlocal i
    #         while i < n and expression[i] == ' ':
    #             i += 1
    #         if i >= n:
    #             return None
    #         j = i
    #         if expression[j] in '()':
    #             i += 1
    #             return expression[j]
    #         while i < n and expression[i] not in ' ()':
    #             i += 1
    #         word = expression[j:i]
    #         return word
    #
    #     def parseInt(word):
    #         if not isinstance(word, str) or word[0] in DIGITS:
    #             return int(word)
    #         return context[word]
    #
    #     def eval():
    #         if tokens[0] == 'let':
    #             return parseInt(tokens[-1])
    #         else:
    #             a, b = map(parseInt, tokens[-2:])
    #             return a+b if tokens[0] == 'add' else a*b
    #
    #     while True:
    #         token = forward()
    #         if not token:
    #             break
    #         if token == '(':
    #             st.append((tokens, context))
    #             tokens, context = [], dict(context)
    #         elif token == ')':
    #             token = eval()
    #             tokens, context = st.pop()
    #             tokens.append(token)
    #         else:
    #             tokens.append(token)
    #         if len(tokens) >= 3 and tokens[0] == 'let':
    #             context[tokens.pop()] = parseInt(tokens.pop())
    #     return int(tokens[0])

    def test1(self):
        self.assertEqual(3, self.evaluate("(add 1 2)"))

    def test2(self):
        self.assertEqual(15, self.evaluate("(mult 3 (add 2 3))"))

    def test3(self):
        self.assertEqual(10, self.evaluate("(let x 2 (mult x 5))"))

    def test4(self):
        self.assertEqual(14, self.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"))

    def test5(self):
        self.assertEqual(2, self.evaluate("(let x 3 x 2 x)"))

    def test6(self):
        self.assertEqual(6, self.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"))

    def test7(self):
        self.assertEqual(4, self.evaluate("(let a1 3 b2 (add a1 1) b2)"))

