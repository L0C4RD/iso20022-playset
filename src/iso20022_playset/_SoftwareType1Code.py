# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class SoftwareType1Code(base_types._BaseDataType_String):

	_values = {
		"MFFW",
		"MFSW",
		"APSW",
		"OTHP",
		"OTHN",
	}