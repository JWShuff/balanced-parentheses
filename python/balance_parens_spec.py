import unittest
from balance_parens import balance_parens

class TestParens(unittest.TestCase):

    """
    When you call Balanced Parens you get a string back
    """
    def test_returns_a_string(self):
        self.assertTrue(type(balance_parens("test")) == str)

    """
    When you call balanced parens with "" you get "" back:
    """
    def test_returns_a_blank(self):
        self.assertTrue(balance_parens("") == "")
    """
    When you call balanced parens, you get correctly balanced strings
    """
    def test_function_output_accuracy(self):
        self.assertTrue(balance_parens("abc(d)e(fgh))(i)j)k") == "abc(d)e(fgh)(i)jk")
        self.assertTrue(balance_parens("abc((d)e(fgh)(i)j(k") == "abc(d)e(fgh)(i)jk")

        self.assertTrue(balance_parens("()") == "()")
        self.assertTrue(balance_parens("a(b)c)") == "a(b)c")
        self.assertTrue(balance_parens("(a)(bdd)c)")  == "(a)(bdd)c")
        self.assertTrue(balance_parens("a(b)(c)())")  == "a(b)(c)()")
        self.assertTrue(balance_parens(")(")  == "")
        self.assertTrue(balance_parens("(((((")  == "")
        self.assertTrue(balance_parens(")(())(")  == "(())")
        self.assertTrue(balance_parens("(()()(")  == "()()")
        self.assertTrue(balance_parens(")())(()()(")  == "()()()")
    
    """
    Challenge Questions
    """
    def test_function_challenge(self):
        self.assertTrue(balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p") == "abc(d)(ef(g(h))ij)klm()op")
    def test_function_additional(self):
        self.assertTrue(balance_parens("(((((asdfjkl;))(())(((((((") == "((asdfjkl;))(())")

if __name__ == '__main__':
    unittest.main()
