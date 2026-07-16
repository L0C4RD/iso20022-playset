# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountRequestAcknowledgementV04

class ACMT_010_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.010.001.04"
		_docname = "acmt.010.001.04"

		__slots__ = ["_AcctReqAck"]
		@property
		def AcctReqAck(self):
			return self._AcctReqAck

		@AcctReqAck.setter
		def AcctReqAck(self, value):
			self._AcctReqAck = value if value is not None else base_types.UninitialisedField(self, 'AcctReqAck', AccountRequestAcknowledgementV04, False)

		@AcctReqAck.deleter
		def AcctReqAck(self):
			del self._AcctReqAck
			self._AcctReqAck = base_types.UninitialisedField(self, 'AcctReqAck', AccountRequestAcknowledgementV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctReqAck', type=AccountRequestAcknowledgementV04, min=1, max=1, mutex_group=None, array=False),
		))