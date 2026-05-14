# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PhoneNumber(base_types._BaseDataType_String):

	_pattern = r"\+[0-9]{1,3}-[0-9()+\-]{1,30}"