# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class SettlementDate8Code(base_types._BaseDataType_String):

	_values = {
		"ASAP",
		"ENDC",
		"CASH",
		"CLEA",
		"MONT",
		"FUTU",
		"PRVD",
		"REGU",
		"SAVE",
		"SELL",
		"TBAT",
		"TFIV",
		"TFOR",
		"TONE",
		"TTRE",
		"TTWO",
		"WHIF",
		"WDIS",
		"WISS",
		"WHID",
	}