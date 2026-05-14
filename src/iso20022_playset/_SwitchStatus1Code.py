# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class SwitchStatus1Code(base_types._BaseDataType_String):

	_values = {
		"ACPT",
		"BTRQ",
		"BTRS",
		"COMP",
		"REDT",
		"REDE",
		"REJT",
		"REQU",
		"TMTN",
	}