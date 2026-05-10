import base_types

class CHIPSParticipantIdentifier(base_types._BaseDataType_String):

	_pattern = r"CP[0-9]{4,4}"

