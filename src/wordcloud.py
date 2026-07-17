import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Function for Generating Word Cloud
def generate_wordcloud(text):

  wordcloud = WordCloud(
      width=800,
      height=400,
      background_color='white',
      relative_scaling=0.5,
      min_font_size=8
  ).generate(text)

  plt.figure(figsize=(10, 10))
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis("off")

  plt.show()

# Test Function
if __name__ == "__main__":
  generate_wordcloud('demo.txt')
