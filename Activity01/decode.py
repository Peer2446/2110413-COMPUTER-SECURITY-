import hashlib
import time

# Generate all possible combinations of a password
def generate_password_combinations(password):
    passwords = []
    
    # Helper function to generate all possible combinations of a password
    def helper(passwords, password, index=0, current_combination=''):
        if index == len(password):
            passwords.append(current_combination)
            return

        char = password[index]
        helper(passwords, password, index + 1, current_combination + char.lower())
        helper(passwords, password, index + 1, current_combination + char.upper())

        char_to_number = {'o': '0', 'i': '1', 'l': '1'}
        if char.lower() in char_to_number:
            helper(passwords, password, index + 1, current_combination + char_to_number[char.lower()])

    helper(passwords, password)
    return passwords

# Decode the password using the 10k most common passwords
def decode_password(passwordHash, passwords):
    for p in passwords:
        combinations = generate_password_combinations(p.strip())
        for c in combinations:
            if hashlib.sha1(c.encode()).hexdigest() == passwordHash:
                return c
    return ''

# Generate a rainbow table using the 10k most common passwords
def generateRainbowTable(passwords):
    rainbowTable = {}
    for p in passwords:
        combinations = generate_password_combinations(p.strip())
        for c in combinations:
            rainbowTable[c] = hashlib.sha1(c.encode()).hexdigest()
    return rainbowTable

# Read the 10k most common passwords
try:
    with open('/Users/peeralis/Documents/Computer Security/Activity01/10k-most-common.txt', 'r') as passwordFile:
        passwordList = passwordFile.readlines()
except FileNotFoundError:
    print("Password file not found.")
    exit(1)

#1
print('#1', decode_password('d54cc1fe76f5186380a0939d2fc1723c44e8a5f7', passwordList))

#2
start = time.time()
rainbowTable = generateRainbowTable(passwordList)
end = time.time()
print('#2 Time taken:', end - start)
print('#2 Table size:', len(rainbowTable))
# print(tabulate(rainbowTable.items(), headers=['Password', 'Hash'], tablefmt='grid'))

#3
password = "password"
startTime = time.time()
hashValue = hashlib.sha1(password.encode()).hexdigest()
endTime = time.time()

timeTaken = endTime - startTime
print("#3 Time taken for a single SHA-1 hash:", timeTaken)

#4 assume that the password is 7 characters long and contains only letters and digits
# time to generate all possible combinations 36^7(26 from a-z, 10 from 0-9)
totalCombinations = 36**7
timeToGenerate = totalCombinations * timeTaken
print(f'#4 Time to generate all possible combinations: {timeToGenerate} seconds / {timeToGenerate/3600} hours / {timeToGenerate/3600/24} days')

#5
passwordLength = 1
while True:
    totalCombinations = 36**passwordLength
    timeToGenerate = totalCombinations * timeTaken
    # if time to generate is more than 1 year, break
    if timeToGenerate > 365*24*3600:
        print(f'#5 Time to generate all possible combinations for a {passwordLength}-character password: {timeToGenerate/3600} hours / {timeToGenerate/3600/24} days')
        print(f'#5 The proper length of the password is {passwordLength} (need more than 1 year to break)')
        break
    passwordLength += 1

# 6. Explanation of salt
print("#6 Salt explanation: Salt is a random string added to the password before hashing. It protects against precomputed hash attacks (rainbow tables).")
