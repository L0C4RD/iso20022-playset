from . import base_types

class Max15NumericText(base_types._BaseDataType_String):

	_pattern = r"[0-9]{1,15}"

