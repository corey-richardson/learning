guests = {}
def read_guestlist(file_name):
    text_file = open(file_name,'r')
    while True:
        n = yield
        if n == None:
          line_data = text_file.readline().strip().split(",")
        else: # is not none
          line_data = n.split(",")
        if len(line_data) < 2:
          # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        age = int(line_data[1])
        guests[name] = age
        yield name
        
guest_list = read_guestlist("guest_list.txt")

for guest in range(10):
  next(guest_list)
  print(next(guest_list))

next(guest_list)
guest_list.send("Jane, 35")

for guest in range(8):
  next(guest_list)

over_21 = (name for name in guests if guests[name] >= 21)

def table1_generator():
  for i in range(1, 6):
    yield "Chicken", "Table 1", "Seat {}".format(i)
def table2_generator():
  for i in range(1, 6):
    yield "Beef", "Table 2", "Seat {}".format(i)
def table3_generator():
  for i in range(1, 6):
    yield "Fish", "Table 3", "Seat {}".format(i)
table1 = table1_generator()
table2 = table2_generator()
table3 = table3_generator()

def assign_table_generator(guests):
  for guest in guests:
    guest_code = list(guests.keys()).index(guest) + 1
    if guest_code <= 5:
      yield (guest, next(table1))
    elif guest_code <= 10:
      yield (guest, next(table2))
    else:
      yield (guest, next(table3))
table = assign_table_generator(guests)