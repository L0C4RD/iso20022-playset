# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PenaltyStatusReason2Code(base_types._BaseDataType_String):

	_values = {
		"UPDT",
		"SUSP",
		"TECH",
		"SWIC",
		"SESU",
		"SEMP",
		"RALO",
		"OTHR",
		"NEWP",
		"INTS",
		"INSO",
		"CORP",
		"NOSU",
	}