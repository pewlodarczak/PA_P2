'''
height = 5

1
3
5
7

   *
  ***
 *****
*******
   *
'''


def buildTree(height):
    i = 0
    while i < height:
        print('*')
        i += 1


height = input("Enter hight: ")
height = int(height)
buildTree(height)