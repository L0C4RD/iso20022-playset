from . import base_types

class ImpliedCurrencyAndAmount(base_types._BaseDataType_Decimal):

	_max_totaldigits = 18
	_max_fractiondigits = 5
	_min_inclusive = 0

