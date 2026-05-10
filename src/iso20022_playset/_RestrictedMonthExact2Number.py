from . import base_types

class RestrictedMonthExact2Number(base_types._BaseDataType_Decimal):

	_max_totaldigits = 2
	_max_fractiondigits = 0
	_min_inclusive = 1
	_max_inclusive = 12
	_pattern = r"[0-9]{2,2}"

