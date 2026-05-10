import base_types

class Max10NumericText(base_types._BaseDataType_String):

	_pattern = r"[0-9]{1,10}"

