import unittest
import cvScore.__main__ as cvScore

from pathlib import Path


class TestFileType(unittest.TestCase):
    def test_pdf(self):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/testDoc1.pdf").resolve()
        self.assertEqual(cvScore.get_file_type(file_path.absolute()), "application/pdf")
        self.assertNotEqual(cvScore.get_file_type(file_path.absolute()), "application/xml")

    def test_docx(self):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/testDoc1.docx").resolve()
        self.assertEqual(cvScore.get_file_type(file_path.absolute()), "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        self.assertNotEqual(cvScore.get_file_type(file_path.absolute()), "application/pdf")


if __name__ == '__main__':
    unittest.main()
