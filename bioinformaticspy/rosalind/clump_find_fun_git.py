fname = raw_input("Enter file name: ")
def CheckClumpLength(indicies, t, L):
	'''Checks that a given set of t k-mers falls within a clump of size L.'''
	for i in  xrange(len(indicies)-t+1):
		if indicies[t+i-1] - indicies[i] <= L:
			return True
	return False

with open(fname) as input_data:
	dna, [k, L, t] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]

# Find all k-mers, count their appearances, and store thier indicies. 
kmer_dict = dict()
for i in xrange(len(dna)-k+1):
	if dna[i:i+k] in kmer_dict:
		kmer_dict[dna[i:i+k]][0] += 1
		kmer_dict[dna[i:i+k]][1].append(i)
	else:
		kmer_dict[dna[i:i+k]] = [1, [i]]

# The candidate k-mers that appear at least t times, along with the indicies where they appear.
kmer_candidates = [ [kmer[0],kmer[1][1]] for kmer in kmer_dict.items() if kmer[1][0] >= t]

# Check that at least t candidate k-mers fall within a clump of size L.
kmer_clumps = []
for candidate in kmer_candidates:
	if CheckClumpLength(candidate[1], t, L):
		kmer_clumps.append(candidate[0])

# Print and save the solution.
print ' '.join(kmer_clumps)
with open(fname[:-4]+'output.txt', 'w') as output_data:
	output_data.write(' '.join(kmer_clumps))