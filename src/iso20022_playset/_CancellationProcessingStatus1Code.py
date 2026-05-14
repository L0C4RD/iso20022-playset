# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CancellationProcessingStatus1Code(base_types._BaseDataType_String):

	_values = {
		"CAND",
		"CANP",
		"DEND",
		"EXCH",
		"INTE",
		"PACK",
		"PARF",
		"REJT",
		"REPR",
	}