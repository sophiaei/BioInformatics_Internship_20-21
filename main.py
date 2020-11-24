#importing random module
import random
import io

#setting up nucleotide list for randomization
nucleo_list = ("A", "T", "C", "G")

def dna_sequence():
  subset1 = ""
  subset2 = ""
  # adding random # of randomized nucleotides to the first subset
  for i in range(random.randint(1, 76)):
    subset1 += nucleo_list[random.randint(0, 3)]
  
  # adding an approriate # of randomized nucleotides to the second subset
  for i in range(150 - len(subset1)):
    subset2 += nucleo_list[random.randint(0, 3)]

  #creating the full sequence
  full_sequence = subset1 + subset2 + subset1 + subset2

  #returns the full sequence.
  return full_sequence


filename = input("File name is: ")
fileheader = input("Gene Info: ")

def fasta_maker(filename, fileheader):
  try:
    with open(filename + ".fasta", "w") as spidroin_handle:
      spidroin_handle.write(">" + fileheader)
      spidroin_handle.write(dna_sequence())
  except IOError as err:
    print("theres an error")
  return spidroin_handle

fasta_maker(filename, fileheader)
