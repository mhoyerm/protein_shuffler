import sys

import random



def main():

	if len(sys.argv) < 3:

		print("Use: <.py file> <input file> <output file>")

		sys.exit(0)


	# input file

	filein = open(sys.argv[1], 'r')

	fin = filein.read()



	# output file

	fout = open(sys.argv[2], 'w')


	# define amino acids

	aa = [["G","A","L","V","I","P","F","S","T","C","Y","N","Q","D","E","R","K","H","W","M"],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


	# split genes by '>'

	lista1 = str.split(fin, '>')

	percentage = 0

	interface = 0

	for i in range(len(lista1)-1):

		nonsense = "false"

		percentage = 50*i/len(lista1)

		while interface < percentage:

			interface += 1

			print(str(interface)+"% complete")

		newvalue = str.split(lista1[i+1], ']')



		# lista2 = list of each base in a gene

		lista2 = newvalue[len(newvalue)-1]

		lista2 = lista2.replace("\n", "")

		lista2 = lista2.replace("\r", "")

		lista2 = list(lista2) 

		



		j = 0

		while j < len(lista2):

			matched = "false"

			try:

				codon = lista2[j]

			except Exception:

				print(str.split(name, ' ')[0]+": fragmented codon")

				break

			for w in range(len(aa[0])):

				if matched == "false":

					if codon == aa[0][w]:

						matched = "true"

				if matched == "true":

					aa[1][w] += 1

			j+=1



	for i in range(len(lista1)-1):

		nonsense = "false"

		percentage = 50+50*i/len(lista1)

		while interface < percentage:

			interface += 1

			print(str(interface)+"% complete")

		newvalue = str.split(lista1[i+1], ']')

		for j in range(len(newvalue)-1):

			name = newvalue[j] + "]"

		fout.write("\n>"+name+"\n")



		# lista2 = list of each base in a gene

		lista2 = newvalue[len(newvalue)-1]

		lista2 = lista2.replace("\n", "")

		lista2 = lista2.replace("\r", "")

		lista2 = list(lista2) 

		

		j = 0

		while j < len(lista2):

			try:

				codon = lista2[j]

			except Exception:

				print(str.split(name, ' ')[0]+": fragmented codon")

				break

			if codon != "UAA" or "UAG" or "UGA":

				itsamatch = "false"

				for w in range(len(aa[0])):

					if codon == aa[0][w]:

						teste = random.random()*aa[1][len(aa[1])-1]

						for z in range(len(aa[0])):

							if  itsamatch == "false":

								if teste <= aa[1][z]:

									fout.write(aa[0][z])

									itsamatch = "true"

							if itsamatch == "true":

								aa[1][z] -= 1

						break

			j+=1


main()

print("100% complete!\n")