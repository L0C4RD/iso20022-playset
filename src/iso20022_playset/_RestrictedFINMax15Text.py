# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class RestrictedFINMax15Text(base_types._BaseDataType_String):

	_max = 15
	_min = 1