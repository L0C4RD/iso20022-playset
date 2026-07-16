# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SupplementaryData1
from . import TaxReport1
from . import TaxReportHeader1

class InvoiceTaxReportV01(base_types._BaseFieldType):

	__slots__ = ["_InvcTaxRptHdr", "_SplmtryData", "_TaxRpt"]
	@property
	def InvcTaxRptHdr(self):
		return self._InvcTaxRptHdr

	@InvcTaxRptHdr.setter
	def InvcTaxRptHdr(self, value):
		self._InvcTaxRptHdr = value if value is not None else base_types.UninitialisedField(self, 'InvcTaxRptHdr', TaxReportHeader1, False)

	@InvcTaxRptHdr.deleter
	def InvcTaxRptHdr(self):
		del self._InvcTaxRptHdr
		self._InvcTaxRptHdr = base_types.UninitialisedField(self, 'InvcTaxRptHdr', TaxReportHeader1, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def TaxRpt(self):
		return self._TaxRpt

	@TaxRpt.setter
	def TaxRpt(self, value):
		self._TaxRpt = value if value is not None else base_types.UninitialisedField(self, 'TaxRpt', TaxReport1, True)

	@TaxRpt.deleter
	def TaxRpt(self):
		del self._TaxRpt
		self._TaxRpt = base_types.UninitialisedField(self, 'TaxRpt', TaxReport1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvcTaxRptHdr', type=TaxReportHeader1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxRpt', type=TaxReport1, min=1, max=None, mutex_group=None, array=True),
	))