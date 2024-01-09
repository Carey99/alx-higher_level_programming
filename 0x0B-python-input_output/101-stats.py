#!/usr/bin/python3
"""Log parsing"""


def stats_print(size, s_codes):
    """
    Print accumulated metrics
    """
    print("File size: {}".format(size))

    for k in sorted(s_codes):
        print("{}: {}".format(k, s_codes[k]))


if __name__ == "__main__":
    import sys

    size = 0
    s_codes = {}
    v_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                stats_print(size, s_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in v_codes:
                    if s_codes.get(line[-2], -1) == -1:
                        s_codes[line[-2]] = 1
                    else:
                        s_codes[line[-2]] += 1
            except IndexError:
                pass

        stats_print(size, s_codes)

    except KeyboardInterrupt:
        stats_print(size, s_codes)
        raise
