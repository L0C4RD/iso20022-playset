from . import base_types
from .CurrencyCode import CurrencyCode

class CurrencyAndAmount(base_types._BaseDataType_Decimal):

	attrib = {
		"Ccy" : None,
	}

	_attrib_defs = frozenset((
		base_types.AttributeEntry(name='Ccy', type=CurrencyCode, required=True),
	))

	_max_totaldigits = 18
	_max_fractiondigits = 5
	_min_inclusive = 0

