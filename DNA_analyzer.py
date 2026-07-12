# Obtain DNA sequence of interest
DNA_string = input("Enter DNA sequence: ").upper()

# Base Counter Function
def DNA_base_counter(string):

  A_count, G_count, C_count, T_count = 0, 0, 0, 0
  allowed_characters = {'A', 'G', 'C', 'T'}

  # Check if the DNA sequence is valid
  for char in string:
    if char not in allowed_characters:
      return print("DNA sequence is not valid. Please enter a valid DNA sequence to count its bases.")

    else:
      continue
  
  # Counting bases
  for letter in string:
    if letter == 'A':
      A_count += 1
    elif letter =='G':
      G_count += 1
    elif letter == 'C':
      C_count += 1
    else:
      T_count += 1
  
  return print(f"A: {A_count}, G: {G_count}, C: {C_count}, T: {T_count}")

# GC Content Calculator
def GC_content(string):
  G_counts = string.count('G')
  C_counts = string.count('C')

  GC_content = ((G_counts + C_counts) / len(string)) * 100

  return print(f"GC Content: {round(GC_content, 2)}%")

# Comeplementary Strand Generator
def DNA_complement(string):
  complements = {
      'A' : 'T',
      'G' : 'C', 
      'C' : 'G',
      'T' : 'A'
  }
  allowed_characters = {'A', 'G', 'C', 'T'}
  DNA_complements = ''

  # Check if DNA sequence is valid and generate complementary strand
  for char in string:
    if char not in allowed_characters: 
      return print("DNA sequence is not valid. Please enter a valid DNA sequence to generate its complementary strand.")
    else:
      for key, value in complements.items():
        if key == char:
          DNA_complements += str(complements[f"{key}"])
  
  return print(DNA_complements)

# RNA Strand Generator
def RNA_generator(string):
  allowed_characters = {'A', 'G', 'C', 'T'}

  for char in string:
    if char not in allowed_characters:
      return print("DNA sequence is not valid. Please enter a valid DNA sequence to generate its RNA strand.")
    else:
      return print(string.replace('T', 'U'))

# EXECUTE FUNCTIONS
if __name__ == "__main__":
    DNA_base_counter(DNA_string)
    DNA_complement(DNA_string)
    RNA_generator(DNA_string)
    GC_content(DNA_string)
