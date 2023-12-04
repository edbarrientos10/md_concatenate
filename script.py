import os

# Set the directory containing your Markdown files
markdown_dir = '/Users/edbarrientos/Downloads/kontapedia'  # Replace with the path to your Markdown files
output_file = 'combined_file.md'  # Name of the output file

# Function to concatenate the Markdown files
def concatenate_markdown_files(directory, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        # Iterate through each file in the directory
        for filename in os.listdir(directory):
            if filename.endswith('.md'):  # Check if the file is a Markdown file
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read() + '\n\n new article \n\n')  # Append file content to the output file

# Call the function with the specified directory and output file name
concatenate_markdown_files(markdown_dir, output_file)

print(f"All Markdown files have been concatenated into {output_file}")
