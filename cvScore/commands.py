import click
from pathlib import Path
import cvScore.__main__ as cvScore


@click.group()
def main():
    pass

@main.command()
@click.argument("cvDir", type=click.Path(file_okay=False, dir_okay=True, writable=False, path_type=Path))
@click.argument("keywordFile", type=click.Path(file_okay=True, dir_okay=False, writable=False, path_type=Path))
def score(cvdir, keywordfile):
    """Score a set of resumes against a set of keywords.
        The resumes must be in PDF or DOCX format.
        The keywords file must have one keyword per line.

        \b
        Example:
            score data/resumes keywords.txt
        """
    files = set()

    dir = Path(cvdir)
    keywords = Path(keywordfile)
    for file in dir.iterdir():
        if file.is_file():
            if file.suffix == '.pdf' or file.suffix == '.docx':
                files.add(file)

    retVal = cvScore.process_files(files, keywords.absolute())

    for item in retVal:
        click.echo(item)

if __name__ == '__main__':
    main()