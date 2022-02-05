import argparse


def parse_args():

    description = "you should add those parameter"
    parser = argparse.ArgumentParser(description=description)
    help = "The path of address"
    parser.add_argument('--address', '-a', help=help)
    help = "The phone number"
    parser.add_argument('--phone', '-p', help=help)

    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = parse_args()
    print(args.address)
    print(args.phone)