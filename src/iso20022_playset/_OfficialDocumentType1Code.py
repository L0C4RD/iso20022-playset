# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class OfficialDocumentType1Code(base_types._BaseDataType_String):

	_values = {
		"ARNU",
		"AUTH",
		"DIPL",
		"DVLC",
		"EURO",
		"IDEN",
		"INTE",
		"INPO",
		"LZPR",
		"OTHN",
		"OTHP",
		"PASS",
		"VISA",
		"PERM",
		"REFU",
	}