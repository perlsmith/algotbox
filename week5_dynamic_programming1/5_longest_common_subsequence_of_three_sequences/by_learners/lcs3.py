#Uses python3

import sys
import pdb

def lcs3(a, b, c):
	#write your code here
	# ( list, list , list ) --> int
	an = len( a )
	bn = len( b )
	cn = len( c )
	
	D = []
	# this is just the init loop
	for k in range( cn+1 ) :
		D1 = []
		for j in range( bn+1 ) :
			D2 = []
			for i in range( an+1 ) :
				if k == j == 0 :
					D2.append( [i,0] )
				elif j == i == 0 :
					D2.append( [k,0] )
				elif k == i == 0 :
					D2.append( [j,0] )
				else :
					D2.append( [0,0] )
			D1.append( D2 )
		D.append( D1 )
	
	# now, we're back at dynamic programming - filling in from left to right
	# same deal - mismatches are penalized double. So, you get a slightly different "edit distance"
	# and keep track of matches as well..
	for k in range( cn+1 ) :
		for j in range( bn+1 ) :
			for i in range( an+1 ) :
				if k == j == i == 0 or D[k][j][i][0] != 0 :
					continue
				if j >= 1 :
					ins1 = D[k][j-1][i][0] + 1
					if i >= 1 :
						mm1 = D[k][j-1][i-1][0] + 2
					else :
						mm1 = 10
				else :
					ins1 = 10
					mm1 = 10
				if k >= 1 :
					ins2 = D[k-1][j][i][0] + 1
					mm = D[k-1][j-1][i-1][0] + 3
					match = D[k-1][j-1][i-1][0]
					if j >= 1 :
						mm2 = D[k-1][j-1][i][0] + 2
						if i >= 1 :
							mm = D[k-1][j-1][i-1][0] + 3
							match = D[k-1][j-1][i-1][0]
						else :
							mm = 10
							match = 10
					else :
						mm2 = 10
						mm = 10
						match = 10
				else :
					ins2 = 10
					mm = 10
					match = 10
					mm2 = 10
				if i >= 1 :
					ins3 = D[k][j][i-1][0] + 1
					if k >= 1 :
						mm3 = D[k-1][j][i-1][0] + 2
					else :
						mm3 = 10
				else :
					ins3 = 10
					mm3 = 10
				if a[i-1] == b[j-1] == c[k-1] :
					if ins1 == min( ins1, ins2, ins3, mm1, mm2, mm3, match ) :
						D[k][j][i] = [ ins1,  D[k][j-1][i][1] ]
					elif ins2 == min( ins1, ins2, ins3, mm1, mm2, mm3, match ) :
						D[k][j][i] = [ ins2 , D[k-1][j][i][1] ]
					elif ins3 == min( ins1, ins2, ins3, mm1, mm2, mm3, match ) :
						D[k][j][i] = [ ins3 , D[k][j][i-1][1] ]
					elif mm1 == min( ins1, ins2, ins3, mm1, mm2, mm3, match ) :
						D[k][j][i] = [ mm1 ,  D[k][j-1][i-1][1] ]
					elif mm2 == min( ins1, ins2, ins3, mm1, mm2, mm3, match ) :
						D[k][j][i] = [ mm2 ,  D[k-1][j-1][i][1] ]
					elif mm3 == min( ins1, ins2, ins3, mm1, mm2, mm3, match ) :
						D[k][j][i] = [ mm3 ,  D[k-1][j][i-1][1] ]
					else :	# match
						D[k][j][i] = [ match, 1 + D[k-1][j-1][i-1][1] ]
				else :
					if ins1 == min( ins1, ins2, ins3, mm1, mm2, mm3, mm ) :
						D[k][j][i] = [ ins1,  D[k][j-1][i][1] ]
					elif ins2 == min( ins1, ins2, ins3, mm1, mm2, mm3, mm ) :
						D[k][j][i] = [ ins2 , D[k-1][j][i][1] ]
					elif ins3 == min( ins1, ins2, ins3, mm1, mm2, mm3, mm ) :
						D[k][j][i] = [ ins3 , D[k][j][i-1][1] ]
					elif mm1 == min( ins1, ins2, ins3, mm1, mm2, mm3, mm ) :
						D[k][j][i] = [ mm1 ,  D[k][j-1][i-1][1] ]
					elif mm2 == min( ins1, ins2, ins3, mm1, mm2, mm3, mm ) :
						D[k][j][i] = [ mm2 ,  D[k-1][j-1][i][1] ]
					elif mm3 == min( ins1, ins2, ins3, mm1, mm2, mm3, mm ) :
						D[k][j][i] = [ mm3 ,  D[k-1][j][i-1][1] ]
					else :	# mismatch
						D[k][j][i] = [ mm, D[k-1][j-1][i-1][1] ]
						
	return D[cn][bn][an][1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    #pdb.set_trace()
    print(lcs3(a, b, c))
