'''
height = 5

4 2
5 3
6 4

   *
  ***
 *****
*******
   *
'''

def buildTree(height):
   if height < 4:
      print('Height has to be at least 4')
      return
   i = 0
   spaces = height - 2
   tmpSpc = spaces
   stars = 0
   tmpStrs = stars
   while i < height:
      line = ''
      indx = 0
      # numBlanks = height - 2
      numStars = 1
      while spaces > 0:
         line += ' '
         spaces -= 1
      while stars < tmpStrs + 1:
         stars += 1
      
      tmpStrs = stars
      stars += 1
      #print('stars ' + str(stars))
      #print('tmpstars ' + str(tmpStrs))
      indx += 1
      tmpSpc -= 1
      spaces = tmpSpc
      line += '*'
      print(line)
      i += 1

height = input("Enter hight: ")
print()
height = int(height)
buildTree(height)