# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class BarcodeType1Code(base_types._BaseDataType_String):

	_values = {
		"COQR",
		"C128",
		"C025",
		"C039",
		"EA13",
		"EAN8",
		"P417",
		"UPCA",
	}