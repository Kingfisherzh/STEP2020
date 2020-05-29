def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
    while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index


def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1


def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1


def readMultiply(line, index):
  token = {'type': 'MULTIPLY'}
  return token, index + 1


def readDivide(line, index):
  token = {'type': 'DIVIDE'}
  return token, index + 1


def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
    if line[index].isdigit():
      (token, index) = readNumber(line, index)
    elif line[index] == '+':
      (token, index) = readPlus(line, index)
    elif line[index] == '-':
      (token, index) = readMinus(line, index)
    elif line[index] == '*':
      (token, index) = readMultiply(line, index)
    elif line[index] == '/':
      (token, index) = readDivide(line, index)  
    else:
      print('Invalid character found: ' + line[index])
      exit(1)
    tokens.append(token)
  return tokens


def evaluate(tokens):
  answer = 0
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  second_tokens = []
  index = 1

  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS':
        second_tokens.append({'type': 'NUMBER', 'number': answer})
        second_tokens.append({'type': 'PLUS'})
        answer = tokens[index]['number']
      elif tokens[index - 1]['type'] == 'MINUS':
        second_tokens.append({'type': 'NUMBER', 'number': answer})
        second_tokens.append({'type': 'MINUS'})
        answer = tokens[index]['number']
      elif tokens[index - 1]['type'] == 'MULTIPLY':
        answer *= tokens[index]['number']
      elif tokens[index - 1]['type'] == 'DIVIDE':
        answer /= tokens[index]['number']
      else:
        print('Invalid syntax')
        exit(1)
    index += 1
  if second_tokens:
    #print(second_tokens)
    # Add the last number into the tokens
    second_tokens.append({'type': 'NUMBER', 'number': answer})
    answer = second_evaluate(second_tokens) 
  return answer


def second_evaluate(tokens):
  answer = 0
  index = 1
  while index < len(tokens):
    if tokens[index]['type'] == 'NUMBER':
      if tokens[index - 1]['type'] == 'PLUS':
       answer += tokens[index]['number']
      elif tokens[index - 1]['type'] == 'MINUS':
       answer -= tokens[index]['number']
    index += 1
  return answer


def test(line):
  tokens = tokenize(line)
  actualAnswer = evaluate(tokens)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
    print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
    print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
  print("==== Test started! ====")
  test("1+2")
  test("1.0+2.1-3")
  test("5+90/3+2-5")
  test("3/2*1.5")
  test("0.50*1.0/1/20")
  test("-9/3*2.5/0.2")
  print("==== Test finished! ====\n")

runTest()

while True:
  print('> ', end="")
  line = input()
  tokens = tokenize(line)
  answer = evaluate(tokens)
  print("answer = %f\n" % answer)
