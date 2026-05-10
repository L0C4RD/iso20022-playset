from . import base_types

class NonNegativeDecimalNumber(base_types._BaseDataType_Decimal):

	_max_totaldigits = 18
	_max_fractiondigits = 17
	_min_inclusive = 0

