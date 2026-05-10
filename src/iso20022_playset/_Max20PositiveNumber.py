from . import base_types

class Max20PositiveNumber(base_types._BaseDataType_Decimal):

	_max_totaldigits = 20
	_max_fractiondigits = 0
	_min_inclusive = 0

