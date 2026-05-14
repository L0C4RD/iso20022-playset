# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TypeOfAmount19Code(base_types._BaseDataType_String):

	_values = {
		"CONN",
		"INSU",
		"LNDS",
		"MISC",
		"OTHN",
		"OTHP",
		"USGE",
	}