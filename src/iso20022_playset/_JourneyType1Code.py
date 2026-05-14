# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class JourneyType1Code(base_types._BaseDataType_String):

	_values = {
		"COAC",
		"EARL",
		"FLGT",
		"LATE",
		"ONTM",
		"OTHR",
		"TRAN",
		"VESS",
	}