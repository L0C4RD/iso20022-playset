# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InterestPaymentRequestV05

class COLR_013_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:colr.013.001.05"
		_docname = "colr.013.001.05"

		__slots__ = ["_IntrstPmtReq"]
		@property
		def IntrstPmtReq(self):
			return self._IntrstPmtReq

		@IntrstPmtReq.setter
		def IntrstPmtReq(self, value):
			self._IntrstPmtReq = value if value is not None else base_types.UninitialisedField(self, 'IntrstPmtReq', InterestPaymentRequestV05, False)

		@IntrstPmtReq.deleter
		def IntrstPmtReq(self):
			del self._IntrstPmtReq
			self._IntrstPmtReq = base_types.UninitialisedField(self, 'IntrstPmtReq', InterestPaymentRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntrstPmtReq', type=InterestPaymentRequestV05, min=1, max=1, mutex_group=None, array=False),
		))