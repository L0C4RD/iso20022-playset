# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvoicePaymentReconciliationStatusV01 import InvoicePaymentReconciliationStatusV01

class TSMT_054_001_01():

	class Document(base_types._BaseFieldType):

		attrib = {
			"xmlns" : "urn:iso:std:iso:20022:tech:xsd:tsmt.054.001.01",
		}

		_attrib_defs = frozenset((
			base_types.AttributeEntry(name='xmlns', type=xs:string, required=True),
		))

		__slots__ = ["_InvcPmtRcncltnSts"]
		@property
		def InvcPmtRcncltnSts(self):
			return self._InvcPmtRcncltnSts

		@InvcPmtRcncltnSts.setter
		def InvcPmtRcncltnSts(self, value):
			self._InvcPmtRcncltnSts = value if type(value) != base_types.auto else self.make_default("InvcPmtRcncltnSts")

		@InvcPmtRcncltnSts.deleter
		def InvcPmtRcncltnSts(self):
			del self._InvcPmtRcncltnSts
			self._InvcPmtRcncltnSts = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcPmtRcncltnSts', type=InvoicePaymentReconciliationStatusV01, min=1, max=1, mutex_group=None, array=False),
		))