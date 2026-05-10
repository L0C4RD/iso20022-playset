from . import base_types

class GeographicPointInDecimalDegrees(base_types._BaseDataType_String):

	_max = 27
	_pattern = r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?"

