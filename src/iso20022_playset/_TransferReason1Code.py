# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types

class TransferReason1Code(base_types._BaseDataType_String):

	_values = {
		"TRAU",
		"TRAC",
		"TRAT",
		"TRAO",
		"TRAI",
		"TRAG",
		"TPLD",
		"TTDT",
		"TRPE",
		"TRAF",
		"TRAN",
	}