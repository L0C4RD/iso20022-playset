# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PaymentType3Code(base_types._BaseDataType_String):

	_values = {
		"CBS",
		"BCK",
		"BAL",
		"CLS",
		"CTR",
		"CBH",
		"CBP",
		"DPG",
		"DPN",
		"EXP",
		"TCH",
		"LMT",
		"LIQ",
		"DPP",
		"DPH",
		"DPS",
		"STF",
		"TRP",
		"TCS",
		"LOA",
		"LOR",
		"TCP",
		"OND",
		"MGL",
	}