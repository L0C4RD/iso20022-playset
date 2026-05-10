from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .TaxReport1 import TaxReport1
from .TaxReportHeader1 import TaxReportHeader1

class InvoiceTaxReportV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_InvcTaxRptHdr", "_TaxRpt"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def InvcTaxRptHdr(self):
		return self._InvcTaxRptHdr

	@InvcTaxRptHdr.setter
	def InvcTaxRptHdr(self, value):
		self._InvcTaxRptHdr = value if type(value) != base_types.auto else self.make_default("InvcTaxRptHdr")

	@InvcTaxRptHdr.deleter
	def InvcTaxRptHdr(self):
		del self._InvcTaxRptHdr
		self._InvcTaxRptHdr = None

	@property
	def TaxRpt(self):
		return self._TaxRpt

	@TaxRpt.setter
	def TaxRpt(self, value):
		self._TaxRpt = value if type(value) != base_types.auto else self.make_default("TaxRpt")

	@TaxRpt.deleter
	def TaxRpt(self):
		del self._TaxRpt
		self._TaxRpt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InvcTaxRptHdr', type=TaxReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRpt', type=TaxReport1, min=1, max=None, mutex_group=None, array=True),
	))

