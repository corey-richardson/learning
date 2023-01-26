starts = [1,11,21,31,41,51,61,71,81,91]
ends =   [10,20,30,40,50,60,70,80,90,100]
values = list(zip(starts, ends))
print(values)

with open("links.txt","w") as links:
    pass

# https://github.com/corey-richardson/100-days-of-code/blob/main/day-{start}-{end}-log.md

for i, value in enumerate(values):
    start = values[i][0]
    end = values[i][1]
    print(start, end)
    name = f"day-{start}-{end}-log.md"

    with open(name,"w") as file:
        pass

    with open(name,"a") as file:
        for number in range(start,end+1):
            file.write(f"### Day {number}: \n\n")
            file.write("**Today's Tasks and Progress:**\n\n")
            file.write("**About:**\n\n")
            file.write("**Links:** []()\n\n")
            file.write("\n\n\n")
        print("done")

    with open("links.txt","a") as links:
        to_write = f" - [days-{start}-{end}-log](https://github.com/corey-richardson/100-days-of-code/blob/main/day-{start}-{end}-log.md)\n\n"
        links.write(to_write)
        