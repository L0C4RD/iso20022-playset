from . import base_types
from .SecuritiesAccount21 import SecuritiesAccount21
from .TotalPortfolioValuation1 import TotalPortfolioValuation1
from .PortfolioBalance1 import PortfolioBalance1
from .SupplementaryData1 import SupplementaryData1
from .Pagination import Pagination
from .Report4 import Report4

class TotalPortfolioValuationReportV01(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_RptGnlDtls", "_Pgntn", "_AcctDtls", "_TtlPrtflValtn", "_SplmtryData"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if type(value) != auto else self.make_default("RptGnlDtls")

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = None

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if type(value) != auto else self.make_default("Pgntn")

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = None

	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def TtlPrtflValtn(self):
		return self._TtlPrtflValtn

	@TtlPrtflValtn.setter
	def TtlPrtflValtn(self, value):
		self._TtlPrtflValtn = value if type(value) != auto else self.make_default("TtlPrtflValtn")

	@TtlPrtflValtn.deleter
	def TtlPrtflValtn(self):
		del self._TtlPrtflValtn
		self._TtlPrtflValtn = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=PortfolioBalance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGnlDtls', type=Report4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount21, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPrtflValtn', type=TotalPortfolioValuation1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=1, mutex_group=None, array=False),
	))

