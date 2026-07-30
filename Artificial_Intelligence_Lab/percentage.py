# Input marks of 5 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

# Calculate total marks
total = sub1 + sub2 + sub3 + sub4 + sub5

# Calculate percentage (assuming each subject is out of 100)
percentage = (total / 500) * 100

# Display results
print("\nTotal Marks =", total)
print("Percentage = {:.2f}%".format(percentage))