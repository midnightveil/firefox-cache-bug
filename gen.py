# This was too hard to replicate by hand.

import string

ALPHABET = string.ascii_lowercase

def script_contents(name, additional=""):
    return """\
export function %s(arg) {
    return "%s" + arg%s;
}
""" % (name, name, additional)

def import_contents(name):
    return """\
import {%s} from "/depends/%s.js";
""" % (name, name)

def double_script_contents(name):
    return import_contents(name.upper()) \
        +  script_contents(name, " + " + name.upper() + "('')")

for letter in ALPHABET:
    with open(f"depends/{letter.upper()}.js", "w") as f:
        f.write(script_contents(letter.upper()))

    with open(f"depends/{letter}.js", "w") as f:
        f.write(double_script_contents(letter))

with open("main.js", "w") as f:
    for letter in ALPHABET:
        f.write(import_contents(letter))

    f.write("""
document.getElementById("for-js").innerHTML =
    """)

    for letter in ALPHABET:
        f.write(letter + "(")

    f.write("'_'")

    for letter in ALPHABET:
        f.write(")")

    f.write(";")
