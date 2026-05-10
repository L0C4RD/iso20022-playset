from . import base_types

class ReservationStatus1Code(base_types._BaseDataType_String):

	_values = {
		"ENAB",
		"DISA",
		"DELD",
		"REQD",
		"BLKD",
	}

