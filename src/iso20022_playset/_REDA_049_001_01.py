# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountLinkCreationRequestV01

class REDA_049_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:reda.049.001.01"
		_docname = "reda.049.001.01"

		__slots__ = ["_AcctLkCreReq"]
		@property
		def AcctLkCreReq(self):
			return self._AcctLkCreReq

		@AcctLkCreReq.setter
		def AcctLkCreReq(self, value):
			self._AcctLkCreReq = value if value is not None else base_types.UninitialisedField(self, 'AcctLkCreReq', AccountLinkCreationRequestV01, False)

		@AcctLkCreReq.deleter
		def AcctLkCreReq(self):
			del self._AcctLkCreReq
			self._AcctLkCreReq = base_types.UninitialisedField(self, 'AcctLkCreReq', AccountLinkCreationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctLkCreReq', type=AccountLinkCreationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))