# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RejectionReason68Code(base_types._BaseDataType_String):

	_values = {
		"DSEC",
		"EVNM",
		"UKWN",
		"ICOL",
		"CONL",
		"ELIG",
		"INID",
		"OTHR",
	}