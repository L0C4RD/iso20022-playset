# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class OptionEventType1Code(base_types._BaseDataType_String):

	_values = {
		"CLST",
		"CONF",
		"KNIN",
		"KNOC",
		"OTHR",
		"TRIG",
	}