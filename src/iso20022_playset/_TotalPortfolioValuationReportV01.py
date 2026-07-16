# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Pagination
from . import PortfolioBalance1
from . import Report4
from . import SecuritiesAccount21
from . import SupplementaryData1
from . import TotalPortfolioValuation1

class TotalPortfolioValuationReportV01(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_Bal", "_Pgntn", "_RptGnlDtls", "_SplmtryData", "_TtlPrtflValtn"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', SecuritiesAccount21, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', SecuritiesAccount21, False)

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', PortfolioBalance1, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', PortfolioBalance1, False)

	@property
	def Pgntn(self):
		return self._Pgntn

	@Pgntn.setter
	def Pgntn(self, value):
		self._Pgntn = value if value is not None else base_types.UninitialisedField(self, 'Pgntn', Pagination, False)

	@Pgntn.deleter
	def Pgntn(self):
		del self._Pgntn
		self._Pgntn = base_types.UninitialisedField(self, 'Pgntn', Pagination, False)

	@property
	def RptGnlDtls(self):
		return self._RptGnlDtls

	@RptGnlDtls.setter
	def RptGnlDtls(self, value):
		self._RptGnlDtls = value if value is not None else base_types.UninitialisedField(self, 'RptGnlDtls', Report4, False)

	@RptGnlDtls.deleter
	def RptGnlDtls(self):
		del self._RptGnlDtls
		self._RptGnlDtls = base_types.UninitialisedField(self, 'RptGnlDtls', Report4, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, False)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, False)

	@property
	def TtlPrtflValtn(self):
		return self._TtlPrtflValtn

	@TtlPrtflValtn.setter
	def TtlPrtflValtn(self, value):
		self._TtlPrtflValtn = value if value is not None else base_types.UninitialisedField(self, 'TtlPrtflValtn', TotalPortfolioValuation1, False)

	@TtlPrtflValtn.deleter
	def TtlPrtflValtn(self):
		del self._TtlPrtflValtn
		self._TtlPrtflValtn = base_types.UninitialisedField(self, 'TtlPrtflValtn', TotalPortfolioValuation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount21, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=PortfolioBalance1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pgntn', type=Pagination, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptGnlDtls', type=Report4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlPrtflValtn', type=TotalPortfolioValuation1, min=1, max=1, mutex_group=None, array=False),
	))