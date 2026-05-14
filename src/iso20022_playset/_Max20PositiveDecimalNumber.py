# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Max20PositiveDecimalNumber(base_types._BaseDataType_Decimal):

	_max_totaldigits = 20
	_max_fractiondigits = 2
	_min_inclusive = 0