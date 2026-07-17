def parser(filename):
  try:
    with open(txt) as text:
      text = text.read()

  except FileNotFoundError:
    print("File not found.")
    return None

if __name__ == "__main__":
  text = parser("demo.txt")

  if text is not None:
    print(text[:200])
