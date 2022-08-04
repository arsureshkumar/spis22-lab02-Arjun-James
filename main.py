# The goal of this program is to practice Python constructs

def getNumber():
  
  number = 0
  symbols = "0"
  while (int(symbols) >= 0 ):
    number = number*10 + int(symbols)
    symbols = input("Enter a digit: ")
  return number



def sumTwo(a,b):

   c = a + b
   return c


def sumDigits(x):

  sum = 0
  while (x > 0):
    sum = sum + (x % 10)
    x = int(x/10)

  return sum

#takes in wageGap as a parameter to account for different wageGaps in different places
def convertWageMtoW(mWage, wageGap):

  if (wageGap > 0):
    ratio = 1 - wageGap

    return mWage * ratio





#x = sumTwo(3,5)
#print(x)

#y = getNumber()
#print(y)

#z = sumDigits(5798)
#print(z)

#b = convertWageMtoW(100, 0.182)
#print(b)
#a = convertWageMtoW(76.2, 0.182)
#print(a)
#c = convertWageMtoW(0, 0.182)
#print(c)


def wordGuess(word):
  end = 0
  while (end < 7 and len(word) > 0):
    char = input('Enter a character: ')
    if(char in word):
      print(char, 'is located at', word.index(char))
      word = word[:word.index(char)] + word[(word.index(char)+1):]
    else:
      print("This character is not in the word!")
      end += 1
  print("Game Over!")


wordGuess('hello')