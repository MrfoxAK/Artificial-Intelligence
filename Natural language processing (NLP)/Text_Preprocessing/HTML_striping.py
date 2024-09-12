import re

text = "<p>This is <sub>subscripted</sub> text.</p>"

def stripHTML(data):
     p = re.compile(r'<.+?>')
     return p.sub('',data)


print(stripHTML(text))