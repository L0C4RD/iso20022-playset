from . import base_types

class Max10PositiveNumber(base_types._BaseDataType_Decimal):

	_max_totaldigits = 10
	_max_fractiondigits = 0
	_min_inclusive = 1

