
def printChart(chart, rang):
  print()
  for i in range(rang): 
    for j in range(rang): 
      print(chart[i][j]," ", end="")
    print()

def check_full_horozontal(chart, rang):  
  for i in range(rang): 
    x_num = 0
    o_num = 0
    
    for j in range(rang): 
      if(chart[i][j] == "x"):
        x_num = x_num + 1
      if(chart[i][j] == "o"):
        o_num = o_num + 1
        
    if(x_num == rang):
        return 1
    elif(o_num == rang):
        return 2
      
  return 0
    
def check_full_vertical(chart, rang):
  for i in range(rang): 
    x_num = 0
    o_num = 0
    
    for j in range(rang): 
      if(chart[j][i] == "x"):
        x_num = x_num + 1
      if(chart[j][i] == "o"):
        o_num = o_num + 1
        
    if(x_num == rang):
        return 1
    elif(o_num == rang):
        return 2
      
  return 0
    
def check_full_angle(chart, rang):
  x_num = 0
  o_num = 0
  
  for i in range(rang):
    # print(chart[i][i], " ", i, " ", i)
    if(chart[i][i] == 'x'):
      x_num += 1
    elif(chart[i][i] == 'o'):
      o_num += 1

  if(x_num == rang):
    return 1
  elif(o_num == rang):
    return 2
    
  x_num = 0
  o_num = 0
  j = rang
  for i in range(rang):
    j -= 1
    if(chart[i][j] == 'x'):
      x_num += 1
    elif(chart[i][j] == 'o'):
      o_num += 1
  
  if(x_num == rang):
    return 1
  elif(o_num == rang):
    return 2
  else:
    return 0



def addLetter(grid, turn, rang):
  open = 1
  while(open == 1):
    if(turn == 1):
      print()
      row = int(input("Enter the row position you would like to change for X : "))
      col = int(input("Enter the column position you would like to change for X : "))
      
      if((row > rang-1) | (row < 0) | (col > rang-1) | (col < 0)):
        print()
        print("Invalid number try again... ")
        print()
        continue
        
      if(grid[row][col] != '-'):
        open = 1
        print()
        print("There is something in that spot try again...")
        print()
        continue
      elif(grid[row][col] == '-'):
        grid[row][col] = "x"
        open = 2
        return grid
      
    elif(grid, turn):
      print()
      row = int(input("Enter the row position you would like to change for O : "))
      col = int(input("Enter the column position you would like to change for O : "))
      
      if((row > rang-1) | (row < 0) | (col > rang-1) | (col < 0)):
        print()
        print("Invalid number try again... ")
        print()
        continue

      if(grid[row][col] != '-'):
        open = 1
        print()
        print("There is something in that spot try again...")
        print()
        continue
      elif(grid[row][col] == '-'):
        grid[row][col] = "o"
        open = 2
        return grid



def CheckWin(charter, rang):
  if((check_full_angle(charter, rang) == 1) | (check_full_vertical(charter, rang) == 1) | (check_full_horozontal(charter, rang) == 1)):
    return 1
  elif((check_full_angle(charter, rang) == 2 )| (check_full_vertical(charter, rang) == 2 )| (check_full_horozontal(charter, rang) == 2)):
    return 2
  else:
    return 0

    
### Start Main
print("Welcome to TicTacToe", end="\n")
rane = 0

while(rane < 2):
  rane = int(input("What size do you want your board, >= 3 : "))

chart = [['-' for j in range(rane)] for i in range(rane)]
# printChart(chart, rane) ##

print()
print("Row and Column are positions 0-%s... Enjoy!"%(rane-1), end="")
cont = 1


while(cont == 1):
  chart = [['-' for j in range(rane)] for i in range(rane)]
  
  printChart(chart, rane)
  winner = 0
  cont = 1

  while(winner == 0):
    chart = addLetter(chart, 1, rane)
    printChart(chart, rane)
  
    if(CheckWin(chart, rane) != 0):
      if(CheckWin(chart, rane) == 2):
        print("o wins!")
        break
      elif(CheckWin(chart, rane) == 1):
        print("x wins!")
        break
    
    chart = addLetter(chart, 2, rane)
    printChart(chart, rane)
  
    if(CheckWin(chart, rane) != 0):
      if(CheckWin(chart, rane) == 2):
        print("o wins!")
        break
      elif(CheckWin(chart, rane) == 1):
        print("x wins!")
        break

  print()
  print("Would you like to play again?")
  cont = int(input("Please type 1 for Yes and anything else for No. "))
  print()



  
