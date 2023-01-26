message = "The quick brown fox jumps over the lazy dog."
message = message.lower()

alphabet_count = {}


alphabet = "abcdefghijklmnopqrstuvwxyz0123456789.,!? "
for letter in alphabet:
    alphabet_count[letter] = 0

input_file = "textfile.txt"
with open(input_file,"r") as message: 
    for line in message: 
        for char in line.lower():
            if char in alphabet_count:
                alphabet_count[char] += 1
            else:
                alphabet_count[char] = 1
        
# print(alphabet_count)

for key in alphabet_count:
    print(f"{key} : {alphabet_count[key]}")


