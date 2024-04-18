# cvScore
Scores a set of resumes against a set of keywords.

### Keywords
The keywords are entered into a text file, one per line.  Matching is case insensitive.
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


