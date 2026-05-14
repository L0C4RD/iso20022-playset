# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Max2Fraction1NonNegativeNumber(base_types._BaseDataType_Decimal):

	_max_totaldigits = 2
	_max_fractiondigits = 1
	_min_inclusive = 0
	_max_inclusive = 9.9