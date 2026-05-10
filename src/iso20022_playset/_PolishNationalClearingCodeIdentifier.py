from . import base_types

class PolishNationalClearingCodeIdentifier(base_types._BaseDataType_String):

	_pattern = r"PL[0-9]{8,8}"

