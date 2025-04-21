def modify_content(content):
    """
    Modify the content of the file.
    You can change the behavior below (like replacing words, reversing lines, etc.)
    """

    # --- Start of Editable Modifications ---

    # 1. Replace specific words (customize these!)
    content = content.replace("boring", "exciting")
    content = content.replace("bad", "good")

    # 2. Remove blank lines
    lines = content.splitlines()
    non_blank_lines = [line for line in lines if line.strip()]

    # 3. Capitalize each sentence (basic version)
    capitalized_lines = [line.capitalize() for line in non_blank_lines]

    # 4. Add line numbers
    numbered_lines = [f"{idx + 1}: {line}" for idx, line in enumerate(capitalized_lines)]

    # 5. Reverse the text (optional — reverse each line)
    reversed_lines = [line[::-1] for line in numbered_lines]

    # Choose what to return here:
    return "\n".join(reversed_lines)  # <- Change this line to apply different combinations
    # return "\n".join(numbered_lines)
    # return "\n".join(capitalized_lines)

    # --- End of Editable Modifications ---

def main():
    input_filename = input("Enter the name of the file to read: ")

    try:
        with open(input_filename, 'r') as infile:
            original_content = infile.read()

        modified_content = modify_content(original_content)

        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"\nFile successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read or write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if _name_ == "_main_":
    main()