# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class GeographicPointInDecimalDegreesText(base_types._BaseDataType_String):

	_max = 27
	_pattern = r"(\+|-)?[\d]{1,3}(\.[\d]{1,8})?/(\+|-)?[\d]{1,3}(\.[\d]{1,8})?"