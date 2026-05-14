# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ExchangePolicy2Code(base_types._BaseDataType_String):

	_values = {
		"ONDM",
		"IMMD",
		"ASAP",
		"AGRP",
		"NBLT",
		"TTLT",
		"CYCL",
		"NONE",
		"BLCK",
	}