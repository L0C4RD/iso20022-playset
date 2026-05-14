# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class EncryptionFormat3Code(base_types._BaseDataType_String):

	_values = {
		"TR34",
		"TR31",
		"CTCE",
		"CBCE",
	}