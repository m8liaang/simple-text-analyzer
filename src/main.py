from parser import parser
from frequencies import word_counter
from wordcloud import generate_wordcloud

def main():
  text = parser("demo.txt")

  if text is None:
    return

  frequencies = word_counter("demo.txt")

  generate_wordcloud(text)

# Test Function
if __name__ == "__main__":
    main()
