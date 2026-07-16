# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMReconciliationResponseV01

class CAAM_016_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.016.001.01"
		_docname = "caam.016.001.01"

		__slots__ = ["_ATMRcncltnRspn"]
		@property
		def ATMRcncltnRspn(self):
			return self._ATMRcncltnRspn

		@ATMRcncltnRspn.setter
		def ATMRcncltnRspn(self, value):
			self._ATMRcncltnRspn = value if value is not None else base_types.UninitialisedField(self, 'ATMRcncltnRspn', ATMReconciliationResponseV01, False)

		@ATMRcncltnRspn.deleter
		def ATMRcncltnRspn(self):
			del self._ATMRcncltnRspn
			self._ATMRcncltnRspn = base_types.UninitialisedField(self, 'ATMRcncltnRspn', ATMReconciliationResponseV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRcncltnRspn', type=ATMReconciliationResponseV01, min=1, max=1, mutex_group=None, array=False),
		))