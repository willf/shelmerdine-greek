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
# cat data/words.tsv | python3 script/collate.py | python3 script/to_markdown.py > vocabulary/vocabulary.md


import sys

href_dict = {
    "ADJ": "Declension",
    "ADV": "Adverb",
    "CONJ": "Conjunction",
    "INTER": "Interjection",
    "NOUN": "Declension",
    "PART": "Particle",
    "PREP": "Preposition",
    "PRO": "Declension",
    "VERB": "Inflection",
}

pos_dict = {
    "ADJ": "Adjectives",
    "ADV": "Adverbs",
    "CONJ": "Conjunctions",
    "INTER": "Interjections",
    "NOUN": "Nouns",
    "PART": "Particles",
    "PREP": "Prepositions",
    "PRO": "Pronouns",
    "VERB": "Verbs",
}

current_chapter = None
current_pos = None

if len(sys.argv) >= 2:
    title = sys.argv[1]
else:
    title = "Introduction to Greek (Shelmerdine & Shelmerdine, 3rd Edition) Vocabulary"

print("# " + title)

header = True
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
    parts = [x.strip() for x in form.split(",")]
    part0 = parts[0]
    lemma = part0.replace(" ", "_")
    # remove any parentheticals from the lemma
    lemma = lemma.split("(")[0].strip()
    # remove any ... from the lemma
    lemma = lemma.split("...")[0].strip()
    if href_dict[pos]:
        part0_link = (
            f"[{form}](https://en.wiktionary.org/wiki/{lemma}#{href_dict[pos]})"
        )
    else:
        part0_link = f"[{form}](https://en.wiktionary.org/wiki/{lemma})"
    translation = fields[1]
    chapter = fields[2]
    if chapter != current_chapter:
        current_chapter = chapter
        print("\n## Chapter " + chapter)
        current_pos = None
    if pos != current_pos:
        current_pos = pos
        print("\n### " + pos_dict[pos])
    print("- " + part0_link + " : " + translation)
