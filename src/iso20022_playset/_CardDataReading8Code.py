# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CardDataReading8Code(base_types._BaseDataType_String):

	_values = {
		"TAGC",
		"PHYS",
		"BRCD",
		"MGST",
		"CICC",
		"DFLE",
		"CTLS",
		"ECTL",
		"CDFL",
		"SICC",
		"UNKW",
		"QRCD",
		"OPTC",
	}