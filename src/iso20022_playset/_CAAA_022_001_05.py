# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorNonFinancialRequestV05

class CAAA_022_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.022.001.05"
		_docname = "caaa.022.001.05"

		__slots__ = ["_AccptrNonFinReq"]
		@property
		def AccptrNonFinReq(self):
			return self._AccptrNonFinReq

		@AccptrNonFinReq.setter
		def AccptrNonFinReq(self, value):
			self._AccptrNonFinReq = value if value is not None else base_types.UninitialisedField(self, 'AccptrNonFinReq', AcceptorNonFinancialRequestV05, False)

		@AccptrNonFinReq.deleter
		def AccptrNonFinReq(self):
			del self._AccptrNonFinReq
			self._AccptrNonFinReq = base_types.UninitialisedField(self, 'AccptrNonFinReq', AcceptorNonFinancialRequestV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrNonFinReq', type=AcceptorNonFinancialRequestV05, min=1, max=1, mutex_group=None, array=False),
		))