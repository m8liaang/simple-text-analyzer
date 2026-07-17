from parser import parser
from frequencies import word_counter
from wordcloud import generate_wordcloud

def main(text):
  text = parser(text)

  frequencies = word_counter(text)
  print(frequencies)
  
  generate_wordcloud(text)

# Test Function
if __name__ == "__main__":
    main("demo.txt")
