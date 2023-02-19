import cowsay
import argparse
flags = ["l", "n", "b", "d", "g", "p", "s", "t", "w", "y"]
parser = argparse.ArgumentParser(prog = 'Cowsay')
parser.add_argument("message", nargs='?', default="hello", help="text")
parser.add_argument("-f", "--cowfile", default="default", help="custom string")
parser.add_argument("-e", "--eyes", default="00", help="eye string")
parser.add_argument("-T", "--tongue", default="  ", help="tongue string")
parser.add_argument("-W", "--width", type=int, default=40, help="The width of the text")

for flag in flags:
    parser.add_argument(f"-{flag}", action="store_true")
args = parser.parse_args().__dict__

if args["l"]:
    print("Cow files:")
    print(*cowsay.list_cows())
else:
    preset = "".join([flag for flag in ["b", "d", "g", "p", "s", "t", "w", "y"] if args[flag]])
    if "/" not in args["cowfile"]:
        s = cowsay.cowsay(args["message"], cow=args["cowfile"], eyes=args["eyes"], width=args["width"], tongue=args["tongue"], preset=preset, wrap_text=args["n"])
    else:
        s = cowsay.cowsay(args["message"], cowfile=args["cowfile"], eyes=args["eyes"], width=args["width"], tongue=args["tongue"], preset=preset, wrap_text=args["n"])
    print(s)

