# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class EventToNotify2Code(base_types._BaseDataType_String):

	_values = {
		"ABRT",
		"MAIB",
		"CRDI",
		"COMP",
		"CRDR",
		"CUSL",
		"MAIE",
		"INIT",
		"KEYP",
		"MAIR",
		"OODR",
		"SADM",
		"SWUP",
		"SECA",
		"SHUT",
		"SASS",
		"DISC",
		"CNTN",
		"TNOK",
		"TNKO",
	}