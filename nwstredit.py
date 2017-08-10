# coding: utf-8
import sys

def print_table(s1,s2,table,trace=None):
    """print the DP table, t, for strings s1 and s2.  
    If the optional 'trace' is present, print * indicators for the alignment.
    Fancy formatting ensures this will also work when s1 and s2 are lists of strings"""
    print "       ",
    for i in range(len(s1)):
        print "%3.3s" % s1[i],
    print
    for i in range(len(table)):
        if i > 0: print "%3.3s" % s2[i-1], 
        else: print '   ',
        for j in range(len(table[i])):
            if trace and trace[i][j] == "*":
                print "*" + "%2d" % table[i][j],
            else:
                print "%3d" % table[i][j],
        print

def argmin (*a):
    """Return two arguments: first the smallest value, second its offset"""
    min = sys.maxint; arg = -1; i = 0
    for x in a:
        if (x < min):
            min = x; arg = i
        i += 1
    return (min,arg)
            

def nwstredit (s1,s2, showtable=True):
    "Calculate Levenstein edit distance for strings s1 and s2."
    len1 = len(s1) # vertically
    len2 = len(s2) # horizontally
    # Allocate the table
    table = [None]*(len2+1)
    for i in range(len2+1): table[i] = [0]*(len1+1)
    # Initialize the table
    for i in range(1, len2+1): table[i][0] = i
    for i in range(1, len1+1): table[0][i] = i
    # Do dynamic programming
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if s1[j-1] == s2[i-1]:
                d = 0
            else:
                #d = 1
		d = distancia(s1[j-1],s2[i-1])
            table[i][j] = min(table[i-1][j-1] + d,
                              table[i-1][j]+d+1,
                              table[i][j-1]+d+1)
    if showtable:
        print_table(s1, s2, table)
    return table[len2][len1]

def nwstredit2 (s1,s2, showtable=True):
    "String edit distance, keeping trace of best alignment"
    len1 = len(s1) # vertically
    len2 = len(s2) # horizontally
    # Allocate tables
    table = [None]*(len2+1)
    for i in range(len2+1): table[i] = [0]*(len1+1)
    trace = [None]*(len2+1)
    for i in range(len2+1): trace[i] = [None]*(len1+1)
    # initialize table
    for i in range(1, len2+1): table[i][0] = i
    for i in range(1, len1+1): table[0][i] = i
    # in the trace table, 0=subst, 1=insert, 2=delete
    for i in range(1,len2+1): trace[i][0] = 1
    for j in range(1,len1+1): trace[0][j] = 2
    # Do dynamic programming
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if s1[j-1] == s2[i-1]:
                d = 0
            else:
                #d = 1
		d = distancia(s1[j-1],s2[i-1])
            # if true, the integer value of the first clause in the "or" is 1
            table[i][j],trace[i][j] = argmin(table[i-1][j-1] + d,
                                             table[i-1][j]+d+1,
                                             table[i][j-1]+d+1)
    if showtable:
	# If you are implementing Smith-Waterman, then instead of initializing
	# i=len2 and j=len1, you must initialize i and j to the indices 
	# of the table entry that has the miminum value (it will be negative)
        i = len2
        j = len1
        while i != 0 or j != 0:
            if trace[i][j] == 0:
                nexti = i-1
                nextj = j-1
            elif trace[i][j] == 1:
                nexti = i-1
                nextj = j
            elif trace[i][j] == 2:
                nexti = i
                nextj = j-1
	    else:
		nexti = 0
		nextj = 0
            trace[i][j] = "*"
            i = nexti
            j = nextj
	    print "ij", i, j
        print_table(s1, s2, table, trace)
    return table[len2][len1]

