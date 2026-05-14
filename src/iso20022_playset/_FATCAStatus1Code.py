# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class FATCAStatus1Code(base_types._BaseDataType_String):

	_values = {
		"F101",
		"F102",
		"F103",
		"F104",
		"F105",
		"F201",
		"F202",
		"F203",
		"F204",
		"F205",
		"F206",
	}