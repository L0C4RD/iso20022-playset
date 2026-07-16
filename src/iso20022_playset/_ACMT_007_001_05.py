# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountOpeningRequestV05

class ACMT_007_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:acmt.007.001.05"
		_docname = "acmt.007.001.05"

		__slots__ = ["_AcctOpngReq"]
		@property
		def AcctOpngReq(self):
			return self._AcctOpngReq

		@AcctOpngReq.setter
		def AcctOpngReq(self, value):
			self._AcctOpngReq = value if value is not None else base_types.UninitialisedField(self, 'AcctOpngReq', AccountOpeningRequestV05, False)

		@AcctOpngReq.deleter
		def AcctOpngReq(self):
			del self._AcctOpngReq
			self._AcctOpngReq = base_types.UninitialisedField(self, 'AcctOpngReq', AccountOpeningRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AcctOpngReq', type=AccountOpeningRequestV05, min=1, max=1, mutex_group=None, array=False),
		))