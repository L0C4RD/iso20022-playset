# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class BaselineStatus3Code(base_types._BaseDataType_String):

	_values = {
		"PROP",
		"CLSD",
		"PMTC",
		"ESTD",
		"ACTV",
		"COMP",
		"AMRQ",
		"RARQ",
		"CLRQ",
		"SCRQ",
		"SERQ",
		"DARQ",
	}