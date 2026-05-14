# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ATMSecurityScheme3Code(base_types._BaseDataType_String):

	_values = {
		"APPK",
		"CERT",
		"FRAN",
		"DTCH",
		"LUXG",
		"MANU",
		"PKIP",
		"SIGN",
		"NONE",
		"TR34",
	}