# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TradeStatus6Code(base_types._BaseDataType_String):

	_values = {
		"INVA",
		"FMTC",
		"SMAP",
		"RJCT",
		"RSCD",
		"STLD",
		"SPLI",
		"UMTC",
		"SMAT",
		"FUMT",
		"NETT",
		"PFIX",
		"OMTC",
	}