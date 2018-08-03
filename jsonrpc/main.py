import sys
import argparse


def main(args=sys.argv[1:]):
    """
    Commandline JSON-RPC client tool.
    """
    opts = parse_args(args)
    raise NotImplementedError(main)


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)
    return p.parse_args(args)
