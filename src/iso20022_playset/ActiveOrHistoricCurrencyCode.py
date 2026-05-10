import base_types

class ActiveOrHistoricCurrencyCode(base_types._BaseDataType_String):

	_pattern = r"[A-Z]{3,3}"

