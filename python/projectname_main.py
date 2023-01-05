#!/usr/bin/env python
# NOTE: use python3 in the shebang line above if targeting py3 and not py2-compatible
""" example main file with cmd line interface """
from argparse import ArgumentParser
import logging
from logging.handlers import RotatingFileHandler
import sys

import packagename
PACKAGE_NAME = "todo_set_this_to_your_packagename"
COMMAND_NAME = "todo_set_this_to_your_commandname"

def parse_args(argv):
    # =========================================================================
    # === set up arguments
    # =========================================================================
    parser = ArgumentParser(description='todo_short_desc_of_projname_goes_here')
    
    # === arguments for the main command
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="count",
                        default=0
    )
    # other examples:
    # parser.add_argument("source", help="directory to copy from")
    # parser.add_argument('-l', '--log',
    #     help="desired filepath of log file",
    #     default="/var/opt/projectname/backup.log"
    # )
    # parser.add_argument('--rclonelog',
    #     help="desired path of rclone log file",
    #     default=None
    # )
    
    parser.set_defaults(func=my_subcommand_method)  # set default behavior if subcommand not given
    
    # === subcommands
    subparsers = parser.add_subparsers(
        title='subcommands',
        description='usage: `projectname $subcommand` ',
        help=f'addtnl help for subcommands: `{COMMAND_NAME} $subcommand -h`'
    )

    parser_status = subparsers.add_parser(
        'todo_my_subcommand', help='todo_help_str_for_my_subcommand'
    )
    parser_status.set_defaults(func=my_subcommand_method)

    # add more here...
    # parser_backup = subparsers.add_parser('backup', help='try backing up right now')
    # parser_backup.set_defaults(func=backup)

    args = parser.parse_args()
    # =========================================================================
    # === set up logging behavior
    # =========================================================================
    if (args.verbose == 0):
        stream_log_level = logging.WARNING
    elif (args.verbose == 1):
        stream_log_level = logging.INFO
    else: #} (args.verbose == 2){
        stream_log_level = logging.DEBUG
    logging.basicConfig(level=stream_log_level)

    # === (optional) create custom logging format(s)
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    formatter = logging.Formatter(
       '%(asctime)s|%(levelname)s\t|%(filename)s:%(lineno)s\t|%(message)s'
    )

    # === (optional) create handlers
    # https://docs.python.org/3/howto/logging.html#useful-handlers
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_log_level)
    stream_handler.setFormatter(formatter)
    stream_handler.addFilter(DuplicateLogFilter())

    file_handler = RotatingFileHandler(
       f'/var/opt/{PACKAGE_NAME}/{COMMAND_NAME}.log', maxBytes=1e6, backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(DuplicateLogFilter())

    # === add the handlers (if any) to the logger
    _handlers = [
        stream_handler,
        file_handler
    ]

    logging.basicConfig(
        handlers=_handlers,
        level=logging.DEBUG  # this must be set to lowest of all levels used in handlers
    )
    # =========================================================================
    return args
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    args.func(args)
else:
    raise AssertionError(
        f"{PACKAGE_NAME}.{SCRIPT_NAME} CLI should called as __main__ and should not be imported."
    )
