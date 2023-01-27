#!/usr/bin/env python3

import os, json

# CGI script serve environment variables as json
print("\n----------env----------\n")
print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=1))

# CGI script to report query parameters as html
print("\n----------query----------\n")
print("Content-Type: text/html")
print()
print("<title>Query</title>")
try:
    print("<p>query parameter: <b>%s</b></p>" % os.environ["QUERY_STRING"])
except KeyError:
    print("<p>No query parameter</p>")

# CGI script to report users browser as html
print("\n----------browser----------\n")
print("Content-Type: text/html")
print()
print("<title>Browser</title>")
try:
    print("<p>Browser: <b>%s</b></p>" % os.environ["HTTP_USER_AGENT"])
except KeyError:
    print("<p>No browser</p>")



