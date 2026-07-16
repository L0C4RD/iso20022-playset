# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ReconciliationResponseV05

class CAAD_006_001_05():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caad.006.001.05"
		_docname = "caad.006.001.05"

		__slots__ = ["_RcncltnRspn"]
		@property
		def RcncltnRspn(self):
			return self._RcncltnRspn

		@RcncltnRspn.setter
		def RcncltnRspn(self, value):
			self._RcncltnRspn = value if value is not None else base_types.UninitialisedField(self, 'RcncltnRspn', ReconciliationResponseV05, False)

		@RcncltnRspn.deleter
		def RcncltnRspn(self):
			del self._RcncltnRspn
			self._RcncltnRspn = base_types.UninitialisedField(self, 'RcncltnRspn', ReconciliationResponseV05, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='RcncltnRspn', type=ReconciliationResponseV05, min=1, max=1, mutex_group=None, array=False),
		))