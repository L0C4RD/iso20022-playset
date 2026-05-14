# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RejectionReason12Code(base_types._BaseDataType_String):

	_values = {
		"DEAC",
		"FAIL",
		"SAME",
		"REFI",
		"AGIN",
		"MAIN",
		"OPTI",
		"PEDA",
		"NORO",
		"INET",
		"INUS",
		"INPT",
		"INMV",
		"SAID",
		"MICA",
		"NOAP",
	}