# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class DayOfMonthNumber(base_types._BaseDataType_Decimal):

	_min_inclusive = 1
	_max_inclusive = 31