import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Function for Generating Word Cloud
def generate_wordcloud(txt):
  try:
    with open(txt) as file:
      text = file.read()
  except FileNotFound Error:
    print("File not found.")
    return

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

  plt.savefig("data/output/wordcloud.png", dpi=300, bbox_inches="tight")

  plt.show()

# Function Demonstration
if __name__ == "__main__":
  generate_wordcloud('demo.txt')
