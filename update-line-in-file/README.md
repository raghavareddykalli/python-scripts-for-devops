## Below Python script finds a line with a specific key in a file and changes its value, leaving all other lines unchanged.

Here’s a simple and detailed explanation of the code:

What does this code do?

- Purpose:
  This code updates a specific setting (key) in a configuration file. For example, if you want to change the value of MAX_CONNECTIONS in a file called server.conf, this code will do that for you.

### Step-by-step explanation

1. **Define a function:**
  The function "file_update" takes three inputs:
  - file_path: The path to the file you want to update (e.g., './server.conf')
  - key: The setting you want to change (e.g., 'MAX_CONNECTIONS')
  - value: The new value you want to set (e.g., '1000')
    
2. **Read the file:**
    The code opens the file in read mode ('r') and reads all lines into a list called lines.

3. **Write back to the file:**
   The code opens the same file in write mode ('w'), which means it will overwrite the file.
   It goes through each line in the file:
   - If the line contains the key you want to update (e.g., 'MAX_CONNECTIONS'), it writes a new line with the updated value (e.g., MAX_CONNECTIONS = 1000).
   - If the line does not contain the key, it writes the line back as it was.
  
4. **Call the function:**
   The last line calls the function to update MAX_CONNECTIONS to 1000 in the file server.conf.

## Summary:
This script finds a line with a specific key in a file and changes its value, leaving all other lines unchanged.
    
