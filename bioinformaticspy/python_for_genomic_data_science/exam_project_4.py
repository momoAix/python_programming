from Bio import SeqIO

#s='ACGGTCAATTCGAACTACTGGCAGAACGTGCAGAAAGGCGCGAAGGCGGCGCTCGACGGCGCGAAGGGCTACACGATGACGTTCCAGGGCCCGGCGGCCGAGTCCGACATCAGCGGCCAGGTCAACATGGTCGACAACGCGGTCACGCGGCATGTGGCGGGCATCGTGCTCGCGCCGTCCGATCCCGATGCGCTGGTGCCCGCGATCAAGAAGGCGTGGGAAGCGCACATTCCCGTCGTGCTGATCGACTCGGCGATCGCGGACGCCGGCAAGCCGTACTACCAGGCGTTCCTGTCGACCGACAACGAGAAGGCGGGCGCGCTGTGCGCGAAGGCGCTGATCGACCGCGTCGGGCAGTCGGGCAAGATCGCGATCATGTCGTACGTGCCGGGCGCGGGGTCCGAGGTCAGCCGCGTCGGCGGGTTCCGCAAGTACATCGAGAGCCATTCGAAGCTGCAGGTCGTCGGCCCGTACTACTCGCAATCGCAAATGGCGACCGCGCTGAACCAGACGACCGACGTGCTGTCGGCGAACCCGGACCTGAAGGGCATCTTCGGCGCGAACGAGCCGACCGCGGTCGGGATGGGCCGTGCGCTGAAGCAGTCGGGCAAGGCGGGCAAGGTGGTGGCGATCGGGTTCGACGGCAACGAGGACCTGCAGGGCTTCGTGCGCGACGGCACCGTGCAGGCGATCGCCGTGCAGGGCTCGTGGCAGATGGGGAACCAGGGCGTGCGCACGGCGCTCGACGTGATCGAGCGCAAGCCCGCGCCGAAGCTGATCGATACCGGCGTCGTGATGGTCGACAAGCAGAACCTCGATTCGCAGGCGGCGAAGAACGTCCTGTACTGATCCCTTTTCCCCGCATCCGGTTACGCCTCATGAATGCAAACGATACGCGCACCTTGCCGCGCAGCGGGCTGACGGTGTCCGCGCTCGGCCTCGGCTGCTCGCAGCTCGGCGGCCTTTATCGGCCGATGTCGGCCGCCGATGCCGCCGCGCTCGTCGACGCCGCGTGGGCGGCCGGCCTGCGCTATTTCGACACCGCGCCGTATTACGGCTACACGCTGTCCGAGCGGCGCGTGGGGGCGGGGCTCGCCCCGCGCGAGCGCCGCGCCTTCACGCTCAGCACGAAGGTCGGGCGGCTGATGCGGGCCGACGCGAGCGTGCGGCCGGGCGACGACGGCTGGGCGGAGCCGCTGCCGTTCCGGCCGGTGTACGACTACAGCTACGACGGCATCATGCGCTCGCACGACGACAGCCGGCAACGGCTCGGGCTCGCGCGAGTCGACATGCTGTACGTGCACGACATCGGCGCGATGACGCACGGCGATCGTCACGCGCACTACTGGGACCAGTTGACCCGCGGCGGCGGGTTTCGCGCGCTGGATGCGTTGCGCTCGGGCGGCGAGATCGGCGGGTTCGGTCTCGGCGTGAACGAATGGGAAGTCGCGGCCGACGCGCTGAACGAAGCGGCGCTCGATGCGGTGCTGCTGGCCGGCCGCTATACGCTGCTCGAACAGACGGCGCTCGAACCGCTGCTCGACGCGTGTGCCCGTGAAGGGACGGCGATCGTGATCGGCGGCGTGTTCAATTCCGGTTTGCTCGCCGGCAACGGCAAATTCAACTATGCGGACGCGAGCGCCGACGTGATCGACAAGGCGACGCGGCTCGGCGCGTTGTGCAACCGCTTCGACGTGCCGCTTCCGGCCGCGGCGTTGCAGTTTCCGTTCGGCCATCCGGCCGTCGTGTCGTGCGTGGTCGGCGCGCGCAGCGTGGCTCAGCTGAAGCAGAACATCGCATGGTTCGAGCGCCCCGCGCCGGCCGAGCTGTGGGATGCGCTGCGCGACGAAGGGCTGATCGCGGCGCACGCGCCGGTGCCGGGAGCACACGCATGACCCCGCGCATCGACGCCCATCAGCACTACTGGCGCATCGACGCGCGGGCCGGCTGCTGGCCGCCGGCCGAGCTCGACGCGATTCACCGGGATTTCGGCCCGGCCGATCTGGCGCCGCTGCTCGACGCCGCGCGCATCGATATCACCGTCGTCGTGCAGTCGCTGCCGAGCGAAGCCGACACGCGCTTTCTGCTCGATCTCGCGGCTGAAACGCCGAGCGTCGGCGCCGTGGTCGGCTGGGTCGACCTGAAGGCCGACGACGCACCCGCGCGGATCGCGGCGTTTGCATCCGCGCCGAAGGCGCGCGGCTTGCGACCGATGCTGCAGGATCTGCCCGACGACGCGTGGATCGACGATCCGCGGCTGGATCGCGCAGTCGCCGCGATGCTCGAGTACGGGCTGCGTTTCGATGCGCTGGTGATGCCGCGCCATCTCGATGCGCTGCACGCGTTCGCGCAACGCCATCCGGATCTGCCGATCGTGATCGACCACGGCGCGAAGCCGTTCATCGAGCGCGGCGAGATGCAGCCGTGGCTAACGGCGATGCGCAGGCTCGCGAGCCTGCCGAACCTGCATTGCAAGCTGTCCGGCCTCTGGACGGAAGCCGGGCCGTCGGCCGGCCCGGATGCGGTGCGCGCACGCACGCGGCCGTATGTCCAGGCGCTGGCCGAGCTGTTCGGGCCGACGCGCTTGATGTGGGGCAGCGACTGGCCGGTGCTGCGGCTGGCGTCGGCGTGCGGCGGCTACGGCGAATGGCTGGCCGCGTGCGAGGACGACTGCGCGCAGATGCTCGGCGCCGCGGCGCTGGAGGACCTTTTCGGCGGCAACGCGCGCCGCTTCTACCGGATCGACACCGCACGCCACGACGAATGAACCAGAACGAAAGGAAACCGACATGCTCAGCGTGATTTGCGAATCCCCCGGCGTGCTGCGCGTGCAGCATCGCGAGCTGCCCGTGCGCGGCAGCGGCGAAGTGCTGTTGCGCGTGCAACGGGTCGGCATCTGCGGCACCGATCTGCACATCTTCACCGGCAACCAGCCGTACCTCGACTATCCGCGCGTGATGGGCCACGAGCTGTCGGCGGTCGTCGTCGAGGCGGAAGCCGAGTCGGGGCTCGGCGCCGGCGACGCGGTGTACGTGATGCCGTATCTGTCGTGCGGGCACTGCGTCGCCTGCCGTCACGGCAACACGAACTGCTGCGTGAACATCAAGGTGCTCGGCGTGCATCGCGACGGCGCACTCGCCGAATACCTGAGCGTGCCCGCGCAGTTCGTGCACAAGGCCGACGGCATTTCGCTCGACCAGGCGGCGATGCTCGAATTTCTCGCGATCGGCGCGCATGCGGTGCGGCGCGCGGACATCCGCGCCGGGCAGCGCGCGCTGGTCGTCGGCGCCGGGCCGATCGGCATGGCCGCGATGATCTTCGCGAAGCTGCGCGGCGCCGACGTCACGTGCCTCGACACGCGGGCCGACCGGCTGGCGTTCTGCCGCCAGCATCTGGCGGTCGATGCGGCGGTGGAGGTGGGGGAAGGCGACGCGGAGCGTCTCGCGTCGTTGACGAACGGCGAGTATTTCGATGCGGTGTTCGACGCGACCGGCAACCTCGATGCGATGAATCGCGGTTTCGAATTCGTCGCGCACGGCGGCAAATACACGTTGATCTCGATCGTGCGCGGGCACGTCGCGTTTTCGGATCCCGAGTTCCACAAGCGGGAAACCACGCTGCTCGCGAGCCGCAATGCGACGGCCGAGGATTTCGCGACGGTGCTCGACGCGATGCGCGCGGGGCGCATTCCGGACCGCGCGCTGAACACGCACCGGATGCGGCTCGATGAGGTGCCGGACGCGCTGCCGCGTCTGCTGGATGCCGGGCAGACCGTCGTGAAGGCGCTCGTCGAATGCTGATCTATCGAATCCGCCACGCGGAGCGCACGCGATGACGCCGCCGATCCTGCAGTTCGGCACGAGCCGCTTCCTGCTCGCGCACGTCGACCTGTTCGTCTCCCAGGCGCTGGACGAAGGCAACGCGATCGGCGGCATCGGCATCGTGCAGACGACCGGCAATCCGGCCAGCCGCGCCCGCATCGACGCGCTGCGCGCCACCGGCCGCTATCCGGTGCGGATTCGCGGGCGCGAGCGCGGCGGCGTGGTCGACGAAGTCGTCGAGTGCCGCGCCGTGCAGCGCGCGTGGGACGCCGAGCGCGACTGGGCGGAAATACGCGGCGCCGCGATCGAGACGGTGCGCGTGATCGTGTCGAACACCGGCGACGCAGGCTATCGCGCCGATCCGCGCGACGCCGCAAAC'
s2=6
#a=''	
def get_kmer(s, s2):
	count=dict()
	for i in range(len(s)-int(s2)):
		if s[i:].startswith(s[i:i+int(s2)]):
			count[s[i:i+int(s2)]]=count.get(s[i:i+int(s2)],0)+1	
    	return count 
for s in SeqIO.parse("dna1.fasta.fasta", "fasta"):

	kkk= get_kmer (s.seq, s2)
	for a in [key for key, value in kkk.items() if value==max(kkk.values())] :
		print "the frequent k-mers:", key, value 
		
