# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CorporateActionPendingStatus1Code(base_types._BaseDataType_String):

	_values = {
		"CNFC",
		"PUBF",
		"REOR",
		"ACCR",
		"SCAL",
		"LATE",
		"MATU",
		"PAYD",
		"POSD",
		"CNPC",
		"CNRD",
		"CNRE",
		"VRON",
		"VRZC",
	}