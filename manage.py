import argparse

if __name__ == '__main__':
    modules = {}

    parser = argparse.ArgumentParser(description='Automation')
    parser.add_argument('module', help='Module to run')
    parser.add_argument('script', help='Script to run')
    parser.add_argument('--optional_arg', nargs='?', default=None, help='Optional Parameter')

    args = parser.parse_args()
    optional_arg = args.optional_arg

    if args.module in modules:
        if optional_arg:
            modules[args.module](args.script, optional_arg-optional_arg)
        else:
            modules[args.module](args.script)
    else:
        print("Invalid module")
