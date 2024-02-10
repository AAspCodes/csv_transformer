

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
        out_line[0] = "Mr. " + in_line[1] # make it fancy
        out_line[1] = "yes" if int(in_line[2]) >= 21 else "no" # google "python inline ternary"
        out_line[2] = in_line[0]
        out_line[3] = in_line[2]
        out_data.append(out_line)

    write_csv(out_data, OUT_FILE)
