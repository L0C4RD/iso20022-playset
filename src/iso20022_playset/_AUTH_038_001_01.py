# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvoiceTaxReportStatusAdviceV01

class AUTH_038_001_01():

	class Document(base_types._BaseFieldType_Document):

		_xmlns = "urn:iso:std:iso:20022:tech:xsd:auth.038.001.01"
		_docname = "auth.038.001.01"

		__slots__ = ["_InvcTaxRptStsAdvc"]
		@property
		def InvcTaxRptStsAdvc(self):
			return self._InvcTaxRptStsAdvc

		@InvcTaxRptStsAdvc.setter
		def InvcTaxRptStsAdvc(self, value):
			self._InvcTaxRptStsAdvc = value if value is not None else base_types.UninitialisedField(self, 'InvcTaxRptStsAdvc', InvoiceTaxReportStatusAdviceV01, False)

		@InvcTaxRptStsAdvc.deleter
		def InvcTaxRptStsAdvc(self):
			del self._InvcTaxRptStsAdvc
			self._InvcTaxRptStsAdvc = base_types.UninitialisedField(self, 'InvcTaxRptStsAdvc', InvoiceTaxReportStatusAdviceV01, False)

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcTaxRptStsAdvc', type=InvoiceTaxReportStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))