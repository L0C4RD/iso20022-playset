from . import base_types

class Max20PositiveDecimalNumber(base_types._BaseDataType_Decimal):

	_max_totaldigits = 20
	_max_fractiondigits = 2
	_min_inclusive = 0

