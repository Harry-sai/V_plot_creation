### Instructions for the Program

1. **Manipulate the Data Using Linux Commands:**
   - Use a Linux command to manipulate the original data file and extract the required information.
   - Save the processed data into a new file for further analysis.

2. **Plot the Data Using a Python Program:**
   - Use a Python script (e.g., `program.py`) to create a visualization of the processed data.
   - I used `matplotlib` library to generate the plot, with the new file from the previous step being read and used as the input.

3. **Automate the Process with a Script:**
   - Create a script file (`trans_script.sh`) that includes all the necessary commands to run the entire process on the file `mapped.bed.gz`.
   - This script automates the data manipulation, plotting, and any other required steps, allowing everything to be executed in one go.

### How to Run the Program

1. **Make the Script Executable:**
   - Use the following command to give execute permissions to `trans_script.sh`:
     ```
     chmod +x trans_script.sh
     ```

2. **Run the Script:**
   - Execute the script with the following command:
     ```
     sh trans_script.sh
     ```
   - This will run all the steps in sequence, and the results will be displayed.

