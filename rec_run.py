import os
import argparse


def get_all_ini_files():
    """
    collect all ini files in the current folder
    :return: a list of sorted file names
    """
    current_path = os.getcwd()
    all_files = os.listdir(current_path)

    ini_files = []

    for item in all_files:
        if os.path.isfile(item) and item.endswith('.ini'):
            ini_files.append(item)

    return sorted(ini_files)


def modify_arg_file(file_name=None, value=None):
    """
    change arg file
    :param file_name: which file to change
    :param value: what value should be changed to
    :return: None
    """
    with open("astra_in.in", 'r') as arg_file:
        contents = arg_file.readlines()

        if file_name is not None:
            distribution_line = contents[2]
            line_parts = distribution_line.split('\'')
            line_parts[1] = file_name
            new_line = '\''.join(line_parts)
            contents[2] = new_line

        if value is not None:
            # max_b_line = contents[68]
            max_b_line = contents[80]   # 80 if space charge module is taken into account
            max_b_part = max_b_line.split('=')
            max_b_part[1] = value
            new_max_b_line = '='.join(max_b_part)
            contents[80] = new_max_b_line  # 80 if space charge module is taken into account

    with open('astra_in_' + file_name + '-solStrength' + value + '.in', 'w') as arg_file:
        arg_file.writelines(contents)


def main(filename=None, start=None, end=None, step=None):
    """
    main function
    :param filename: particle distribution files
    :param start: imaging solenoid starting B field
    :param end: imaging solenoid final B field
    :param step: scann step size
    :return: None
    """
    if start is not None and filename is None and end is None and step is None:
        files = get_all_ini_files()
        for file in files:
            print('processing {fn} with solenoid B field value of {va}'.format(
                fn=filename,
                va=start
            ))
            modify_arg_file(file_name=file, value=str(start))
            os.system('./astra astra_in_' + file + '-solStrength' + start + '.in')

    elif filename is not None and start is not None and end is not None and step is not None:
        for i in range(int(start), int(end) - 1, int(step)):
            value = i / 10000
            print('processing {fn} with solenoid B field value of {va}'.format(
                fn=filename,
                va=value
            ))
            modify_arg_file(file_name=filename, value=str(value))
            os.system('./astra astra_in_' + filename + '-solStrength' + str(value) + '.in')

    else:
        print('Follow the following format:')
        print('python3 ' + __file__ + ' -f [filename] -start [start] -end [end] -step [step]')
        quit()

    print("DONE.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="file name")
    parser.add_argument('-s', '--start', help='start value (10000 or real number)')
    parser.add_argument('-e', '--end', help='end value (10000)')
    parser.add_argument('-st', '--step', help='step (10000)')

    args = parser.parse_args()

    main(filename=args.filename, start=args.start, end=args.end, step=args.step)
