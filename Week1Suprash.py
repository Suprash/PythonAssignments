#Question 1
a = float (input("Enter a number(can be float):"))

b = int(a)
c = str(a)

print("Output:")

print("Original Input:")
print(a)
print("Converted to int:")
print(b)
print("Converted to string:")
print(c)


###############################################################
#Question 2
a = input("Tell me your full name")
b = 0

for i in range(len(a)):
    if a[i] == " ":
        b = i


print(b)
initials = a[0].upper() + "." + a[b+1].upper()
print("Your Initials are:")
print(initials)


########################################################
#Question 3

a = input("String from you:")
stringa = a[len(a)::-1] #len(a) gives the lenght and goes from backwards :: -1
print(stringa)

#######################################
#Question 4
word = input("enter a word")
index = int(input("give me an index"))

sanoword = word[index:len(word)]
print(sanoword)

################################################
#Question 5
# Asks the user to enter an email address.
# Extracts the domain name (part after @) using string slicing.
# Prints the extracted domain.

email = input("enter your email address:")

for i in range(len(email)):
    if email[i] == "@":
        b = i+1

print("Domain: ")
print(email[b:len(email)])

################################################################
#Question 6

# Takes a word as input.
# Swaps its first and last character using string slicing.
# Displays the new word.

word = input("Input:")

middle_part = word[1:(len(word)-1)]

final = word[len(word)-1] + middle_part + word[0]

print(final)


