# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Unlimited9Text(base_types._BaseDataType_String):

	_length = 9
	_pattern = r"UNLIMITED"