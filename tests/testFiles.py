import unittest
import cvScore.__main__ as cvScore
from pathlib import Path

class TestFiles(unittest.TestCase):
    def test_files(self):

        files = set()

        base_path = Path(__file__).parent
        file_path = (base_path / "../data/testDoc1.pdf").resolve()
        files.add(file_path)

        file_path = (base_path / "../data/testDoc1.docx").resolve()
        files.add(file_path)

        file_path = (base_path / "../data/testDoc2.pdf").resolve()
        files.add(file_path)

        file_path = (base_path / "../data/testDoc2.docx").resolve()
        files.add(file_path)

        keywords_path = (base_path / "../data/keywords.txt").resolve()

        self.assertEqual(len(files), 4)

        retVal = cvScore.process_files(files, keywords_path.absolute())

        self.assertEqual(4, len(retVal))

        for r in retVal:
            print(r)


if __name__ == '__main__':
    unittest.main()
