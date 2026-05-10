from . import base_types

class ISO8583TransactionTypeCode(base_types._BaseDataType_String):

	_pattern = r"[0-9A-Z]{2,2}"

