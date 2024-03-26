text = "Ceertain conditions duriing seveal ggenerations aree modified srry"


from textblob import TextBlob

Textblb = TextBlob(text)

output = Textblb.correct()

print(output)