import base_types

class Min8Max28NumericText(base_types._BaseDataType_String):

	_pattern = r"[0-9]{8,28}"

