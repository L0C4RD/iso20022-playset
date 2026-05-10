from . import base_types

class AustrianBankleitzahlIdentifier(base_types._BaseDataType_String):

	_pattern = r"AT[0-9]{5,5}"

