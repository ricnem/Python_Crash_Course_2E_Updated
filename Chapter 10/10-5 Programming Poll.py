filename = 'reasons.txt'

prompt = "(Type 'quit' and press enter when finished.)\n"
prompt += "Why do you like programming? "

with open(filename, 'w') as f:

    while True:
        reason = input(prompt)

        if reason == 'quit':
            print("Thank you for your feedback!\n")
            break
        else:
            print("--->Recording your answer inside the reasons.txt file...\n")
            f.write(f"{reason}\n")