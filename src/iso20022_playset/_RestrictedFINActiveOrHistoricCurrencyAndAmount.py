from . import base_types
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class RestrictedFINActiveOrHistoricCurrencyAndAmount(base_types._BaseDataType_Decimal):

	attrib = {
		"Ccy" : None,
	}

	_attrib_defs = frozenset((
		base_types.AttributeEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, required=True),
	))

	_max_totaldigits = 14
	_max_fractiondigits = 5
	_min_inclusive = 0

