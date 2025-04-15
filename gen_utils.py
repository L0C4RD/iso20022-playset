# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

import secrets
import string
from xml.sax.saxutils import escape
import base64
import warnings

from hypothesis import strategies as st

DEFAULT_LIST_MIN = 0
DEFAULT_LIST_MAX = 10

DEFAULT_STR_MIN = 0
DEFAULT_STR_MAX = 64

DEFAULT_MAX_TOTALDIGITS = 20
DEFAULT_MAX_FRACTIONDIGITS = 10

PRINTABLE_NOWS = string.digits+string.ascii_letters+string.punctuation

def string_from_pattern(pattern):

    # This is so disgusting. Let's update this to exrex or something.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        strategy = st.from_regex(pattern, fullmatch=True)
        s = strategy.example()
    return s

def random_string_xmlescape(min, max):

    inner_max = max if max is not None else DEFAULT_STR_MAX
    inner_min = min if min is not None else DEFAULT_STR_MIN

    length = secrets.choice(range(inner_min, inner_max+1))

    chartoks = [ escape(secrets.choice(PRINTABLE_NOWS)) for _ in range(length) ]

    while sum(len(t) for t in chartoks) != length:

        chartoks.pop(0)

        while sum(len(t) for t in chartoks) < length:

            chartoks.append(escape(secrets.choice(PRINTABLE_NOWS)))
    
    return "".join(chartoks)

def random_string_b64(min, max):

    inner_max = max if max is not None else DEFAULT_STR_MAX
    inner_min = min if min is not None else DEFAULT_STR_MIN

    min_bytes = (inner_min*3)//4
    max_bytes = (inner_max*3)//4

    bytes_length = secrets.choice(range(min_bytes, max_bytes+1))

    return base64.b64encode(secrets.token_bytes(bytes_length))

def random_decimal(min, max, max_fractiondigits, max_totaldigits):

    inner_max_totaldigits = DEFAULT_MAX_TOTALDIGITS if max_totaldigits is None else max_totaldigits
    inner_max_fractiondigits = DEFAULT_MAX_FRACTIONDIGITS if max_fractiondigits is None else max_fractiondigits

    inner_max_string = ("9"*inner_max_totaldigits) if max is None else str(max)
    inner_min_string = ("-" + "9"*inner_max_totaldigits) if min is None else str(min)
    inner_max = float(inner_max_string)
    inner_min = float(inner_min_string)

    # First, decide if we're positive or negative.
    if inner_min < 0 and inner_max < 0:
        is_negative = True
    elif inner_min < 0:
        is_negative = coin_flip()
    else:
        is_negative = False

    # Then generate the integer part.
    if is_negative:
        max_integer_length = len(inner_min_string.split(".", 1)[0])-1
        max_integer_length = 1 if max_integer_length == 0 else max_integer_length
    else:
        max_integer_length = len(inner_max_string.split(".", 1)[0])
        max_integer_length = 1 if max_integer_length == 0 else max_integer_length

    integer_length = secrets.choice(range(0, max_integer_length+1))
    integer_string = "".join(secrets.choice(string.digits) for _ in range(integer_length))

    integer_max = False
    if is_negative:
        if int(integer_string) *-1 < inner_min:
            integer_string = inner_min_string.split(".", 1)[0][1:]
            integer_max = True
    else:
        if int(integer_string) > inner_max:
            integer_string = inner_max_string.split(".", 1)[0]
            integer_max = True

    # Then do the decimal part
    max_decimal_places = min(
        inner_max_fractiondigits,
        inner_max_totaldigits - len(integer_string)
    )
    decimal_places = secrets.choice(range(0, max_decimal_places+1))
    decimal_string = "".join(secrets.choice(string.digits) for _ in range(decimal_places))

    # Put it together.
    integer = ("-" if is_negative else "+" if coin_flip() else "") + integer_string
    decimal = ("." if len(decimal_string) > 0 else "" if max_fractiondigits == 0 else "." if coin_flip() else "") + decimal_string

    number_string = integer+decimal

    if is_negative:
        if float(number_string) < inner_min:
            number_string = inner_min_string
    else:
        if float(number_string) > inner_max:
            number_string = inner_max_string

    return number_string

def coin_flip():
    return secrets.choice((True, False))

def list_length(field_def):

    min = field_def.min if field_def.min is not None else DEFAULT_LIST_MIN
    max = field_def.max if field_def.max is not None else DEFAULT_LIST_MAX

    return secrets.choice(range(min, max+1))

def choose_one(iterable_in):
    return secrets.choice(iterable_in)


if __name__ == "__main__":

    s=random_string(1,2)
    print(s)
    print(len(s))