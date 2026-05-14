# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Priority5Code(base_types._BaseDataType_String):

	_values = {
		"HIGH",
		"LOWW",
		"NORM",
		"URGT",
	}