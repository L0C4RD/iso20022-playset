# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class SwapType1Code(base_types._BaseDataType_String):

	_values = {
		"OSSC",
		"XFSC",
		"XFMC",
		"XXSC",
		"XXMC",
		"IFMC",
		"FFSC",
		"FFMC",
		"IFSC",
		"OSMC",
	}