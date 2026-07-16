# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMDepositRequestV02

class CATP_012_001_02():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:catp.012.001.02"
		_docname = "catp.012.001.02"

		__slots__ = ["_ATMDpstReq"]
		@property
		def ATMDpstReq(self):
			return self._ATMDpstReq

		@ATMDpstReq.setter
		def ATMDpstReq(self, value):
			self._ATMDpstReq = value if value is not None else base_types.UninitialisedField(self, 'ATMDpstReq', ATMDepositRequestV02, False)

		@ATMDpstReq.deleter
		def ATMDpstReq(self):
			del self._ATMDpstReq
			self._ATMDpstReq = base_types.UninitialisedField(self, 'ATMDpstReq', ATMDepositRequestV02, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDpstReq', type=ATMDepositRequestV02, min=1, max=1, mutex_group=None, array=False),
		))