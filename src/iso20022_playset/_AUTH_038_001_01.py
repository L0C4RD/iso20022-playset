# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._InvoiceTaxReportStatusAdviceV01 import InvoiceTaxReportStatusAdviceV01

class AUTH_038_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InvcTaxRptStsAdvc"]
		@property
		def InvcTaxRptStsAdvc(self):
			return self._InvcTaxRptStsAdvc

		@InvcTaxRptStsAdvc.setter
		def InvcTaxRptStsAdvc(self, value):
			self._InvcTaxRptStsAdvc = value if type(value) != base_types.auto else self.make_default("InvcTaxRptStsAdvc")

		@InvcTaxRptStsAdvc.deleter
		def InvcTaxRptStsAdvc(self):
			del self._InvcTaxRptStsAdvc
			self._InvcTaxRptStsAdvc = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcTaxRptStsAdvc', type=InvoiceTaxReportStatusAdviceV01, min=1, max=1, mutex_group=None, array=False),
		))