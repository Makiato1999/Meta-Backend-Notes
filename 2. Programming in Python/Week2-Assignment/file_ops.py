def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name, "r") as file:
        content = file.read()
    print(content)
    return content
    raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE
    list = []
    with open(file_name, "r") as file:
        temp_list = file.readlines()
        for index, line in enumerate(temp_list):
            list.append(temp_list[index])
    return list
    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    firstLine = file_contents.split("\n", 1)[0]
    with open(output_filename, "w") as file:
        file.write(firstLine)
    return None
    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE
    temp_list = []
    list = []
    with open(file_name, "r") as file:
        temp_list = file.readlines()
        for index, item in enumerate(temp_list, start=1):
            if index % 2 == 0:
                list.append(item)
    return list
    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    temp_list = []
    list = []
    with open(file_name, "r") as file:
        temp_list = file.readlines()
        for item in reversed(temp_list):
            list.append(item)
    return list
    raise NotImplementedError()

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    path = "./2. Programming in Python/Week2-Assignment/sampletext.txt"
    createFile_path = "./2. Programming in Python/Week2-Assignment/online.txt"
    file_contents = read_file(path)
    print(read_file_into_list(path))
    write_first_line_to_file(file_contents, createFile_path)
    print(read_even_numbered_lines(path))
    print(read_file_in_reverse(path))

if __name__ == "__main__":
    main()