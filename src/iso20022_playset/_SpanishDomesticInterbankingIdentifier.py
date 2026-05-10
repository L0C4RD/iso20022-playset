from . import base_types

class SpanishDomesticInterbankingIdentifier(base_types._BaseDataType_String):

	_pattern = r"ES[0-9]{8,9}"

