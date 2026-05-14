# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class ProductIdentifier2Code(base_types._BaseDataType_String):

	_values = {
		"BINR",
		"COMD",
		"EANC",
		"HRTR",
		"MANI",
		"MODL",
		"PART",
		"QOTA",
		"STYL",
		"SUPI",
		"UPCC",
	}