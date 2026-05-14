# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class QRCodeErrorCorrection1Code(base_types._BaseDataType_String):

	_values = {
		"M015",
		"Q025",
		"H030",
		"L007",
	}