#!/usr/bin/env python3
import re


def rearrange_name(name):
    assert type(name) == str, 'Name should be a string'
    assert ',' in name, 'Name should follow a pattern [last name], [first name]. e.g., Gist, Github'
    return re.sub(r"^([\w .]*), ([\w .]*)$", r"\2 \1", name)

