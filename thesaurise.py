#!/usr/bin/env python

from src.parser import parse, generateParser



generateParser()

# TODO: Lolhardcoded
for f in ['test.cs', 'test2.cs', 'test3.cs']:
    ast = parse('tests/' + f)
    print(ast)
    print('\n')



