from . import base_types

class OrderStatus4Code(base_types._BaseDataType_String):

	_values = {
		"PACK",
		"COSE",
		"STNP",
		"RECE",
		"SETT",
		"CPNP",
		"CNFC",
		"DONE",
		"DONF",
		"OPOD",
		"IACO",
	}

