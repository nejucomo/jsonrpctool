import os
import re
import sys
import json
import argparse
import jsonrpcclient


def main(args=sys.argv[1:]):
    """
    Commandline JSON-RPC client tool.
    """
    (endpoint, method, listparams, dictparams) = parse_args(args)
    result = jsonrpcclient.request(endpoint, method, *listparams, **dictparams)
    json.dump(result, sys.stdout, sort_keys=True, indent=2)


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)
    p.add_argument(
        '--endpoint',
        dest='ENDPOINT',
        default=os.environ.get('JSONRPC_ENDPOINT'),
    )
    p.add_argument('METHOD')
    p.add_argument('PARAMS', nargs='*')
    opts = p.parse_args(args)

    listparams = []
    dictparams = {}
    paramtype = None

    for param in opts.PARAMS:
        m = re.match(r'((?P<KEY>[a-zA-Z0-9_]+)=)?(?P<VALUE>.*)$', param)
        if m is None:
            p.error('Could not parse: {!r}'.format(param))
        else:
            key = m.group('KEY')
            if key is None:
                newparamtype = 'array'
            else:
                newparamtype = 'object'

            if paramtype is None:
                paramtype = newparamtype
            elif newparamtype != paramtype:
                p.error('Cannot mix array and object params.')

            valstr = m.group('VALUE')
            try:
                value = json.loads(valstr)
            except ValueError as e:
                p.error('Could not decode arg {!r}: {}'.format(valstr, e))

            if paramtype == 'array':
                listparams.append(value)
            else:
                dictparams[key] = value

    return (opts.ENDPOINT, opts.METHOD, listparams, dictparams)
