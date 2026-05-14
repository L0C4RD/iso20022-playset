# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CertificateType2Code(base_types._BaseDataType_String):

	_values = {
		"AMLC",
		"DVLC",
		"DFOR",
		"GOST",
		"IDEN",
		"INCU",
		"LREF",
		"PASS",
		"PRAD",
		"PKIC",
	}