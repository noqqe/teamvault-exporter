#!/usr/bin/env python3

"""
What this script does:
* exports all secret entries
* exports only secrets that are available to the current user.
* finds the LATEST revision of the password
* writs a CUSTOM json as output.

What this script does NOT:
* exporting ALL versions (past versions) of a secret
* exporting uploaded files from teamvault
"""

import requests
import json
import argparse

import warnings
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

def tv_get(url, auth):
    """
    simple requests query builder
    """
    b = requests.get(url, auth=requests.auth.HTTPBasicAuth(auth.split(":")[0], auth.split(":")[1]), verify=False).text
    j = json.loads(b)
    return j

def get_secret(url, auth):
    """
    fetch 1 password
    """

    # Fetch latest revision
    if url is not None:
        j = tv_get(url, auth)
    else:
        return ""

    # Fetch data from latest revision
    try:
        p = tv_get(j["data_url"], auth)["password"]
    except KeyError:
        p = ""

    # Give password back
    return p


def get_page(url, auth, entries):
    """
    fetches 1 page of password entries and parses its body to python dict
    """
    j = tv_get(url, auth)
    res = j["results"]

    # loop over all entries and if a password is available, add it to the dict
    for n, entry in enumerate(res):
        print("Exporting {}".format(entry["name"]))
        if entry["content_type"] == "password":
            p = get_secret(entry["current_revision"], auth)
            res[n]["password"] = p

    entries.extend(res)

    return j["next"]

def export_jsonfile(e, out):
    out_file = open(out, "w")
    json.dump(e, out_file, indent=2)


def main(auth, baseurl, out):
    """
    main loop for export passwords
    """

    # init empty result list
    entries = list()

    # Loop over pages
    next_url = baseurl + "/api/secrets"
    while next_url is not None:
        next_url = get_page(next_url, auth, entries)
        print("## Exported {} entries so far".format(len(entries)))

    # Write json file
    export_jsonfile(entries, out)

# Options
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--auth", type=str, required=True, help="auth in user:pass form")
parser.add_argument("-u", "--url", type=str, required=True, help="for example https://teamvault.acme.com")
parser.add_argument("-o", "--output", type=str, required=True, help="output file")
args = parser.parse_args()

# start exporting
main(auth=args.auth, baseurl=args.url, out=args.output)


