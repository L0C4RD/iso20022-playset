# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class BeneficiaryCertificationType4Code(base_types._BaseDataType_String):

	_values = {
		"ACCI",
		"DOMI",
		"NDOM",
		"FULL",
		"NCOM",
		"QIBB",
		"TRBD",
		"PAPW",
		"PABD",
		"FRAC",
	}