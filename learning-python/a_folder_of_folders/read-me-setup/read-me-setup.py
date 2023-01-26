#100 days of code readME maker

# with open("text.txt","w") as file:
#     pass

# with open("text.txt","a") as file:
#     file.write("#100DaysOfCode | https://www.100daysofcode.com/ \n\n")
#     file.write("Started: 2022-11-21 | Optimal End: 2023-03-01 | Actual End: ___ \n\n")
#     file.write("corey-richardson | linktr.ee/coreyrichardson \n\n")
#     file.write("----\n\n")
#     for number in range(100):
#         file.write(f"### Day {number+1}: \n\n")
#         file.write("**Today's Tasks and Progress:**\n\n")
#         file.write("**About:**\n\n")
#         file.write("**Links:** []()\n\n")
#         file.write("\n\n\n")
#     print("done")
    
# ChatGPT Suggestion for better efficiency:

#100 days of code readME maker

template = "#100DaysOfCode | https://www.100daysofcode.com/ \n\nStarted: 2022-11-21 | Optimal End: 2023-03-01 | Actual End: ___ \n\ncorey-richardson | linktr.ee/coreyrichardson \n\n----\n\n"

with open("text.txt","w") as file:
    pass

with open("text.txt","a") as file:
    file.write(template)
    for number in range(100):
        file.write(f"### Day {number+1}: \n\n**Today's Tasks and Progress:**\n\n**About:**\n\n**Links:** []()\n\n\n\n\n")
    print("done")
