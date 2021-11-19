import re

pattern = r'\[\[(\w+|\w+.*\w+)\]\]'

def test(word):
    bla = re.search(pattern, word).group(1)
    bla = bla.replace(" ", "+")
    bla = bla.replace(",", "")
    return bla

print(test("[[Anowon, the Ruin Thief]]"))
