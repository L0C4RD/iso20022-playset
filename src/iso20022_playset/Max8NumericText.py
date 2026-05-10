from . import base_types

class Max8NumericText(base_types._BaseDataType_String):

	_pattern = r"[0-9]{1,8}"

