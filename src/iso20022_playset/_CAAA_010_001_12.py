# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcceptorReconciliationResponseV12

class CAAA_010_001_12():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caaa.010.001.12"
		_docname = "caaa.010.001.12"

		__slots__ = ["_AccptrRcncltnRspn"]
		@property
		def AccptrRcncltnRspn(self):
			return self._AccptrRcncltnRspn

		@AccptrRcncltnRspn.setter
		def AccptrRcncltnRspn(self, value):
			self._AccptrRcncltnRspn = value if value is not None else base_types.UninitialisedField(self, 'AccptrRcncltnRspn', AcceptorReconciliationResponseV12, False)

		@AccptrRcncltnRspn.deleter
		def AccptrRcncltnRspn(self):
			del self._AccptrRcncltnRspn
			self._AccptrRcncltnRspn = base_types.UninitialisedField(self, 'AccptrRcncltnRspn', AcceptorReconciliationResponseV12, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrRcncltnRspn', type=AcceptorReconciliationResponseV12, min=1, max=1, mutex_group=None, array=False),
		))