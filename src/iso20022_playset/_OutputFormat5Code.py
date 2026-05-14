# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class OutputFormat5Code(base_types._BaseDataType_String):

	_values = {
		"OTHN",
		"OTHP",
		"TEXT",
		"URLI",
		"HTML",
		"PLIN",
		"JSON",
		"XMLF",
		"EDIF",
		"CSVF",
		"JPEG",
		"PDFF",
		"PNGF",
		"SVGF",
	}