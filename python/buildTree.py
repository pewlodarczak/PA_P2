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
    starLine = ''
    while i < height - 1:
        line = ''
        while spaces > 0:
            line += ' '
            spaces -= 1

        tmpSpc -= 1
        spaces = tmpSpc
        line += '*'
        line += starLine
        starLine += '**'
        print(line)
        i += 1
    
    line = ''
    spaces = height - 2
    while spaces > 0:
        line += ' '
        spaces -= 1
    line += '*'
    print(line)

height = input("Enter hight: ")
print()
height = int(height)
buildTree(height)