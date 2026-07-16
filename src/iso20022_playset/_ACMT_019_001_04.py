# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountClosingRequestV04

class ACMT_019_001_04():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.019.001.04"
		_docname = "acmt.019.001.04"

		__slots__ = ["_AcctClsgReq"]
		@property
		def AcctClsgReq(self):
			return self._AcctClsgReq

		@AcctClsgReq.setter
		def AcctClsgReq(self, value):
			self._AcctClsgReq = value if value is not None else base_types.UninitialisedField(self, 'AcctClsgReq', AccountClosingRequestV04, False)

		@AcctClsgReq.deleter
		def AcctClsgReq(self):
			del self._AcctClsgReq
			self._AcctClsgReq = base_types.UninitialisedField(self, 'AcctClsgReq', AccountClosingRequestV04, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctClsgReq', type=AccountClosingRequestV04, min=1, max=1, mutex_group=None, array=False),
		))