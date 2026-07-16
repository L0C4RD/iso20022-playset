# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorDiagnosticResponseV13

class CAAA_014_001_13():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.014.001.13"
		_docname = "caaa.014.001.13"

		__slots__ = ["_AccptrDgnstcRspn"]
		@property
		def AccptrDgnstcRspn(self):
			return self._AccptrDgnstcRspn

		@AccptrDgnstcRspn.setter
		def AccptrDgnstcRspn(self, value):
			self._AccptrDgnstcRspn = value if value is not None else base_types.UninitialisedField(self, 'AccptrDgnstcRspn', AcceptorDiagnosticResponseV13, False)

		@AccptrDgnstcRspn.deleter
		def AccptrDgnstcRspn(self):
			del self._AccptrDgnstcRspn
			self._AccptrDgnstcRspn = base_types.UninitialisedField(self, 'AccptrDgnstcRspn', AcceptorDiagnosticResponseV13, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrDgnstcRspn', type=AcceptorDiagnosticResponseV13, min=1, max=1, mutex_group=None, array=False),
		))