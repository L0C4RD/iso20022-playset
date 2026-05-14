# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class EventFrequency5Code(base_types._BaseDataType_String):

	_values = {
		"YEAR",
		"SEMI",
		"QUTR",
		"MNTH",
		"WEEK",
		"DAIL",
		"CLOS",
		"TOMN",
		"TOWK",
		"TWMN",
	}