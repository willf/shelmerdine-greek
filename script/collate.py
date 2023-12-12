# sort the word list in the same order as Shelmerdine.

# read in a TSV file in the following format:
# form	translation	chapter	POS
# ἀγαθός	good	1	ADJ
# sort the word list in the same order as Shelmerdine.
# POS in the following order: VERB, NOUN, PRO, ADJ, ADV, NUM, PREP, CONJ, PART, INTER
# keep the header line intact.
# stdin to stdout

import sys

POSDict = {
    "POS": 0,
    "VERB": 0,
    "NOUN": 1,
    "PRO": 2,
    "ADJ": 3,
    "ADV": 4,
    "NUM": 5,
    "PREP": 6,
    "CONJ": 7,
    "PART": 8,
    "INTER": 9,
}


def chapter_to_int(chapter):
    if chapter == "chapter":
        return 0
    return int(chapter)


def sortKey(line):
    fields = line.strip().split("\t")
    pos = fields[3]
    chapter = fields[2]
    return 1000 * chapter_to_int(chapter) + POSDict[pos]


lines = sys.stdin.readlines()
lines.sort(key=sortKey)
sys.stdout.writelines(lines)
