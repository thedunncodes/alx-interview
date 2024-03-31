#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re
import signal
from datetime import datetime
from sys import stdin, exit


available_codes = {}
filesize_sum = 0
num_lines = 0


def split_string(s):
    '''
    Splits strings based on the required pattern

    Return: A list of delimited strings
    '''

    single_quote_pattern = r'"([^"]*)"'
    square_bracket_pattern = r'\[([^\]]*)\]'

    quoted_words = re.findall(single_quote_pattern, s)
    square_bracketed_words = re.findall(square_bracket_pattern, s)

    replaced_string = re.sub(single_quote_pattern, '__QUOTED_WORD__', s)
    replaced_string = re.sub(square_bracket_pattern,
                             '__SQUARE_BRACKETED_WORD__', replaced_string)

    split_string = replaced_string.split()

    for i, word in enumerate(split_string):
        if word == '__QUOTED_WORD__':
            split_string[i] = quoted_words.pop(0)
        elif word == '__SQUARE_BRACKETED_WORD__':
            split_string[i] = square_bracketed_words.pop(0)

    return split_string


def date_validator(date):
    '''
    Checks if the parsed in date matches an actual date format

    Return: A boolean
    '''
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    try:
        date_res = bool(datetime.strptime(date, date_format))
    except ValueError:
        date_res = False

    return date_res


def status_code_validator(code):
    '''
    Checks if 'code' is present among the needed status codes
    and saves it in a dictionary for future references

    sorted_dict: a sorted tuple of the available_codes dict returned
    to be able to have a sorted dict

    Return: A sorted tuple of the 'available_codes' dictionary
    '''
    codes = [200, 301, 400, 401, 403, 404, 405, 500]

    if code in available_codes:
        available_codes[code] += 1
    elif code in codes:
        available_codes[code] = 1

    sorted_dict = sorted(available_codes.items())

    return sorted_dict


def signal_handler(signal, frame):
    '''
    Handles keyboard Interruption
    '''
    print("File size: {}".format(filesize_sum))
    for k, v in available_codes.items():
        print("{}: {}".format(k, v))
    exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in stdin:
    try:
        num_lines += 1
        check_point = split_string(line.rstrip())

        ipaddress = check_point[0].split(".")
        if len(ipaddress) >= 4:
            ip_res = all(map(str.isdigit, ipaddress))
        else:
            ip_res = None

        date_status = date_validator(check_point[2])

        if ip_res and date_status:
            if check_point[4].isdigit():
                code_validator = status_code_validator(int(check_point[4]))
                available_codes = dict(code_validator)

            if check_point[5].isdigit():
                filesize_sum += int(check_point[5])

        if num_lines % 10 == 0:
            print("File size: {}".format(filesize_sum))
            for k, v in available_codes.items():
                print("{}: {}".format(k, v))

    except Exception as e:
        print(e)
