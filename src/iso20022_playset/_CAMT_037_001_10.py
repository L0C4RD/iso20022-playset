# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DebitAuthorisationRequestV10

class CAMT_037_001_10():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:camt.037.001.10"
		_docname = "camt.037.001.10"

		__slots__ = ["_DbtAuthstnReq"]
		@property
		def DbtAuthstnReq(self):
			return self._DbtAuthstnReq

		@DbtAuthstnReq.setter
		def DbtAuthstnReq(self, value):
			self._DbtAuthstnReq = value if value is not None else base_types.UninitialisedField(self, 'DbtAuthstnReq', DebitAuthorisationRequestV10, False)

		@DbtAuthstnReq.deleter
		def DbtAuthstnReq(self):
			del self._DbtAuthstnReq
			self._DbtAuthstnReq = base_types.UninitialisedField(self, 'DbtAuthstnReq', DebitAuthorisationRequestV10, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='DbtAuthstnReq', type=DebitAuthorisationRequestV10, min=1, max=1, mutex_group=None, array=False),
		))