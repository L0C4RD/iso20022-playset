from . import base_types
from ._InvoiceTaxReportV01 import InvoiceTaxReportV01

class AUTH_034_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_InvcTaxRpt"]
		@property
		def InvcTaxRpt(self):
			return self._InvcTaxRpt

		@InvcTaxRpt.setter
		def InvcTaxRpt(self, value):
			self._InvcTaxRpt = value if type(value) != base_types.auto else self.make_default("InvcTaxRpt")

		@InvcTaxRpt.deleter
		def InvcTaxRpt(self):
			del self._InvcTaxRpt
			self._InvcTaxRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='InvcTaxRpt', type=InvoiceTaxReportV01, min=1, max=1, mutex_group=None, array=False),
		))

