#importing regular expressions to find text patterns
import re

#importing os to enable interaction with the file system 
import os

#for handling tabular data and exporting tsv
import pandas as pd



#function that writes a list of data rows into a tsv file using pandas 
def write_tsv(rows, column_list, path):
   
    #convert the list of rows into pandas DataFrame
    df = pd.DataFrame(rows, columns=column_list)
    
    # write the dataframe to tsv:
    df.to_csv(path, sep="\t", index=False)



# Defining the folder where the articles are present
# these articles are text files to search for place names 
folder = r"C:\Users\Dell\Downloads\FASDH25-portfolio2\articles"  


#  define the path and load the gazetteer from the tsv file, having place names and alternate names 
path = r"C:\Users\Dell\Downloads\FASDH25-portfolio2\gazetteers\geonames_gaza_selection.tsv"
#open and read the file
with open(path, encoding="utf-8") as file:
    data = file.read()

# Create an empty dictionary to store regex patterns for each place and how many times they appear
patterns = {}

# Split the gazetteer data 
rows = data.split("\n")

# Skip the header row and process each remaining row one by one
for row in rows[1:]:
    # Split the current row into its columns (TSV = tab-separated values)
    columns = row.split("\t")

    # If a row doesn't have at least 6 columns, skip it (incomplete data)
    if len(columns) < 6:
        continue

    # The first column contains the main place name (asciiname)
    asciiname = columns[0]

    # Create a list to store this place's name and its alternate versions
    name_variants = [asciiname]

    # The 6th column (index 5) contains alternate names, separated by commas
    alternate_names = columns[5].strip()
    #.strip() removes spaces, tabs, and newlines from the start and end of a string (help from chatgpt-solution 1)

    # Check if there are any alternate names listed
    if alternate_names:
        # Split the alternate names by comma into a list
        alternate_list = alternate_names.split(",")

        # Go through each alternate name
        for alternate in alternate_list:
            # Remove any extra spaces around the alternate name
            alternate = alternate.strip()

            # If the cleaned alternate name isn't empty, add it to the list of variants
            if alternate:
                name_variants.append(alternate)

    # Use re.escape() to safely handle special characters in each name variant for regex
    name_variants = [re.escape(name) for name in name_variants]

    # Create a regex pattern that matches any of the name variants
    # \b makes sure we match whole words (e.g., 'Gaza' won't match 'Magazine')
    regex_pattern = r"\b(" + "|".join(name_variants) + r")\b"

    # Save this pattern and start the match count at 0 in the patterns dictionary
    patterns[asciiname] = {"pattern": regex_pattern, "count": 0}


    


# This dictionary stores how many times each place name was mentioned per month
mentions_per_month = {}

# Setting the starting date of the war in Gaza to filter articles
war_start_date = "2023-10-07"

# Loop through each file in the folder to count the number of times each place is mentioned
#code from https://docs.google.com/presentation/d/15iXoENGlvyKovNr4ttU7ZFDbrTlOa1q6iELK5f8S4Vk/edit#slide=id.g34ba5dcdc27_0_150
for filename in os.listdir(folder): #gives a list of all the files and folders inside the folder
    
    # Extract the date from the filename (the format is YYYY-MM-DD_)
    date_str = filename.split("_")[0]
    
    # Skip the file if it was written before the start of the war
    if date_str < war_start_date:
        continue

    # Build the file path to the current article
    # solution from presentation https://docs.google.com/presentation/d/1FpKUbGhJtu6TW-4MVI2xje8N-6DNaDSP6kVPKvqz0T4/edit#slide=id.g343a22a7e4a_1_203
    file_path = os.path.join(folder, filename)
    
    # Open and read the article
    with open(file_path, encoding="utf-8") as file:
        text = file.read() #reads content of file

    # Loop through each place to search for matches in the text
    for place in patterns:
        pattern = patterns[place]["pattern"]  # Get regex-safe pattern
        matches = re.findall(pattern, text, re.IGNORECASE)  # Find all mentions of the place
        count = len(matches)  # Count nuber of times the plave is mentioned 
        
        # Add the number of times the place is found to the total frequency
        patterns[place]["count"] += count
        
        # Extract the month from the date string (YYYY-MM) 
        month_str = date_str[:7]
        
        # Initialize place and month in mentions_per_month if not already done
        if place not in mentions_per_month:
            mentions_per_month[place] = {}
        
        # Check if the month is already in the dictionary for this place
        if month_str not in mentions_per_month[place]:
            # If not, initialize the month with count 0
            mentions_per_month[place][month_str] = 0
        
        # Add the new count to the number of times the place was mentioned that month
        mentions_per_month[place][month_str] += count

# # Show the complete data of monthly mention counts for every place
for place in mentions_per_month:
    print(f'"{place}": {{')
    
    # Find and list every month the place was referenced
    month_list = list(mentions_per_month[place].keys())
    
    # Loop through all months and print how often each appears
    for month in month_list:
        count = mentions_per_month[place][month]  # Get the count for the month
        
        # Print each month and its count, with commas separating entries . took help from classmates 
        if month != month_list[-1]: #refers to the last element in the list
            print(f'    "{month}": {count},')
        else:
            print(f'    "{month}": {count}')
    
    print("},")

# Convert the mentions_per_month dictionary to a list of rows for export (e.g., CSV format)
rows = []

# Loop through each place again to prepare structured data for export. help taken from ma'am amna and chat gtp-solution 2
for place in mentions_per_month:
    for month in mentions_per_month[place]:
        count = mentions_per_month[place][month]
        if count > 0:
            # Append the tuple (place, month, count) to the rows list
            rows.append((place, month, count))
#Write the final tsv file        
write_tsv(rows, ["placename","month", "count"], "regex_counts.tsv")        
