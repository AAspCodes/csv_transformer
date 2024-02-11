IN_FILE = "data/in_data.csv"
OUT_FILE = "data/out_data.csv"


def read_csv(path: str) -> list[list[str]]:
    with open(path, "r") as f:
        contents = f.read()

    out_list = []
    for line in contents.split("\n"):

        # skip final line of input file if empty
        if len(line) == 0:
            continue

        line_list = []
        for val in line.split(","):
            line_list.append(val)
        out_list.append(line_list)

    return out_list


def write_csv(data_to_write: list[list[str]], path: str):
    # convert 2D list of strings to a single string joined by "," and "\n"
    #   the inner list comprehension iterates over each row,
    #   takes the line: list[str], and converts it into a single string. with join
    #   the outer join takes the results list[str] where each string is was a row,
    #   and joins them all into single string

    #   Note: list comprehension do not mutate the list they iterate over,
    #       they copy and tranfrom and produce a new list
    #
    #   uncomment line below to see the intermediary step
    #   print([",".join(line) for line in data_to_write])
    #
    str_data = "\n".join([",".join(line) for line in data_to_write])
    with open(path, "w") as f:
        f.write(str_data)


def transform():
    in_data = read_csv(IN_FILE)
    print(in_data)
    out_data_headers = ["name", "can_drink", "date", "age"]
    out_data = [out_data_headers]

    # [1:] to skip in_data's headers
    for in_line in in_data[1:]:

        # initialize list of empty strings, with length of out_data_headers
        #   this is a list comprehension
        #   list comprehensions save the common pattern of,
        #       - initialize empty list
        #       - loop over something
        #       - insert something into initialized empty list
        #       - I did this in read_csv, twice in a nested way
        #   _ means ignore this value
        out_line = ["" for _ in range(len(out_data_headers))]

        # here is the copying and transforming
        out_line[0] = "Mr. " + in_line[1]  # make it fancy
        out_line[1] = (
            "yes" if int(in_line[2]) >= 21 else "no"
        )  # google "python inline ternary"
        out_line[2] = in_line[0]
        out_line[3] = in_line[2]
        out_data.append(out_line)

    write_csv(out_data, OUT_FILE)


if __name__ == "__main__":
    transform()
