import base_types
import ActiveOrHistoricCurrencyCode

class ActiveOrHistoricCurrencyAnd13DecimalAmount(base_types._BaseDataType_Decimal):

	attrib = {
		"Ccy" : None,
	}

	_attrib_defs = frozenset((
		base_types.AttributeEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, required=True),
	))

	_max_totaldigits = 18
	_max_fractiondigits = 13
	_min_inclusive = 0

