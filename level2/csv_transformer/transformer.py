

def transform(in_data: list[list[str]], config: dict) -> list[list[str]]:
    print(in_data)
    out_data_headers = config["out-headers"]
    out_data = [out_data_headers]

     # [1:] to skip in_data's headers
    for in_line in in_data[1:]:

        out_line = ["" for _ in range(len(out_data_headers))] 
        for tfm in config["transformations"]: 

            try:
                f = operation_dict[tfm["operation"]]
            except KeyError as e:
                print(f"{tfm['operation']} not found in operation_dict")
                raise e

            out_line[tfm["out-index"]] = f(in_line[tfm["in-index"]])

        out_data.append(out_line)

    return out_data


def make_it_fancy(val:str) -> str:
    return "Mr. " + val

def copy(val:str) -> str:
    return val

def can_drink(val:str) -> str:
    return "yes" if int(val) >= 21 else "no"

operation_dict = {
        "make_it_fancy": make_it_fancy,
        "copy": copy,
        "can_drink": can_drink,
        }











