# read in a TSV file in the following format:
# form	translation	chapter
# βλάπτω, βλάψω, ἔβλαψα	harm, injure, damage	2
# γράφω, γράψω, ἔγραψα	write	2
# and output a markdown file in the following format:
# ## Chapter 2
# - [βλάπτω, βλάψω, ἔβλαψα](https://en.wiktionary.org/wiki/βλάπτω#Inflection): harm, injure, damage
# - [γράφω, γράψω, ἔγραψα](https://en.wiktionary.org/wiki/γράφω#Inflection): write
# etc.
# The script is run from the command line like this
# cat verbs.md | python3 verbs_tsv_to_markdown.py Verbs > verbs.md


import sys

header = True
current_chapter = None

title = sys.argv[1]

print("# " + title)

for line in sys.stdin:
    if header:
        header = False
        continue
    line = line.strip()
    if line == "":
        continue
    fields = line.split("\t")
    if len(fields) != 3:
        continue
    form = fields[0]
    parts = [x.strip() for x in form.split(",")]
    onepp = parts[0]
    onepp_link = f"[{form}](https://en.wiktionary.org/wiki/{onepp}#Inflection)"
    translation = fields[1]
    chapter = fields[2]
    if chapter != current_chapter:
        current_chapter = chapter
        print("\n## Chapter " + chapter)
    print("- " + onepp_link + ": " + translation)
