# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class SettlementDate5Code(base_types._BaseDataType_String):

	_values = {
		"REGU",
		"CASH",
		"NXTD",
		"TONE",
		"TTWO",
		"TTRE",
		"TFOR",
		"TFIV",
		"SELL",
		"WDIS",
		"WHID",
		"TBAT",
		"WISS",
	}