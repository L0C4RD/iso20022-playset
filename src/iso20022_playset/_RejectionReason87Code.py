# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RejectionReason87Code(base_types._BaseDataType_String):

	_values = {
		"OPTY",
		"ULNK",
		"DSEC",
		"LATE",
		"NMTY",
		"CANC",
		"INTV",
		"OPNM",
		"OTHR",
		"EVNM",
		"DQCC",
		"DUPL",
		"DSET",
		"DCAN",
		"TRTY",
		"BUMM",
		"ECMD",
		"ECRD",
		"DUCK",
		"DUST",
		"DSNA",
	}