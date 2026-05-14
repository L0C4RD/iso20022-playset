# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RestrictedFINXMax210Text(base_types._BaseDataType_String):

	_max = 210
	_min = 1
	_pattern = r"[0-9a-zA-Z/\-\?:\(\)\.\n\r,'\+ ]{1,210}"