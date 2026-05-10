from . import base_types

class Exact4NumericText(base_types._BaseDataType_String):

	_pattern = r"[0-9]{4}"

