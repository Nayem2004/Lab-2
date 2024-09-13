#Lab 2

import random

def has_shared_birthday(birthdays):
    #Returns True if two birthdays in the list are the same, False otherwise.
    return len(birthdays) != len(set(birthdays))

def simulate_birthday_experiment(n, trials):
    #Simulates the birthday paradox for n people over a number of trials.
    shared_birthday_count = 0
    
    for i in range(trials):
        # Generates random birthdays for n people (days between 1 and 365)
        birthdays = [random.randint(1, 365) for i in range(n)]
        if has_shared_birthday(birthdays):
            shared_birthday_count += 1
            
    # Returns the probability of shared birthdays.
    return shared_birthday_count / trials

def main():
    #Main function to test the birthday paradox for different values of n.
    trials = 10000  # Number of experiments to run for each variable.
    results = []  # Stores results to write it to a file.

    # Headers for the output.
    header = f"n\tProbability of Shared Birthday\n" + "="*35 + "\n"
    print(header)
    results.append(header)

    for n in range(5, 51, 5):
        probability = simulate_birthday_experiment(n, trials)
        result = f"{n}\t{probability:.4f}\n"
        print(result.strip())
        results.append(result)
    
    # Writes the results to a text file.
    with open("birthday_paradox_results.txt", "w") as file:
        file.writelines(results)

# Runs the main function.
main()
