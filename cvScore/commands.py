import click
import cvScore.__main__ as cvScore


@click.command(help="Score the CVs using the provided keywords")
@click.argument("files", type=click.Path(exists=True))
@click.argument("keyword_file", type=click.File('rb'))
def scoreCV(files, keyword_file):
    retVal = cvScore.process_files(files, keyword_file)
