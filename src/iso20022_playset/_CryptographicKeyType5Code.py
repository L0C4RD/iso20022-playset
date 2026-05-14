# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CryptographicKeyType5Code(base_types._BaseDataType_String):

	_values = {
		"AES2",
		"EDE3",
		"DKP9",
		"AES9",
		"AES5",
		"EDE4",
		"UKA2",
		"UKA6",
		"RSAC",
		"ECCC",
		"DKAE",
		"UKA8",
	}