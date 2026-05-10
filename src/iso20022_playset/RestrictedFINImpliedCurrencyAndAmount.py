import base_types

class RestrictedFINImpliedCurrencyAndAmount(base_types._BaseDataType_Decimal):

	_max_totaldigits = 14
	_max_fractiondigits = 5
	_min_inclusive = 0

