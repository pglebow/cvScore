import unittest
from pathlib import Path

from click.testing import CliRunner
from cvScore import commands
import traceback

class TestCLI(unittest.TestCase):
    def test_cli(self):
        try:
            runner = CliRunner()
            base_path = Path(__file__).parent

            resumesPath = (base_path / "../data").resolve()
            dir_URL = Path(resumesPath)

            keywords_path = (base_path / "../data/keywords.txt").resolve()
            keywords_file = Path(keywords_path)
            args = [str(dir_URL.absolute()), str(keywords_file.absolute())]

            result = runner.invoke(commands.scoreCV, args, catch_exceptions=False)
            self.assertEqual(result.exit_code, 0)

        except Exception as e:
            print(traceback.format_exc())
            self.fail()


if __name__ == '__main__':
    unittest.main()
