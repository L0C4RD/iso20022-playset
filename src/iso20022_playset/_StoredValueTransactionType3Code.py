# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class StoredValueTransactionType3Code(base_types._BaseDataType_String):

	_values = {
		"ACTV",
		"DUPL",
		"LOAD",
		"RESV",
		"REVS",
		"ULOA",
		"CLOS",
		"DCTV",
		"OPEN",
		"BALC",
	}