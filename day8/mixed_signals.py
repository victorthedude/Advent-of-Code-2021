ONE_LEN = 2
FOUR_LEN = 4
SEVEN_LEN = 3
EIGHT_LEN = 7

def contain_signals(string, charset):
  for char in charset:
    if char not in string:
      return False
  return True

def count_signals(string, charset):
  i = 0
  for char in charset:
    if char in string:
      i = i + 1
  return i

def determine_mappings(input_line, u_dict):
  mappings = {}
  for key in u_dict:
    # mappings for 1, 4, 7, 8
    mappings.update({ key : next(filter(lambda i: len(i) == u_dict.get(key), input_line)) })
    input_line.remove(mappings.get(key))
    
  # 9 must contain 4 and 7's signals
  signals = set(char for char in mappings.get(4) + mappings.get(7))
  mappings.update({ 9 : next(filter(lambda i: contain_signals(i, signals), input_line)) })
  input_line.remove(mappings.get(9))

  # 0 must contain 7's signals (0 => len == 6)
  # 3 must contain 7's signals (3 => len == 5)
  signals = set(char for char in mappings.get(7))
  zero_and_three = list(filter(lambda i: contain_signals(i, signals), input_line))
  mappings.update({ 0 : next(filter(lambda i: len(i) == 6, zero_and_three)) })
  mappings.update({ 3 : next(filter(lambda i: len(i) == 5, zero_and_three)) })
  input_line.remove(mappings.get(0))
  input_line.remove(mappings.get(3))
    
  # 6 must have length length 6 of remaining
  mappings.update({ 6 : next(filter(lambda i: len(i) == 6, input_line)) })
  input_line.remove(mappings.get(6))

  # 2 must contain 2 of 4's signals
  # 5 must contain 3 of 4's signals
  signals = set(char for char in mappings.get(4))
  mappings.update({ 2 : next(filter(lambda i: 2 == count_signals(i, signals), input_line)) })
  mappings.update({ 5 : next(filter(lambda i: 3 == count_signals(i, signals), input_line)) })

  inv_map = {v: k for k, v in mappings.items()}
  return inv_map

#######

with open("day8/input.txt", 'r') as file:
  outputs = []
  signal_patterns = []
  for line in file:
    split = line.split("|")
    signal_patterns.append(list(filter(lambda i: i != "", split[0].strip("\n").split(" "))))
    outputs.append(list(filter(lambda i: i != "", split[1].strip("\n").split(" "))))

  uniques = { 
    1 : ONE_LEN,
    4 : FOUR_LEN,
    7 : SEVEN_LEN,
    8 : EIGHT_LEN
  }

  # part 1:
  occurences = 0
  for l in outputs:
    for output in l:
      if len(output) in uniques.values():
        occurences += 1
  
  #print(occurences)


  # part 2: 
  result = 0
  for i in range(len(signal_patterns)):
    inputs_list = signal_patterns[i]
    outputs_list = outputs[i]
    mappings = determine_mappings(inputs_list, uniques)
    digit_output = ""
    for output in outputs_list:
      for key in mappings:
        if sorted(key) == sorted(output):
          digit_output = digit_output + str(mappings.get(key))
    #print(digit_output)
    result = result + int(digit_output)
    
  print(result)
  