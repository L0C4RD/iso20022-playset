# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountClosingAmendmentRequestV04

class ACMT_020_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.020.001.04"
		_docname = "acmt.020.001.04"

		__slots__ = ["_AcctClsgAmdmntReq"]
		@property
		def AcctClsgAmdmntReq(self):
			return self._AcctClsgAmdmntReq

		@AcctClsgAmdmntReq.setter
		def AcctClsgAmdmntReq(self, value):
			self._AcctClsgAmdmntReq = value if value is not None else base_types.UninitialisedField(self, 'AcctClsgAmdmntReq', AccountClosingAmendmentRequestV04, False)

		@AcctClsgAmdmntReq.deleter
		def AcctClsgAmdmntReq(self):
			del self._AcctClsgAmdmntReq
			self._AcctClsgAmdmntReq = base_types.UninitialisedField(self, 'AcctClsgAmdmntReq', AccountClosingAmendmentRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctClsgAmdmntReq', type=AccountClosingAmendmentRequestV04, min=1, max=1, mutex_group=None, array=False),
		))