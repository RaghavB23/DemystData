import json
import csv

def generate_spec_file(spec_file):
    """
    Dynamically generate a JSON specification file for the fixed-width data format based on user input.
    """
    fields = []
    print("Enter the fields for the specification:")
    num_fields = int(input("How many fields do you want to define? "))

    for i in range(num_fields):
        field_name = input(f"Enter name for field {i + 1}: ").strip()
        field_length = int(input(f"Enter length for field '{field_name}': "))
        fields.append({"name": field_name, "length": field_length})

    spec = {"fields": fields}
    with open(spec_file, 'w', encoding='utf-8') as file:
        json.dump(spec, file, indent=4)
    print(f"Specification file '{spec_file}' generated successfully.")

def generate_fixed_width_file(data, data_file, spec_file):
    """
    Generate a fixed-width data file based on user-provided data and specification.
    """
    # Load the specification
    with open(spec_file, 'r', encoding='utf-8') as file:
        spec_data = json.load(file)

    fields = spec_data['fields']

    # Validate data length matches spec
    formatted_data = []
    for row in data:
        if len(row) != len(fields):
            raise ValueError(f"Each row must have exactly {len(fields)} fields. Found: {row}")
        
        formatted_row = ""
        for value, field in zip(row, fields):
            formatted_row += value.ljust(field['length'])[:field['length']]
        formatted_data.append(formatted_row)
    
    with open(data_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(formatted_data))
    print(f"Fixed-width data file '{data_file}' generated successfully.")

def parse_fixed_width(input_file, spec_file, output_file, encoding='utf-8'):
    """
    Parse a fixed-width file based on a specification and output a CSV file.
    """
    # Load the specification
    with open(spec_file, 'r', encoding=encoding) as spec:
        spec_data = json.load(spec)

    # Calculate start and end positions for each field
    fields = spec_data["fields"]
    positions = []
    start = 0
    for field in fields:
        length = field["length"]
        positions.append((start, start + length))
        start += length

    # Parse the fixed-width file
    with open(input_file, 'r', encoding=encoding) as infile, open(output_file, 'w', encoding=encoding, newline='') as outfile:
        writer = csv.writer(outfile)

        # Write the header row
        header = [field["name"] for field in fields]
        writer.writerow(header)

        # Write the data rows
        for line in infile:
            row = [line[start:end].strip() for start, end in positions]
            writer.writerow(row)
    
    print(f"Parsed data written to '{output_file}'.")

if __name__ == "__main__":
    # File paths
    spec_file = "spec.json"
    data_file = "fixed_width_data.txt"
    output_file = "output.csv"

    # Step 1: Generate specification file based on user input
    generate_spec_file(spec_file)

    # Step 2: Collect user input for data
    print("Enter data for the fields:")
    with open(spec_file, 'r', encoding='utf-8') as file:
        spec_data = json.load(file)
    num_fields = len(spec_data["fields"])

    # Ask user how many rows they want to input
    num_rows = int(input("How many rows of data do you want to enter? "))
    
    data = []
    for i in range(num_rows):  # Collect user-defined number of rows
        print(f"Enter data for row {i + 1}:")
        row = []
        for field in spec_data["fields"]:
            value = input(f"  {field['name']} (max {field['length']} characters): ").strip()
            row.append(value)
        data.append(row)

    # Step 3: Generate fixed-width file
    generate_fixed_width_file(data, data_file, spec_file)

    # Step 4: Parse the fixed-width file and output to CSV
    parse_fixed_width(data_file, spec_file, output_file)

    print("Processing completed successfully!")
