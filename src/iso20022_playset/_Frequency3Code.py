# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Frequency3Code(base_types._BaseDataType_String):

	_values = {
		"YEAR",
		"MNTH",
		"QURT",
		"MIAN",
		"WEEK",
		"DAIL",
		"TEND",
	}