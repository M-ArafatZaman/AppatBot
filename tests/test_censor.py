from censor.is_inappropriate import is_inappropriate
from censor.sanitizer import sanitize_text
import unittest


# Test Case
class Test(unittest.TestCase):

    def test_is_inappropriate(self):
        '''
        Test is_inappropriate()
        '''
        sentence_good = "A good sentence"
        sentence_bad = "A dick sentence"
        sentence_edge = "A dicksentence"

        self.assertFalse(is_inappropriate(sentence_good), "Good sentence returned true")
        self.assertTrue(is_inappropriate(sentence_bad), "Bad sentence returned false")
        self.assertFalse(is_inappropriate(sentence_edge), "Edge sentence returned true")

    
    def test_sanitize_text(self):
        '''
        Test sanitize_text
        '''
        sentence1 = "A good sentence"
        sentence2 = "A dick sentence"
        sentence3 = "A dicksentence"

        self.assertEqual(sanitize_text(sentence1), sentence1, "Good sentence censored")
        self.assertEqual(sanitize_text(sentence2), "A [CENSORED] sentence", "Bad sentence censored")
        self.assertEqual(sanitize_text(sentence3), sentence3, "Edge sentence censored")


if __name__ == "__main__":
    unittest.main()