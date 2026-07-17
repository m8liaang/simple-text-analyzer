import re
import pandas as pd

# Function to Count Word Frequencies
def word_counter(txt):
  txt_words = {}

  try:
      with open(txt) as text:
        text = text.read()
        words = re.findall(r'\b\w+\b', text)

      for word in words:
        # Lower case all the words
        word = word.lower()

        # Count number of times the word appears
        txt_words[word] = txt_words.get(word, 0) + 1
        
        # Convert dictionary into df (organized into a table, highest to lowest frequencies)
        words_table = pd.DataFrame(txt_words.items(), columns=['Word', 'Frequency'])
        words_table = words_table.sort_values(by='Frequency', ascending=False)
        
      pd.set_option('display.max_rows', None)
      pd.set_option('display.max_columns', None)
      pd.set_option('display.max_colwidth', None)

      print(words_table)
  
  except FileNotFoundError:
    print("File not found.")

# Execute Function
if __name__ == "__main__":
  word_counter("demo.txt")
