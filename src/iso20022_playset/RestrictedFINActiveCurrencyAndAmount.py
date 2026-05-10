from . import base_types
import ActiveCurrencyCode

class RestrictedFINActiveCurrencyAndAmount(base_types._BaseDataType_Decimal):

	attrib = {
		"Ccy" : None,
	}

	_attrib_defs = frozenset((
		base_types.AttributeEntry(name='Ccy', type=ActiveCurrencyCode, required=True),
	))

	_max_totaldigits = 14
	_max_fractiondigits = 5
	_min_inclusive = 0

