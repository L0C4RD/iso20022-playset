# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMPINManagementRequestV03

class CATP_010_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03"
		_docname = "catp.010.001.03"

		__slots__ = ["_ATMPINMgmtReq"]
		@property
		def ATMPINMgmtReq(self):
			return self._ATMPINMgmtReq

		@ATMPINMgmtReq.setter
		def ATMPINMgmtReq(self, value):
			self._ATMPINMgmtReq = value if value is not None else base_types.UninitialisedField(self, 'ATMPINMgmtReq', ATMPINManagementRequestV03, False)

		@ATMPINMgmtReq.deleter
		def ATMPINMgmtReq(self):
			del self._ATMPINMgmtReq
			self._ATMPINMgmtReq = base_types.UninitialisedField(self, 'ATMPINMgmtReq', ATMPINManagementRequestV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMPINMgmtReq', type=ATMPINManagementRequestV03, min=1, max=1, mutex_group=None, array=False),
		))