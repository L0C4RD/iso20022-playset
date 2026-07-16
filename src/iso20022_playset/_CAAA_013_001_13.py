# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorDiagnosticRequestV13

class CAAA_013_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.013.001.13"
		_docname = "caaa.013.001.13"

		__slots__ = ["_AccptrDgnstcReq"]
		@property
		def AccptrDgnstcReq(self):
			return self._AccptrDgnstcReq

		@AccptrDgnstcReq.setter
		def AccptrDgnstcReq(self, value):
			self._AccptrDgnstcReq = value if value is not None else base_types.UninitialisedField(self, 'AccptrDgnstcReq', AcceptorDiagnosticRequestV13, False)

		@AccptrDgnstcReq.deleter
		def AccptrDgnstcReq(self):
			del self._AccptrDgnstcReq
			self._AccptrDgnstcReq = base_types.UninitialisedField(self, 'AccptrDgnstcReq', AcceptorDiagnosticRequestV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrDgnstcReq', type=AcceptorDiagnosticRequestV13, min=1, max=1, mutex_group=None, array=False),
		))