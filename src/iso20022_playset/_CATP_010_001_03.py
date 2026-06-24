# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMPINManagementRequestV03 import ATMPINManagementRequestV03

class CATP_010_001_03():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:catp.010.001.03",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_ATMPINMgmtReq"]
		@property
		def ATMPINMgmtReq(self):
			return self._ATMPINMgmtReq

		@ATMPINMgmtReq.setter
		def ATMPINMgmtReq(self, value):
			self._ATMPINMgmtReq = value if type(value) != base_types.auto else self.make_default("ATMPINMgmtReq")

		@ATMPINMgmtReq.deleter
		def ATMPINMgmtReq(self):
			del self._ATMPINMgmtReq
			self._ATMPINMgmtReq = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMPINMgmtReq', type=ATMPINManagementRequestV03, min=1, max=1, mutex_group=None, array=False),
		))