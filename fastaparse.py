def calc_mass(prot_seq):
	prot_mass= {
        'A':   71.03711,
	'C':   103.00919,
	'D':  115.02694,
	'E':   129.04259,
	'F':   147.06841,
	'G':   57.02146,
	'H':   137.05891,
	'I':   113.08406,
	'K':   128.09496,
	'L':   113.08406,
	'M':   131.04049,
	'N':   114.04293,
	'P':   97.05276,
	'Q':   128.05858,
	'R':   156.10111,
	'S':   87.03203,
	'T':   101.04768,
	'V':   99.06841,
	'W':   186.07931,
	'Y':   163.06333
	}
	result=0
	for i in range(0,len(prot_seq)):
	    mass = prot_mass[prot_seq[i]]
	    result += float(mass)
	return ( "%.4f"% result)

def parse(file_path):
   fasta_dict={}
   with open(file_path, 'r') as f:
     for line in f:
         if line[0] == '>':
            id_=line[1:].replace('\n','')
            DNA=''
         else:
             NA+=line.replace('\n','')
             fasta_dict[id_]=DNA
   return(fasta_dict)

def translate(rna_seq):
      return(rna_seq.replace('T','U'))


def ribosoma(rna_seq,mas,k):
    cod = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
    }
    for i in range(k,len(rna_seq),3):
      result = str()
      if rna_seq[i:i+3]=='AUG':
        try:
          for j in range(i, len(rna_seq),3):
             symbol = cod[rna_seq[j:j+3]]
             if symbol == 'Stop':
                result += symbol
                break
             result += symbol
        except:
            pass
      mas += [result]

def orf(rna_seq):
    mas=[]
    for i in range(3):
           ribosoma(rna_seq,mas,i)
    for i in range(len(mas)):
       if 'Stop' not in mas[i]:
           mas[i] = ''
       else:
           mas[i] = mas[i][:-4]
    mas = [x for x in mas if x]
    return(mas)

def mass_table():
        mass_table= {
        'A':   71.03711,
	'C':   103.00919,
	'D':  115.02694,
	'E':   129.04259,
	'F':   147.06841,
	'G':   57.02146,
	'H':   137.05891,
	'I':   113.08406,
	'K':   128.09496,
	'L':   113.08406,
	'M':   131.04049,
	'N':   114.04293,
	'P':   97.05276,
	'Q':   128.05858,
	'R':   156.10111,
	'S':   87.03203,
	'T':   101.04768,
	'V':   99.06841,
	'W':   186.07931,
	'Y':   163.06333
	}
        return(mass_table)
def rna_codon():
    rna_codon = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
    }
    return(rna_codon)

