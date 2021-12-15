def align_on_pos(input, align_pos):
  total_fuel_cost = 0
  for pos in input:
    total_fuel_cost = total_fuel_cost + abs(align_pos - pos)
  return total_fuel_cost

def day1(input):
  fuel_costs = {}
  for pos in set(input):
    fuel_costs.update({ pos : align_on_pos(input, pos)})

  #print(fuel_costs)
  print(min(fuel_costs.values()))

def align_on_pos_increasing_cost(input, align_pos):
  total_fuel_cost = 0
  for pos in input:
    total_fuel_cost = total_fuel_cost + sum(range(1, 1 + abs(align_pos - pos)))
  return total_fuel_cost

def day2(input):
  fuel_costs = {}
  for pos in range(max(input) + 1):
    fuel_costs.update({ pos : align_on_pos_increasing_cost(input, pos)})

  #print(fuel_costs)
  print(min(fuel_costs.values()))

if __name__ == "__main__":
  INPUT = "day7/input.txt"
  with open(INPUT, 'r') as file:
    input = [int(pos) for pos in file.readline().split(',')]
    #day1(input)
    day2(input)