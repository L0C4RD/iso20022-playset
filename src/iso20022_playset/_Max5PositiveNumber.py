from . import base_types

class Max5PositiveNumber(base_types._BaseDataType_Decimal):

	_max_totaldigits = 5
	_max_fractiondigits = 0
	_min_inclusive = 1

