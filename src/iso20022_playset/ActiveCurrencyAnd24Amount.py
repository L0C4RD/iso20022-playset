import base_types
import ActiveCurrencyCode

class ActiveCurrencyAnd24Amount(base_types._BaseDataType_Decimal):

	attrib = {
		"Ccy" : None,
	}

	_attrib_defs = frozenset((
		base_types.AttributeEntry(name='Ccy', type=ActiveCurrencyCode, required=True),
	))

	_max_totaldigits = 24
	_max_fractiondigits = 5
	_min_inclusive = 0

