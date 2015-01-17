#!/usr/bin/env python

from src.parser import parse

# TODO: Lolhardcoded
ast = parse("/home/nathan/Code/thesaurise/tests/test.cs")

print(ast)
