# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class PendingProcessingReason8Code(base_types._BaseDataType_String):

	_values = {
		"BLOC",
		"ADEA",
		"MINO",
		"MUNO",
		"NEXT",
		"OTHR",
		"DENO",
		"CERT",
	}