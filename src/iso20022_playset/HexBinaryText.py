import base_types

class HexBinaryText(base_types._BaseDataType_String):

	_pattern = r"[0-9a-fA-F]+"

