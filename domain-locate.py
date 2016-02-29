#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Inspired by theHarvester and the capabilities. This project is simply a learning experience of
# recon methods to obtain email address and the way you can go about it.
# Also I really wanted the ability to learn SQL, and make this tool multipthreaded!
#
# * = Require API Key
#
import os
import argparse
import sys
import configparser
from Helpers import helpers
from Common import Conducter 



def cli_parser():
    parser = argparse.ArgumentParser(add_help=False, description='''
        Built off the Concept from Hacking Team and other Forensic Classes taken\n
        from the past. Really intresting concept to track and correlate users.\n
        ''')
    parser.add_argument(
        "-f", metavar='file-in.txt', help="Provide the output file from PS agent.")
    parser.add_argument(
        "-k", metavar="Wifi-Location.kml", help="Set the output KML file name")
    parser.add_argument(
        "-u", metavar="UserName", help="Set the Username required for WIGLE API")
    parser.add_argument(
        "-p", metavar="Password", help="Set the Password for WIGLE API")
    parser.add_argument(
        "-v", action='store_true', help="Set this switch for verbose output of modules")
    parser.add_argument('-h', '-?', '--h', '-help',
                        '--help', action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.h:
        parser.print_help()
        sys.exit()
    return args.f, args.k, args.v, args.u, args.p


def TaskControler():
    # Get all the options passed and pass it to the TaskConducter, this will
    # keep all the prcessing on the side.
    # need to pass the store true somehow to tell printer to restrict output
    cli_file, cli_kmlname, cli_verbose, cli_username, cli_password = cli_parser()
    if cli_file:
        Task = Conducter.Conducter(cli_file, cli_kmlname, cli_username, cli_password, verbose=cli_verbose)
        Task.TaskController()
    else:
        print " [*] No file name?"
        sys.exit(0)



def main():
    # instatiate the class
    TaskControler()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)