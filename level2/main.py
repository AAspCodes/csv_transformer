IN_FILE="data/in_data.csv"
OUT_FILE="data/out_data.csv"


from csv_transformer.arg_parser import get_args
from csv_transformer.serde import read_config, read_csv, write_csv
from csv_transformer.transformer import transform


def main():
    # get args
    args = get_args()
    # get transform config
    config = read_config(args.config) 
    # get input data
    input_data = read_csv(args.input)
    # apply transfomr
    out_data = transform(input_data, config)
    # write out transformed data
    write_csv(out_data, args.output)


if __name__ == "__main__":
    main()
