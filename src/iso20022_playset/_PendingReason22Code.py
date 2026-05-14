# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PendingReason22Code(base_types._BaseDataType_String):

	_values = {
		"ADEA",
		"OTHR",
		"MONY",
		"LACK",
		"LATE",
		"CLAC",
		"CMON",
		"PREA",
		"LINK",
		"CYCL",
		"BOTH",
		"PRCY",
		"FUTU",
	}