def distancia(l1,l2):
    
    if l1 == l2:
	dist = 0
    
    else:
    
	letra1= l1
	letra2=l2
	#tratando os acentos
	aas = ["à","á","â","ã"]
	ccs = ["ç"]
	ees = ["è","é","ê"]
	iis = ["ì","í","î"] 
	oos = ["ò","ó","ô","õ"]
	uus = ["ù","ú","û"]
	#removendo os acentos
	for letra in aas:
	    if letra1 == letra:
		letra1 = "a"
	    if letra2 == letra:
		letra2 = "a"
		    
	for letra in ccs:
	    if letra1 == letra:
		letra1 = "c"
	    if letra2 == letra:
		letra2 = "c"
	for letra in ees:
	    if letra1 == letra:
		letra1 = "e"
	    if letra2 == letra:
		letra2 = "e"
	for letra in iis:
	    if letra1 == letra:
		letra1 = "i"
	    if letra2 == letra:
		letra2 = "i"
	for letra in oos:
	    if letra1 == letra:
		letra1 = "o"
	    if letra2 == letra:
		letra2 = "o"
	for letra in uus:
	    if letra1 == letra:
		letra1 = "u"
	    if letra2 == letra:
		letra2 = "u"
	
	if letra1 == letra2:
	    dist=1
	else:
	    #teclado = {}
	    #teclado[1][1]="q"
	    #teclado[1][2]="w"
	    #teclado[1][3]="e"
	    #teclado[1][4]="r"
	    #teclado[1][5]="t"
	    #teclado[1][6]="y"
	    #teclado[1][7]="u"
	    #teclado[1][8]="i"
	    #teclado[1][9]="o"
	    #teclado[1][10]="p"
	    #teclado[2][1]="a"
	    #teclado[2][2]="s"
	    #teclado[2][3]="d"
	    #teclado[2][4]="f"
	    #teclado[2][5]="g"
	    #teclado[2][6]="h"
	    #teclado[2][7]="j"
	    #teclado[2][8]="k"
	    #teclado[2][9]="l"
	    #teclado[2][10]=None
	    #teclado[3][1]="z"
	    #teclado[3][2]="x"
	    #teclado[3][3]="c"
	    #teclado[3][4]="v"
	    #teclado[3][5]="b"
	    #teclado[3][6]="n"
	    #teclado[3][7]="m"
	    #teclado[3][8]=None
	    #teclado[3][9]=None
	    #teclado[3][10]=None
	    
	    teclado = [["q","w","e","r","t","y","u","i","o","p"],
		       ["a","s","d","f","g","h","j","k","l",None],
		       ["z","x","c","v","b","n","m",None,None,None]]
	
	    for linha in range(0,3):
		for coluna in range(0,10):
		    if letra1 == teclado[linha][coluna]:
			coluna1 = coluna
			linha1 =linha
		    if letra2 == teclado[linha][coluna]:
			coluna2 = coluna
			linha2 =linha
    
	    aux = coluna1 - coluna2 
	    aux2 = linha1 - linha2
	    if aux < 0:
		aux= aux * -1
	    if aux2 < 0:
		aux2 = aux2 * -1
	    dist = aux + aux2
	    dist = dist +1 #aumenta um pois são letras diferentes, a distancia 1 é para letras iguais mas com acentos diferentes
	    
    print dist
    return dist

	    
    
    
#stredit2('mccallum', 'mcalllomo')
#stredit(['this', 'is', 'a', 'test'], ['this', 'will', 'be', 'another', 'test'])
#stredit2("s'allonger", "lounge")
#stredit2("lounge", "s'allonger")
#stredit2('cow over the moon', 'moon in the sky')
#stredit2('another fine day', 'anyone can dive')
#stredit2('another fine day in the park', 'anyone can see him pick the ball')

# import dicts
# argvlen = len(sys.argv)
# target = sys.argv[argvlen-2].lower()
# filename = sys.argv[argvlen-1]
# d = dicts.DefaultDict(0)
# for word in open(filename).read().split():
#     if word not in d:
#       word = word.lower()
#       d[word] = stredit(word, target, False)
# print d.sorted(rev=False)[:20]

