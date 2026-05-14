# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TradeCertificateType1Code(base_types._BaseDataType_String):

	_values = {
		"ANLY",
		"QUAL",
		"QUAN",
		"WEIG",
		"ORIG",
		"HEAL",
		"PHYT",
	}