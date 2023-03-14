# Open a file explorer window to select input file
from tkinter import filedialog as fd
input_file = fd.askopenfile()

# initialise empty list and timeout counter
d_times = []
timeout_counter = 0
# create output file name by replacing ".extension" with "_processed.extension"
output_file = input_file.name.replace(".","_processed.")
# create the destination file, or overwrite empty if it already exists
with open(output_file, "w"):
    pass

# open the input file in read only mode
with open(input_file.name, "r") as src:
    # iterate through lines in source file
    for line in src:
        # check if phrase in line
        if "function_name" in line:
            # if yes:
            # check if "Start" in line
            if "Start" in line:
                # get start time
                start = line.split()
                start_time = int( start[0] )
                print(start_time)
            # check if "End" in line
            elif "End" in line:
                # get end time
                end = line.split()
                end_time = int( end[0] )
                print(end_time)
                # calculate delta time in seconds
                delta_time = ( end_time - start_time ) / 10_000
                d_times.append(delta_time)
                # increment timeout counter
                if delta_time >= 1:
                    timeout_counter += 1
                # format line to include delta time
                line = f"{line.rstrip()}    {delta_time:.4f}\n"    
            # append line to destination file
            with open(output_file, "a+") as dst:
                dst.write(line)

# calculate stats
min_time = min(d_times) 
max_time = max(d_times)
avg_time = sum(d_times) / len(d_times)

# write stats to end of file
with open(output_file, "a") as dst:
    dst.write(f"\nMin: {min_time:.4f}\n")
    dst.write(f"Max: {max_time:.4f}\n")
    dst.write(f"Avg: {avg_time:.4f}\n")
    dst.write(f"Timeouts: {timeout_counter}")
               
print("Done")

# Converts

# ...
#  10873425 line
#  10873426 line
#  10873432 function_name Start
#  10875543 line
#  10875544 line
#  10875559 function_name End
#  10875560 line
#  10875561 line
#  10875562 line
#  10875572 line
# ...

# -->

# ...
#  10873432 function_name Start
#  10875559 function_name    0.2127
# ...

# CR 2023-03-14