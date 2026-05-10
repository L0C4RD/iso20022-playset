from . import base_types

class RestrictedFINDecimalNumber(base_types._BaseDataType_Decimal):

	_max_totaldigits = 14
	_max_fractiondigits = 14

