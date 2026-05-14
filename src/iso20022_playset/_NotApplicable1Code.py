# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class NotApplicable1Code(base_types._BaseDataType_String):

	_max = 4
	_min = 0
	_values = {
		"NOAP",
	}