# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CancelledStatusReason16Code(base_types._BaseDataType_String):

	_max = 4
	_min = 1
	_values = {
		"SCEX",
		"OTHR",
		"CXLR",
		"BYIY",
		"CTHP",
		"CANZ",
		"CANT",
		"CSUB",
		"CANS",
		"CANI",
		"CORP",
	}