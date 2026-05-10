from . import base_types

class FedwireRoutingNumberIdentifier(base_types._BaseDataType_String):

	_pattern = r"FW[0-9]{9,9}"

