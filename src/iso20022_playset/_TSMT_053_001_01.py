# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvoicePaymentReconciliationAdviceV01

class TSMT_053_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:tsmt.053.001.01"
		_docname = "tsmt.053.001.01"

		__slots__ = ["_InvcPmtRcncltnAdvc"]
		@property
		def InvcPmtRcncltnAdvc(self):
			return self._InvcPmtRcncltnAdvc

		@InvcPmtRcncltnAdvc.setter
		def InvcPmtRcncltnAdvc(self, value):
			self._InvcPmtRcncltnAdvc = value if value is not None else base_types.UninitialisedField(self, 'InvcPmtRcncltnAdvc', InvoicePaymentReconciliationAdviceV01, False)

		@InvcPmtRcncltnAdvc.deleter
		def InvcPmtRcncltnAdvc(self):
			del self._InvcPmtRcncltnAdvc
			self._InvcPmtRcncltnAdvc = base_types.UninitialisedField(self, 'InvcPmtRcncltnAdvc', InvoicePaymentReconciliationAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcPmtRcncltnAdvc', type=InvoicePaymentReconciliationAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))