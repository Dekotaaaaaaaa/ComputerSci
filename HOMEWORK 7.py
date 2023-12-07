#Homework 7


#Discussion Question 1 (pg. 278)
#a The difference between these two are that definite loop it runs for a certian amount of times and indefinite loop runs until it is no longer true
#b The while loop runs until a condition is false, and for loop is a definite loop that runs for however many times you want
#c The difference is  interactive loops rely on user input, while sentinel loops use a predetermined condition to determine when to stop iterating.
#d sentinel loop uses a designated value within the input data, while an End of file loop relies on the natural end-of-file indication in the input stream.



#Discussion Question 3 (a,c) (pg. 279)
#a

n = 10  sum_of_numbers = 0
current_number = 1

while current_number <= n:
    sum_of_numbers += current_number
    current_number += 1

print("The sum of the first", n, "counting numbers is:", sum_of_numbers)

#c
sum_of_numbers = 0
number = float(input("Enter a number (enter 999 to stop): "))

while number != 999:
    sum_of_numbers += number
    number = float(input("Enter a number (enter 999 to stop): "))

print("The sum of the entered numbers is:", sum_of_numbers)
#Programming Exercise 1 (pg. 279)
print( "P | Q| R | not (P and Q) | (not P) and Q | (not P) or (not Q)| (P and Q) or R | (P or R) and (Q or R)")
for P in [True, False]:
    for Q in [True, False]:
        for R in [True, False]:
            not_P_and_Q = not (P and Q)
            notP_and_Q = (not P) and Q
            notP_or_notQ = (not P) or (not Q)
            P_and_Q_or_R = (P and Q) or R
            P_or_R_and_Q_or_R = (P or R) and (Q or R)
print(f"{P}| {Q} | {R} | {not_P_and_Q} | {notP_and_Q}| {notP_or_notQ} | {P_and_Q_or_R} | P_or_R_and_Q_or_R")


#Programming Exercise 4 (pg. 280)

def syracuse_sequence(n):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    return sequence
try:
    starting_value = int(input("Starting value for the Syracuse sequence:"))

    if starting_value <= 0:
        print("Enter a positive integer as the startingvalue.")
    else:
sequence = syracuse_sequence(starting_value)
    print("Syracuse sequence for starting value", starting_value, ":", sequence)
except ValueError:
    print("Invalid input. Please enter a positive integer as the starting value.")
