# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class SystemEventType2Code(base_types._BaseDataType_String):

	_values = {
		"LVCO",
		"LVCC",
		"LVRT",
		"EUSU",
		"STSU",
		"LWSU",
		"EUCO",
		"FIRE",
		"STDY",
		"LTNC",
		"CRCO",
		"RECC",
		"LTGC",
		"LTDC",
		"CUSC",
		"IBKC",
		"SYSC",
		"SSSC",
		"REOP",
		"PCOT",
		"NPCT",
		"ESTF",
	}