import argparse

def hello(name:str):
    return f"Hello, {name}!"

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str, default='World', help='Name to greet')

    args = parser.parse_args()
    print(hello(args.name))