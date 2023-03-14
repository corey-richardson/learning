# Set the phrase to search for here
phrase = "function_name"

# Open a file explorer window to select input file
from tkinter import filedialog as fd
input_file = fd.askopenfile()

# Initialisation
d_times = []
timeout_counter = 0

# Generate output file name by replacing ".[extension]" with 
# "_processed.[extension]"
output_file = input_file.name.replace(".","_processed.")

# Create the destination file, or overwrite and empty if it already exists
# Then, add column headers
with open(output_file, "w") as dst:
    dst.write(" T                        T(s)       dT(s)  \n")

# This section could likely be in the other context manager for better resource
# management however I couldn't get that iterator to work :/
# Calculate total number of lines in file
# Could also be done with "len(src.readlines())" however this would load the
# entire file into memory; okay for small files but less okay for larger files.
with open(input_file.name, "r") as temp_src:
    total_lines = 0
    for ln in temp_src:
        total_lines += 1
        
# Open the input file in read only mode
with open(input_file.name, "r") as src:
    
    # Iterate through each line in source file
    # Enumerate creates a counter to be used in the progress output message
    for ln_num, line in enumerate(src):
        
        # Check if phrase in line
        if not phrase in line:
            continue # Early return when False prevents nesting:
        # "Very deep nesting or very long sections of code within the nested
        #  if statements raises questions about the design, readability, and
        #  maintainability of the code."
        # Probably could've got away with it here but nice to get into good
        # habits.
        
        # Progress bar:
        print(f"{ln_num} / {total_lines}")

        if "Start" in line:
            # Get start time
            start = line.split()
            start_time = int(start[0])
            num_length = len( start[0] ) # Used to calculate indent length
            # Format line to be written
            #        {line text    }   {start time in seconds, 4dp}
            line = f"{line.rstrip()}   {start_time/10_000     :.4f} \n"
            
        elif "End" in line:
            # Get end time
            end = line.split()
            end_time = int( end[0] )
            
            # Calculate change in time             in seconds
            delta_time = ( end_time - start_time ) / 10_000
            # Append this value to a list to be used for stats analysis
            d_times.append(delta_time)
            
            # Check if timeout counter should be incremented
            if delta_time >= 1:
                timeout_counter += 1
                
            # Format line to be written
            #        {line text    }     {end time, secs, 4dp}    {delta time, 4dp}
            line = f"{line.rstrip()}     {end_time/10_000:.4f}    {delta_time :.4f}\n"  
              
        # Append line to destination file
        with open(output_file, "a+") as dst:
            dst.write(line)

# Calculate stats
min_time = min(d_times) 
max_time = max(d_times)
avg_time = sum(d_times) / len(d_times)

# Write stats to end of file
# (Indented so you can open in Excel with "fixed width" delimiting)
indent = " " * (num_length + 2)
with open(output_file, "a") as dst:
    dst.write(f"\n{indent}Min: {min_time:.4f}\n")
    dst.write  (f"{indent}Max: {max_time:.4f}\n")
    dst.write  (f"{indent}Avg: {avg_time:.4f}\n")
    dst.write  (f"{indent}Timeouts: {timeout_counter}")
               
print("Done")


# Converts log output
# ...
#  215088 line
#  215090 line
#  215091 line
#  215097 function_name Start
#  215561 line
#  215562 line
#  215577 function_name End
#  215578 line
# ...
# Into more readable -->
# ...
#  T                            T(s)       dT(s)  
#  215097 function_name Start   21.5097
#  215577 function_name End     21.5577    0.0480
# ...
#         Min: 0.0479
#         Max: 1.0001
#         Avg: 0.1366
#         Timeouts: 1

# CR 2023-03-14