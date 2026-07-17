from parser import parser
from frequencies import word_counter
from wordcloud import generate_wordcloud

def main(text):
  text = parser(text)

  if text is None:
    return

  frequencies = word_counter(text)

  generate_wordcloud(text)

# Test Function
if __name__ == "__main__":
    main(text)
