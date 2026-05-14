# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TransactionOperationType8Code(base_types._BaseDataType_String):

	_values = {
		"COMP",
		"CORR",
		"EROR",
		"MODI",
		"NEWT",
		"OTHR",
		"POSC",
		"REVI",
		"TERM",
		"VALU",
		"MARU",
	}