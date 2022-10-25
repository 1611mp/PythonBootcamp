# Lucky , odd and even

# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f"{num} is unlucky.")
#     elif num % 2 == 1:
#         print(f"{num} is odd.")
#     else:
#         print(f"{num} is even.")


# Lucky , odd and even

for num in range(1,51):
    if num == 13 or num == 27:
        state = "unlucky"

    elif num % 2 == 1:
        state = "odd"

    else:
        state = "even"
    print(f"{num} is {state}.")
