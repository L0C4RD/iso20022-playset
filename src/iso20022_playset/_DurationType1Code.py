# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class DurationType1Code(base_types._BaseDataType_String):

	_values = {
		"YEAR",
		"WEEK",
		"SEAS",
		"QURT",
		"MNTH",
		"MNUT",
		"HOUR",
		"DASD",
		"OTHR",
	}