from dataclasses import dataclass, field
from functools import total_ordering

@dataclass
@total_ordering
class ScoredDoc:
    fileName: str = field(hash=True)
    score: int = field(hash=False)
    keywordCount: dict = field(hash=False)

    def __init__(self, fileName, score, keywordCount):
        self.fileName = fileName
        self.score = score
        self.keywordCount = keywordCount

    def __str__(self):
        return "{} : score = {}".format(self.fileName, self.score)

    def __key(self):
        return self.fileName

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, ScoredDoc):
            return self.__key() == other.__key()
        return NotImplemented

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return (self.score < other.score)

    def _is_valid_operand(self, other):
        return (hasattr(other, "fileName") and
                hasattr(other, "score") and
                hasattr(other, "keywordCount"))