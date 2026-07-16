# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATMReconciliationAdviceV03

class CAAM_009_001_03():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:caam.009.001.03"
		_docname = "caam.009.001.03"

		__slots__ = ["_ATMRcncltnAdvc"]
		@property
		def ATMRcncltnAdvc(self):
			return self._ATMRcncltnAdvc

		@ATMRcncltnAdvc.setter
		def ATMRcncltnAdvc(self, value):
			self._ATMRcncltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'ATMRcncltnAdvc', ATMReconciliationAdviceV03, False)

		@ATMRcncltnAdvc.deleter
		def ATMRcncltnAdvc(self):
			del self._ATMRcncltnAdvc
			self._ATMRcncltnAdvc = base_types.UninitialisedField(self, 'ATMRcncltnAdvc', ATMReconciliationAdviceV03, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMRcncltnAdvc', type=ATMReconciliationAdviceV03, min=1, max=1, mutex_group=None, array=False),
		))