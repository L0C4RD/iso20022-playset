# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMReconciliationRequestV01

class CAAM_015_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.015.001.01"
		_docname = "caam.015.001.01"

		__slots__ = ["_ATMRcncltnReq"]
		@property
		def ATMRcncltnReq(self):
			return self._ATMRcncltnReq

		@ATMRcncltnReq.setter
		def ATMRcncltnReq(self, value):
			self._ATMRcncltnReq = value if value is not None else base_types.UninitialisedField(self, 'ATMRcncltnReq', ATMReconciliationRequestV01, False)

		@ATMRcncltnReq.deleter
		def ATMRcncltnReq(self):
			del self._ATMRcncltnReq
			self._ATMRcncltnReq = base_types.UninitialisedField(self, 'ATMRcncltnReq', ATMReconciliationRequestV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRcncltnReq', type=ATMReconciliationRequestV01, min=1, max=1, mutex_group=None, array=False),
		))