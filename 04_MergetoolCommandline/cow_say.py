import sys
import cmd
import shlex
import cowsay


class AbuseCow(cmd.Cmd):
    intro = 'Make her moo'
    prompt = '  ^  ^\n (o)(o)\n( .  . )____] '

    def do_list_cows(self, args):
        if args:
            args = shlex.split(args)
            args = shlex.join(args)
            print(cowsay.list_cows(args))
        else:
            print(cowsay.list_cows(cowsay.COW_PEN))

    def _parse_cow_args(self, args):
        args = shlex.split(args)
        eyes = '[][]'
        tongue = '||'
        cow = 'default'
        for arg in args.copy():
            if arg.startswith('eyes='):
                eyes = arg.split('=')[1]
                args.remove(arg)
            if arg.startswith('tongue='):
                tongue = arg.split('=')[1]
                args.remove(arg)
            if arg.startswith('cow='):
                cow = arg.split('=')[1]
                cow = cow.replace('.cow', '')
                args.remove(arg)
        message = shlex.join(args) if args else ''.join(sys.stdin.readlines())
        return message, eyes, tongue, cow

    def do_cowsay(self, args):
        message, eyes, tongue, cow = self._parse_cow_args(args)
        print(cowsay.cowsay(message=message, eyes=eyes, tongue=tongue, cow=cow))

    def do_cowthink(self, args):
        message, eyes, tongue, cow = self._parse_cow_args(args)
        print(cowsay.cowthink(message=message, eyes=eyes, tongue=tongue, cow=cow))

    def complete_cowsay(self, plx, line, beg, end):
        eyes = ['XX', 'II', 'OOO', 'WW', 'qp']
        tongue = ['U', 'II', 'V', 'X', '0']
        cow = ['tux', 'www', 'whale', 'surgery', 'sheep']
        eyes_compl = [f'eyes={x}' for x in eyes]
        tongue_compl = [f'tongue={x}' for x in tongue]
        cow_compl = [f'cow={x}' for x in cow]
        return [c for c in eyes_compl + tongue_compl + cow_compl if c.startswith(plx)]

    def complete_cowthink(self, plx, line, beg, end):
        return self.complete_cowsay(plx, line, beg, end)

    def complete_list_cows(self, plx, line, beg, end):
        completions = [cowsay.COW_PEN.as_posix()]
        return [c for c in completions if c.startswith(plx)]

    def do_exit(self):
        return True

    def do_EOF(self):
        return True


if __name__ == '__main__':
    AbuseCow().cmdloop()
