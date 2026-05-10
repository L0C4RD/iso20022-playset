from . import base_types
import ActiveOrHistoricCurrencyCode

class ActiveOrHistoricCurrencyAnd20DecimalAmount(base_types._BaseDataType_Decimal):

	attrib = {
		"Ccy" : None,
	}

	_attrib_defs = frozenset((
		base_types.AttributeEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, required=True),
	))

	_max_totaldigits = 25
	_max_fractiondigits = 20
	_min_inclusive = 0

