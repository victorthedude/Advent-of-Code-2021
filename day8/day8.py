ONE_LEN = { 1 : 2}
FOUR_LEN = { 4 : 4}
SEVEN_LEN = { 7 : 3 }
EIGHT_LEN = { 8 : 7 }

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
    mappings.update({ key : filter(lambda i: len(i) == u_dict.get(key), input_line)[0] })
    input_line.remove(mappings.get(key))

    
    # 9 must contain 4 and 7's signals
  signals = set(char for char in mappings.get(4) + mappings.get(7))
  mappings.update({ 9 : filter(lambda i: contain_signals(i, signals), input_line)[0] })
  input_line.remove(mappings.get(9))

    # 0 must contain 7's signals (0 => len == 6)
    # 3 must contain 7's signals (3 => len == 5)
  signals = set(char for char in mappings.get(7))
  zero_and_three = list(filter(lambda i: contain_signals(i, signals), input_line))
  mappings.update({ 0 : filter(lambda i: len(i) == 6, zero_and_three)[0] })
  mappings.update({ 3 : filter(lambda i: len(i) == 5, zero_and_three)[0] })
  input_line.remove(mappings.get(0))
  input_line.remove(mappings.get(3))
    
    # 6 must have length length 6 of remaining
  mappings.update({ 6 : filter(lambda i: len(i) == 6, input_line)[0] })
  input_line.remove(mappings.get(6))

    # 2 must contain 2 of 4's signals
    # 5 must contain 3 of 4's signals
  signals = set(char for char in mappings.get(4))
  mappings.update({ 2 : filter(lambda i: 2 == count_signals(i, signals), input_line)[0] })
  mappings.update({ 5 : filter(lambda i: 3 == count_signals(i, signals), input_line)[0] })

  inv_map = {v: k for k, v in mappings.items()}
  return inv_map

with open("day8/input.txt", 'r') as file:
  outputs = []
  signal_patterns = []
  for line in file:
    split = line.split("|")
    signal_patterns.append(filter(lambda i: i != "", split[0].strip("\n").split(" ")))
    outputs.append(filter(lambda i: i != "", split[1].strip("\n").split(" ")))

  uniques = [ONE_LEN, FOUR_LEN, SEVEN_LEN, EIGHT_LEN]
  u_dict = {}
  for unique in uniques:
    u_dict.update(unique)

  # part 1:
  occurences = 0
  for l in outputs:
    for output in l:
      if len(output) in u_dict.values():
        occurences += 1
  
  
  #print(occurences)

  # part 2: 
  result = 0
  for i in range(len(signal_patterns)):
    inputs_list = signal_patterns[i]
    outputs_list = outputs[i]
    #print(outputs_list)
    mappings = determine_mappings(inputs_list, u_dict)
    #print(mappings)
    correct_output = ""
    for output in outputs_list:
      for key in mappings:
        if sorted(key) == sorted(output):
          correct_output = correct_output + str(mappings.get(key))
    #print(correct_output)
    result = result + int(correct_output)
    
  print(result)
  #test_line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
  #input_line = list(filter(lambda i: i != "", test_line.split("|")[0].strip("\n").split(" ")))
  #output_line = list(filter(lambda i: i != "", test_line.split("|")[1].strip("\n").split(" ")))
  