# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PeriodUnit3Code(base_types._BaseDataType_String):

	_values = {
		"OTHP",
		"OTHN",
		"MNTH",
		"WEEK",
		"YEAR",
		"DAYS",
		"EXDY",
	}