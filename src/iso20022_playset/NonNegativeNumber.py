import base_types

class NonNegativeNumber(base_types._BaseDataType_Decimal):

	_max_totaldigits = 18
	_max_fractiondigits = 0
	_min_inclusive = 0

