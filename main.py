import csv


def txt_to_csv(input_file, output_file, delimiter):
    """
    Converts a TXT file to a CSV file.

    Parameters:
        input_file (str): Path to the input TXT file.
        output_file (str): Path to the output CSV file.
        delimiter (str): Delimiter used in the TXT file
        (e.g., '\t' for tab, ',' for comma).
    """
    try:
        with open(input_file, "r") as txt_file:
            lines = txt_file.readlines()

        with open(output_file, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)

            for line in lines:
                # Split each line by the delimiter and write to the CSV
                row = line.strip().split(delimiter)
                writer.writerow(row)

        print(f"File successfully converted to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    input_txt_file = "input.txt"
    output_csv_file = "output.csv"
    delimiter_used = "\t"

    txt_to_csv(input_txt_file, output_csv_file, delimiter_used)
