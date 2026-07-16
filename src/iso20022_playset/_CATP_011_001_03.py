# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMPINManagementResponseV03

class CATP_011_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.011.001.03"
		_docname = "catp.011.001.03"

		__slots__ = ["_ATMPINMgmtRspn"]
		@property
		def ATMPINMgmtRspn(self):
			return self._ATMPINMgmtRspn

		@ATMPINMgmtRspn.setter
		def ATMPINMgmtRspn(self, value):
			self._ATMPINMgmtRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMPINMgmtRspn', ATMPINManagementResponseV03, False)

		@ATMPINMgmtRspn.deleter
		def ATMPINMgmtRspn(self):
			del self._ATMPINMgmtRspn
			self._ATMPINMgmtRspn = base_types.UninitialisedField(self, 'ATMPINMgmtRspn', ATMPINManagementResponseV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMPINMgmtRspn', type=ATMPINManagementResponseV03, min=1, max=1, mutex_group=None, array=False),
		))