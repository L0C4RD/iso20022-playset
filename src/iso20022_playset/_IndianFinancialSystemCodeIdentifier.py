from . import base_types

class IndianFinancialSystemCodeIdentifier(base_types._BaseDataType_String):

	_pattern = r"IN[a-zA-Z0-9]{11,11}"

