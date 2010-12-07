"""
Convert a string into a regular expression that can match it, roughly
grouped into whitespace, digits, letters (and underscores and dashes),
and everything else.

Examples:

>>> import re
>>> patternize('')
''

>>> print patternize('9')
\d+
>>> re.match(patternize('9'), '27') is None
False

>>> print patternize('aBc-')
[-a-zA-Z_]+
>>> re.match(patternize('aBc-'), 'a_b_c-dEFG') is None
False

>>> print patternize('hello world')
[-a-zA-Z_]+\s+[-a-zA-Z_]+
>>> re.match(patternize('hello world'), 'gooDbye MoOn') is None
False

>>> print patternize('hello world!!?!...')
[-a-zA-Z_]+\s+[-a-zA-Z_]+\W+
>>> re.match(patternize('hello world!!?!...'), 'oh nooo!!!') is None
False

>>> print patternize('\\njohn Q. public,\\nat-large')
\s+[-a-zA-Z_]+\s+[-a-zA-Z_]+\W+\s+[-a-zA-Z_]+\W+\s+[-a-zA-Z_]+
>>> re.match(patternize('\\njohn Q. public,\\nat-large'),
...          '\\njohn Q. public,\\nat-large') is None
False

>>> print patternize('_bag_of_potatos__')
[-a-zA-Z_]+
>>> re.match(patternize('_bag_of_potatos__'), '_asdpOPI-UB_') is None
False
>>> re.match(patternize('_bag_of_potatos__'), '9to5') is None
True

"""

def flatten(*args):
    # flatten all args into a one-dimensional list (not tuple)
    result = []
    for arg in args:
        if isinstance(arg, list) or isinstance(arg, tuple):
            for item in arg:
                item = flatten(item)
                result.extend(item)
        else:
            result.append(arg)
    return result

def replace_pattern_with_re_obj(re_obj, astring):
    if not isinstance(astring, basestring):
        return astring
    parts = re_obj.split(astring)
    output = []
    for p in parts:
        output.append(p)
        output.append(re_obj)
    if output:
        output.pop()
    return output

def patternize(astring):
    import re
    patterns = (r'\d+', r'\s+', r'[-a-zA-Z_]+', r'\W+')
    pat_to_re = dict(zip(patterns, [re.compile(r) for r in patterns]))
    re_to_pat = dict([(item[1], item[0]) for item in pat_to_re.items()])

    output = [astring]
    for pat in patterns:
        re_obj = pat_to_re[pat]
        substituted = [replace_pattern_with_re_obj(re_obj, s) for s in output]
        output = flatten(substituted)
        #print '%r %r %r' % (pat, re_map[pat], re_map[pat].sub('X', s))

    #import pprint; pprint.pprint(output)
    pattern_list = [re_to_pat[obj] for obj in output if obj]
    return ''.join(pattern_list)


if __name__ == '__main__':
    import doctest
    print doctest.testmod()
