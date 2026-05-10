import base_types

class CanadianPaymentsARNIdentifier(base_types._BaseDataType_String):

	_pattern = r"CA[0-9]{9,9}"

