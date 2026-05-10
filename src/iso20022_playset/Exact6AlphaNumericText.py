from . import base_types

class Exact6AlphaNumericText(base_types._BaseDataType_String):

	_pattern = r"[a-zA-Z0-9\s]{6}"

