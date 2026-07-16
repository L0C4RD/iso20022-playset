# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvoiceTaxReportV01

class AUTH_034_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.034.001.01"
		_docname = "auth.034.001.01"

		__slots__ = ["_InvcTaxRpt"]
		@property
		def InvcTaxRpt(self):
			return self._InvcTaxRpt

		@InvcTaxRpt.setter
		def InvcTaxRpt(self, value):
			self._InvcTaxRpt = value if value is not None else base_types.UninitialisedField(self, 'InvcTaxRpt', InvoiceTaxReportV01, False)

		@InvcTaxRpt.deleter
		def InvcTaxRpt(self):
			del self._InvcTaxRpt
			self._InvcTaxRpt = base_types.UninitialisedField(self, 'InvcTaxRpt', InvoiceTaxReportV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcTaxRpt', type=InvoiceTaxReportV01, min=1, max=1, mutex_group=None, array=False),
		))