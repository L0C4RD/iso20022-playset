# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Max10KText(base_types._BaseDataType_String):

	_max = 10000
	_min = 1