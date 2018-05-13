# Uses python3
import pdb

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax( i, j, m, M , ops) :
	# (int, int ) --> ( int, int )
	Min = 1e18
	Max = -1e18	# -inf essentially :)
	if i == j :
		return (m[i][i], M[i][i] )
	elif j == i + 1 :
		result = evalt( m[i][i], m[j][j], ops[i] )
		return (result, result )
	else :
		for k in range( i, j ) :
			a = evalt( M[i][k], M[k+1][j], ops[k] ) # max, max
			b = evalt( M[i][k], m[k+1][j], ops[k] ) # max, min
			c = evalt( m[i][k], M[k+1][j], ops[k] ) # min, max
			d = evalt( m[i][k], m[k+1][j], ops[k] ) # min, min
			Min = min( Min, a, b, c, d)
			Max = max(Max, a, b, c, d )
	return ( Min, Max )

	
def get_maximum_value(dataset):
	# ( string ) --> int
    #write your code here
	digits = list( map( int, dataset[::2] ) )
	ops = dataset[1::2]
	n = len( digits )
	m = []
	M = []
	for i in range( n ) :
		m.append( [0] * i + [digits[i]] + [0] * ( n - i - 1 ) )
		M.append( [0] * i + [digits[i]] + [0] * ( n - i - 1 ) )
	for s in range( n-1 ) :
		for i in range( n-1 - s ) :
			j = i + s + 1		# this is essentially translating the pseudocode... the poor guys don't count like hackers :(
			m[i][j], M[i][j] = MinAndMax( i, j, m, M, ops )
	return M[0][n-1]

def write_opt_expr( dataset ) :
	# string --> string
	# converts the string into 2 lists - positive ints and operators
	# returns the same string with parantheses inserted..
	digits = list( map( int, dataset[::2] ) )
	ops = dataset[1::2]
	n = len( digits )
	m = []
	M = []
	for i in range( n ) :
		m.append( [0] * i + [digits[i]] + [0] * ( n - i - 1 ) )
		M.append( [0] * i + [digits[i]] + [0] * ( n - i - 1 ) )
	for s in range( n-1 ) :
		for i in range( n-1 - s ) :
			j = i + s + 1		# this is essentially translating the pseudocode... the poor guys don't count like hackers :(
			m[i][j], M[i][j] = MinAndMax( i, j, m, M, ops )
	
	# start with 0, n-1 - where will you insert parantheses here?
	# start with 0,0 and 1,n-1 - that is, you go through each operator
	# and, given the operator, you retrive the min and max of the expressions on either
	# side and see if this split (insertion) fits the bill..
	return opt_split( m, M, digits, 0, n-1, ops , True)

def opt_split( m, M, digits, start, end , ops, ifMax  ) :
	# 2-D list of ints, 2D list of ints, list of ints, int, int, array of strings, boolean --> string
	# give it the min and max dynamically computed tables, and the start and end and the ops
	# and whether you're looking for a max
	#  and it gives you the paranthesized digit string by calling itself recursively
	# logic : start, end and ifMax tell you whether to look in m or M for the target
	# after that, it's brute-force searching to look for a match for whether to
	# "split here" and then, a recursive call to get the sub-expressions after the split
	if start == end : 
		return str(digits[start])
	for i in range(start, end+1 ) :
		op = ops[i]
		if '+' == op :
			if ifMax :
				if M[start][end] == M[start][i] + M[i+1][end] :
					return '(' + opt_split( m, M, digits, start, i, ops , True) + op + opt_split( m, M, digits, i+1, end, ops , True) + ')'
			elif m[start][end] == m[start][i] + m[i+1][end] :
				return '(' + opt_split( m, M, digits, start, i, ops , False) + op + opt_split( m, M, digits, i+1, end, ops, False ) + ')'
		elif '-' == op :
			if ifMax :
				if M[start][end] == M[start][i] - m[i+1][end] :
					return '(' + opt_split( m, M, digits, start, i, ops, True ) + op + opt_split( m, M, digits, i+1, end, ops , False) + ')' 
			elif m[start][end] == m[start][i] - M[i+1][end] :
				return '(' + opt_split( m, M, digits, start, i, ops, False ) + op + opt_split( m, M, digits, i+1, end, ops , True) + ')'
		elif '*' == op :
			if ifMax :
				if M[start][end] == M[start][i] * M[i+1][end] :
					return '(' + opt_split( m, M, digits, start, i, ops , True) + op + opt_split( m, M, digits, i+1, end, ops , True) + ')'
				elif M[start][end] == m[start][i] * m[i+1][end] :
					return '(' + opt_split( m, M, digits, start, i, ops , False ) + op + opt_split( m, M, digits, i+1, end, ops , False ) + ')'
			else :	# you want a minimum
				if m[start][end] == M[start][i] * m[i+1][end] :
					return '(' + opt_split( m, M, digits, start, i, ops , True) + op + opt_split( m, M, digits, i+1, end, ops , False) + ')'
				elif M[start][end] == m[start][i] * M[i+1][end] :
					return '(' + opt_split( m, M, digits, start, i, ops , False ) + op + opt_split( m, M, digits, i+1, end, ops , True ) + ')'			

	
if __name__ == "__main__":
	pdb.set_trace()
	#print(get_maximum_value( list(input() ) ))
	print( write_opt_expr( list(input() ) ) )	# not requested. Own initiative..


# future work : can you add a switch so someone can easily get the minimum value
# if they want?

# can you support the division operator?

# dump out the expression with the parantheses added? (reconstruction)