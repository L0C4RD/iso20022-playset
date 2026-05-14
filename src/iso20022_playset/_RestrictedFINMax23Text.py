# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RestrictedFINMax23Text(base_types._BaseDataType_String):

	_max = 23
	_min = 1
	_pattern = r"([^/]+/)+([^/]+)|([^/]*)"