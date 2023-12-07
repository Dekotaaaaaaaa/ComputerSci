#Homework 7


#Discussion Question 1 (pg. 278)


#The difference between these the two are that a indefinite loop is implemented using a while statement and a definite loop is 

#Discussion Question 2 (all sub-problems) (pg. 278/279)

#Discussion Question 3 (a,c) (pg. 279)

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
