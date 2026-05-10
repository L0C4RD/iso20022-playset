from . import base_types

class ISO8583MessageReasonCode(base_types._BaseDataType_String):

	_pattern = r"[0-9]{4,4}"

