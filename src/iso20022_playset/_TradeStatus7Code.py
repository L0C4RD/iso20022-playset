# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TradeStatus7Code(base_types._BaseDataType_String):

	_values = {
		"INVA",
		"UMTC",
		"FMTC",
		"SMAT",
		"SUSP",
		"SMAP",
		"PFIX",
		"FUMT",
	}