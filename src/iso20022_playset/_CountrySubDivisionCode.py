# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class CountrySubDivisionCode(base_types._BaseDataType_String):

	_pattern = r"[A-Z]{2,2}\-[0-9A-Z]{1,3}"