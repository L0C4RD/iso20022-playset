# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class OnLineReason2Code(base_types._BaseDataType_String):

	_values = {
		"RNDM",
		"ICCF",
		"MERF",
		"TRMF",
		"ISSF",
		"FRLT",
		"EXFL",
		"TAMT",
		"CBIN",
		"UBIN",
		"CPAN",
		"FLOW",
		"CRCY",
		"IFPR",
	}