matrix=[]
def cap(spacesBefore,i):
	for j in range(spacesBefore+1):
		matrix[i][j]=' '
	for j in range(spacesBefore+1,spacesBefore+4):
		matrix[i][j]='.'
    #print( " " * spacesBefore + "...")

def wall(spacesBefore, spacesBetween,i):
	for j in range(spacesBefore+1):
		matrix[i][j]=' '
	matrix[i][spacesBefore+1]='.'
	for j in range(spacesBefore+2,spacesBefore+spacesBetween+2):
		matrix[i][j]=' '
	matrix[i][spacesBefore+spacesBetween+2]='.'

	
    #print( " " * spacesBefore + "." + " " * spacesBetween + ".")

def floor(spacesBefore, spacesBetween,i):
	for j in range(spacesBefore+1):
		matrix[i][j]=' '
	for j in range(spacesBefore+1,spacesBefore+4):
		matrix[i][j]='.'
	for j in range(spacesBefore+4,spacesBefore+spacesBetween+4):
		matrix[i][j]=' '
	for j in range(spacesBefore+spacesBetween+4,spacesBefore+spacesBetween+7):
		matrix[i][j]='.'

    #print( " " * spacesBefore + "..." + " " * spacesBetween + "...")
def draw(N):
	for x in range(0,50):
		matrix.append([])
		for y in range(0,50):
			matrix[x].append(' ')
	ct=0
	cap(2*N,ct)
	ct+=1
	for i in range(N):              #loop from 0 to N-1
		wall(2*(N-i), 1+(4*i),ct)
		ct+=1
		floor(2*(N-i-1), 1+(4*i),ct)
		ct+=1
	wall(0, 4*N+1,ct)
	ct+=1
	for i in range(N-1, -1, -1):    #loop from N-1 to 0
		floor(2*(N-i-1), 1+(4*i),ct)
		ct+=1
		wall(2*(N-i), 1+(4*i),ct)
		ct+=1
	cap(2*N,ct)
	print(matrix)
for i in range(7,8):
    draw(i)
    #print ("\n")