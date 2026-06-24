# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMPINManagementResponseV03 import ATMPINManagementResponseV03

class CATP_011_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : base_types.DataType_String(None, data="urn:iso:std:iso:20022:tech:xsd:catp.011.001.03"),
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=base_types.DataType_String, required=True),
		))

		__slots__ = ["_ATMPINMgmtRspn"]
		@property
		def ATMPINMgmtRspn(self):
			return self._ATMPINMgmtRspn

		@ATMPINMgmtRspn.setter
		def ATMPINMgmtRspn(self, value):
			self._ATMPINMgmtRspn = value if type(value) != base_types.auto else self.make_default("ATMPINMgmtRspn")

		@ATMPINMgmtRspn.deleter
		def ATMPINMgmtRspn(self):
			del self._ATMPINMgmtRspn
			self._ATMPINMgmtRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMPINMgmtRspn', type=ATMPINManagementResponseV03, min=1, max=1, mutex_group=None, array=False),
		))