#!/usr/bin/env python

import sys, getopt
file1 = ''
file2 = ''

def main(argv):
   global file1
   global file2
   try:
      opts, args = getopt.getopt(argv,"h1:2:",["file1=","file2="])
   except getopt.GetoptError:
      print 'usage: compfollowers.py -1 <file1> -2 <file2>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'usage: compfollowers.py -1 <file1> -2 <file2>'
         sys.exit()
      elif opt in ("-1", "--file1"):
         file1 = arg
      elif opt in ("-2", "--file2"):
         file2 = arg

   if file1 == '' and file2 == '':
      print 'usage: compfollowers.py -1 <file1> -2 <file2>'
      sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])

# Read file into an array of lines
db_file = open(file1, "r")
dblines = db_file.readlines()
db_file.close()

# Read secondary file into an array of lines
go_file = open(file2, "r")
golines = go_file.readlines()
go_file.close()

# Initialize loop counters, etc.
x = 0
y = 0
match = 0

# Start loop of file1
while x < len(dblines):

	# Strip carriage return from the lines
	db_line = dblines[x].strip()
	x += 1

	# Start loop of file2
	while y < len(golines):
		go_line = golines[y].strip()
		
		# Check for a match and increase match count if found
		if db_line == go_line:
			match += 1

		y += 1
	
	# Reset loop counter for 2nd file
	# (we want to check the entire file each time)
	y = 0

# Output our result
print match