# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class UnmatchedReason16Code(base_types._BaseDataType_String):

	_values = {
		"NCRR",
		"DSEC",
		"DQUA",
		"CMIS",
		"DEPT",
		"ICAG",
		"ICUS",
		"IEXE",
		"DMON",
		"DDAT",
		"DTRD",
		"DELN",
	}