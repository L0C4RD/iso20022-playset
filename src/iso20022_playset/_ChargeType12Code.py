# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ChargeType12Code(base_types._BaseDataType_String):

	_values = {
		"BEND",
		"DISC",
		"FEND",
		"POST",
		"REGF",
		"SHIP",
		"SPCN",
		"TRAN",
	}