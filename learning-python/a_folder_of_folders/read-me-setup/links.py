# links
with open("links.txt","w") as file:
    pass

for i in range(100):
    if not (i+1) %10:
        print(i, True)
        url = "https://github.com/corey-richardson/100DaysOfCode/blob/main/README.md#day-"
        dated_url = url + str(i+1)
        full = f"[day-{i+1}]({dated_url})"
        with open("links.txt","a") as file:
            file.write(full + " ")
    else: print(i)
