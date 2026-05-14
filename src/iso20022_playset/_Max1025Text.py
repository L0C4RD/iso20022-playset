# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Max1025Text(base_types._BaseDataType_String):

	_max = 1025
	_min = 1