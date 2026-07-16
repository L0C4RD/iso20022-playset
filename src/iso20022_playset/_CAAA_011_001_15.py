# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorBatchTransferV15

class CAAA_011_001_15():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.011.001.15"
		_docname = "caaa.011.001.15"

		__slots__ = ["_AccptrBtchTrf"]
		@property
		def AccptrBtchTrf(self):
			return self._AccptrBtchTrf

		@AccptrBtchTrf.setter
		def AccptrBtchTrf(self, value):
			self._AccptrBtchTrf = value if value is not None else base_types.UninitialisedField(self, 'AccptrBtchTrf', AcceptorBatchTransferV15, False)

		@AccptrBtchTrf.deleter
		def AccptrBtchTrf(self):
			del self._AccptrBtchTrf
			self._AccptrBtchTrf = base_types.UninitialisedField(self, 'AccptrBtchTrf', AcceptorBatchTransferV15, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrBtchTrf', type=AcceptorBatchTransferV15, min=1, max=1, mutex_group=None, array=False),
		))