import csv

# Open the input CSV file
with open('aha-music-export.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    next(csv_reader)
    
    # Open the output text file
    with open('output.txt', 'w') as out_file:
        # Iterate over each row in the CSV
        for row in csv_reader:
            # Extract the title and artist columns
            title = row[1]
            artist = row[2]
            
            # Write the "title - artist" format to the output file
            out_file.write(f"{title} - {artist}\n")

print("Output file 'output.txt' generated successfully.")