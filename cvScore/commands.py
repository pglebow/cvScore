import click
from pathlib import Path
import cvScore.__main__ as cvScore


@click.command(help="Score the CVs using the provided keywords")
@click.argument("file_directory", type=click.Path(file_okay=False, dir_okay=True, writable=False, path_type=Path))
@click.argument("keyword_file", type=click.Path(file_okay=True, dir_okay=False, writable=False, path_type=Path))
def scoreCV(file_directory, keyword_file: Path):
    files = set()

    dir = Path(file_directory)
    keywords = Path(keyword_file)
    for file in dir.iterdir():
        if file.is_file():
            if file.suffix == '.pdf' or file.suffix == '.docx':
                files.add(file)

    retVal = cvScore.process_files(files, keywords.absolute())

    return retVal