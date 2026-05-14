# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class Authorisation1Code(base_types._BaseDataType_String):

	_values = {
		"AUTH",
		"FDET",
		"FSUM",
		"ILEV",
	}