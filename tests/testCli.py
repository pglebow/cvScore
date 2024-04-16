import unittest
from pathlib import Path

from click.testing import CliRunner
from cvScore import commands

class MyTestCase(unittest.TestCase):
    def test_cli(self):
        runner = CliRunner()
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/testDoc1.pdf").resolve()
        keywords_path = (base_path / "../data/keywords.txt").resolve()
        result = runner.invoke(commands.scoreCV, file_path.absolute(), keywords_path.absolute())


if __name__ == '__main__':
    unittest.main()
