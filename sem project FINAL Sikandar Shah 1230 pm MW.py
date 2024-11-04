import csv # module imported to read and write CSV files
import random # module to generate randoms

def read_csv_file(file_name): #takes file name as the input file and reads it
    try:
        with open(file_name, 'r') as file: #opens file in read mode
            reader = csv.reader(file) #reads file
            data = [row for row in reader] #data stored in list
        return data
    except FileNotFoundError: #error handling in case file not found
        print(f"Error: File '{file_name}' not found.")
        return None

def count_distinct_values(data): #data from CSV file taken as input
    try:
        headers = data[0]
        distinct_values = {} #dictionary created 
        for i in range(len(headers)): 
            column_values = [row[i] for row in data[1:]]
            distinct_values[headers[i]] = set(column_values) #keys are colums headers
        return distinct_values
    except IndexError: #error handling in case file is empty or missing headers
        print("Error: CSV file is empty or missing headers.")
        return None

def generate_synthetic_data(distinct_values, num_records): #synthetic data is generated based on distinct values found in the columns
    try:
        headers = list(distinct_values.keys())
        synthetic_data = []
        for _ in range(num_records): #iteration throug each column
            record = []
            for header in headers: 
                value = random.choice(list(distinct_values[header])) #random selection of a value from set of distinct values
                record.append(value)
            synthetic_data.append(record) #record created
        return synthetic_data
    except TypeError: #Error handling in case no distinct values are found
        print("Error: No distinct values found. Make sure CSV file contains data.")
        return None

def write_csv_file(file_name, headers, synthetic_data): #writes CSV file with synthetic data
    try:
        with open(file_name, 'w', newline='') as file: #file opened in write mode
            writer = csv.writer(file)
            writer.writerow(headers) #headers in first row
            writer.writerows(synthetic_data) #synthetic data records entered in rows
        print(f"Synthetic data generated and saved to '{file_name}'.") #successful execution message
    except Exception as e: #cathches exceptions that occur during the writing process
        print(f"Error while writing to file: {e}") #Error message

def main(): #glues everything together and executes
    input_file = "Fictional_Customers.csv" #input file name defined
    output_file = "Synthetic_Data.csv" #output file name defined
    
    data = read_csv_file(input_file) #data read with input file
    if data is None:
        return
    
    distinct_values = count_distinct_values(data) #data counted and stored
    if distinct_values is None:
        return
    
    num_records = input("Enter the number of records to generate: ") #user prompted to enter how many records required to be generated
    try:
        num_records = int(num_records) #conversion to integer
        if num_records <= 0: #error handling for negative numbers
            print("Error: Number of records must be a positive integer.")
            return
    except ValueError: #error handling in case non numeric input entered
        print("Error: Invalid input. Please enter a valid number.")
        return
    
    synthetic_data = generate_synthetic_data(distinct_values, num_records) #data generated
    if synthetic_data is None:
        return
    
    headers = list(distinct_values.keys())
    write_csv_file(output_file, headers, synthetic_data) #data written to new output file

main()
