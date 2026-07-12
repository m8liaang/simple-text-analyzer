DNA_string = input("Enter DNA sequence: ")

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
  
  return A_count, G_count, C_count, T_count

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
  
  return DNA_complements

# TO RUN FUNCTIONS/SEE RESULTS
DNA_base_counter(DNA_string)
DNA_complement(DNA_string)
