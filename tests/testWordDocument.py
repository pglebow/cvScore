import unittest
import traceback
import cvScore.__main__ as cvScore

from pathlib import Path

class TestWordDocument(unittest.TestCase):
    def test_something(self):
        try:
            base_path = Path(__file__).parent
            file_path = (base_path / "../data/testDoc2.docx").resolve()
            keywordFile = (base_path / "../data/keywords.txt").resolve()
            retVal = cvScore.process_word_document(file_path, cvScore.load_keywords(keywordFile.absolute()))

            for r in retVal:
                print(r)
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            self.fail(self)


if __name__ == '__main__':
    unittest.main()
