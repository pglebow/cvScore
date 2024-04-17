import unittest
import cvScore.__main__ as cvScore
from pathlib import Path
import os

class TestGroupOfFiles(unittest.TestCase):
    def test_something(self):
        files = set()
        base_path = Path(__file__).parent
        keywords_path = (base_path / "../data/keywords.txt").resolve()
        resumesPath = (base_path / "../data").resolve()

        dir = Path(resumesPath)

        for file in dir.iterdir():
            if file.is_file():
                if file.suffix == '.pdf' or file.suffix == '.docx':
                    files.add(file)

        retVal = cvScore.process_files(files, keywords_path.absolute())

        self.assertTrue(len(retVal) > 0)

        for r in retVal:
            print(r)




if __name__ == '__main__':
    unittest.main()
