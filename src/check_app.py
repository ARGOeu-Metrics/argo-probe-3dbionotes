#!/usr/bin/python3
import argparse
import sys

import requests


class Nagios:
    OK = 0
    WARNING = 1
    CRITICAL = 2
    UNKNOWN = 3

    def __init__(self):
        self._code = self.OK
        self._msg = ""

    def ok(self, msg):
        self._msg = f"OK - {msg}"
        self._code = self.OK

    def warning(self, msg):
        self._msg = f"WARNING - {msg}"
        self._code = self.WARNING

    def critical(self, msg):
        self._msg = f"CRITICAL - {msg}"
        self._code = self.CRITICAL

    def unknown(self, msg):
        self._msg = f"UNKNOWN - {msg}"
        self._code = self.UNKNOWN

    def get_code(self):
        return self._code

    def get_msg(self):
        return self._msg


def main():
    parser = argparse.ArgumentParser(
        "ARGO probe that tests the functionality of 3dBionotes web application"
    )
    parser.add_argument(
        "-H", "--hostname", dest="hostname", required=True, help="hostname"
    )
    parser.add_argument(
        "-t", "--timeout", dest="timeout", type=int, required=True,
        help="timeout in seconds"
    )
    parser.add_argument(
        "--ca-bundle", dest="ca_bundle", type=str, required=True,
        help="location of CA bundle"
    )
    args = parser.parse_args()

    nagios = Nagios()

    try:
        response = requests.get(
            f"https://{args.hostname}/cv19_annotations/P0DTC2_annotations.json",
            timeout=args.timeout,
            verify=args.ca_bundle
        )

        response.raise_for_status()

        data = response.json()

        if "track_name" not in data[0] or \
                data[0]["track_name"] != "Functional_mapping_PPI":
            nagios.warning("Expected key not in json!")

        else:
            nagios.ok("Data fetched successfully")

    except (
        requests.exceptions.HTTPError,
        requests.exceptions.ConnectionError,
        requests.exceptions.RequestException,
        requests.exceptions.Timeout,
        requests.exceptions.TooManyRedirects
    ) as e:
        nagios.critical(str(e))

    except Exception as e:
        nagios.unknown(str(e))

    print(nagios.get_msg())
    sys.exit(nagios.get_code())


if __name__ == "__main__":
    main()
