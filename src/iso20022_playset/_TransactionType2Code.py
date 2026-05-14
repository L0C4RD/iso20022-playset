# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TransactionType2Code(base_types._BaseDataType_String):

	_values = {
		"REDM",
		"SUBS",
		"SSPL",
		"RWPL",
		"TRIN",
		"TOUT",
		"SWII",
		"SWIO",
		"SUAA",
		"REAA",
	}