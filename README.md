# cvScore
Scores a set of resumes against a set of keywords.

## Source code, Installation and Usage

### Source code
The source is available at https://github.com/pglebow/cvScore

### Installation
To install this utility, create a virtual environment and install from PyPi.  For example:

    python3 -m venv venv
    source venv/bin/activate
    pip3 install cvScore
    cvScore score --help
    Usage: cvScore score [OPTIONS] CVDIR KEYWORDFILE

    Score a set of resumes against a set of keywords. The resumes must be in PDF
    or DOCX format. The keywords file must have one keyword per line.

    Example:
        score data/resumes keywords.txt

    Options:
        --help  Show this message and exit.

### Using cvScore
To use this utility, create a directory containing your resumes.  PDF and DOCX formats are supported.
Then create a text file with the keywords you're looking for, with one keyword per line.  For example:

    cvScore score dev/cvScore/data dev/cvScore/data/keywords.txt
    data/testDoc1.docx : score = 22
    data/testDoc1.pdf : score = 22
    data/testDoc2.pdf : score = 10
    data/testDoc2.docx : score = 10

## Further details

### Keywords
The keywords are entered into a text file, one per line.  Matching is case-insensitive.
> Example keywords.txt file:
> 
    ETL
    Java
    Python

### Running from Poetry:

    poetry run cvScore score data data/keywords.txt

    data/testDoc1.docx : score = 22
    data/testDoc1.pdf : score = 22
    data/testDoc2.pdf : score = 10
    data/testDoc2.docx : score = 10

### Ranking Algorithm
The algorithm is very simple.  It counts the number of times each keyword occurs
in the document and the score is the sum of the counts.  If multiple documents are
found in the directory, a list of documents, sorted from highest to lowest score, is returned.


