# read a tsv file with the following columns:
# form	translation	chapter	POS
# for example:
# βλάπτω, βλάψω, ἔβλαψα	harm, injure, damage	2	VERB
# γράφω, γράψω, ἔγραψα	write	2	VERB
# and for each chapter, create a file with the following name, e.g.: chapter_02.tsv
# with the following columns:
# form	translation
# for example:
# βλάπτω	harm, injure, damage
# βλάψω	harm, injure, damage
#
# run this script like this:
# mkdir -p for_quizlet
# cat data/words.tsv | python3 script/collate.py | python3 script/for_quizlet.py
import sys

header = True
current_chapter = None
out = None
for line in sys.stdin:
    if header:
        header = False
        continue
    line = line.strip()
    if line == "":
        continue
    fields = line.split("\t")
    form = fields[0]
    translation = fields[1]
    chapter = fields[2]
    pos = fields[3]
    if chapter != current_chapter:
        if out:
            out.close()
        current_chapter = chapter
        current_chapter_padded = "{:02d}".format(int(current_chapter))
        filename = f"for_quizlet/chapter_{current_chapter_padded}.tsv"
        print(f"writing to {filename}")
        out = open(filename, "w")
    out.write(f"{form}\t{translation} ({pos.lower()})\n")
if out:
    out.close()
