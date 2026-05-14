from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._PercentageRate import PercentageRate
from ._PriceType2 import PriceType2
from ._PriceValueChange1 import PriceValueChange1
from ._StatisticsByPredefinedTimePeriods2 import StatisticsByPredefinedTimePeriods2
from ._StatisticsByUserDefinedTimePeriod3 import StatisticsByUserDefinedTimePeriod3

class ValuationStatistics4(base_types._BaseFieldType):

	__slots__ = ["_ByPrdfndTmPrds", "_ByUsrDfndTmPrd", "_Ccy", "_PricChng", "_PricTpChngBsis", "_Yld"]
	@property
	def ByPrdfndTmPrds(self):
		return self._ByPrdfndTmPrds

	@ByPrdfndTmPrds.setter
	def ByPrdfndTmPrds(self, value):
		self._ByPrdfndTmPrds = value if type(value) != base_types.auto else self.make_default("ByPrdfndTmPrds")

	@ByPrdfndTmPrds.deleter
	def ByPrdfndTmPrds(self):
		del self._ByPrdfndTmPrds
		self._ByPrdfndTmPrds = None

	@property
	def ByUsrDfndTmPrd(self):
		return self._ByUsrDfndTmPrd

	@ByUsrDfndTmPrd.setter
	def ByUsrDfndTmPrd(self, value):
		self._ByUsrDfndTmPrd = value if type(value) != base_types.auto else self.make_default("ByUsrDfndTmPrd")

	@ByUsrDfndTmPrd.deleter
	def ByUsrDfndTmPrd(self):
		del self._ByUsrDfndTmPrd
		self._ByUsrDfndTmPrd = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def PricChng(self):
		return self._PricChng

	@PricChng.setter
	def PricChng(self, value):
		self._PricChng = value if type(value) != base_types.auto else self.make_default("PricChng")

	@PricChng.deleter
	def PricChng(self):
		del self._PricChng
		self._PricChng = None

	@property
	def PricTpChngBsis(self):
		return self._PricTpChngBsis

	@PricTpChngBsis.setter
	def PricTpChngBsis(self, value):
		self._PricTpChngBsis = value if type(value) != base_types.auto else self.make_default("PricTpChngBsis")

	@PricTpChngBsis.deleter
	def PricTpChngBsis(self):
		del self._PricTpChngBsis
		self._PricTpChngBsis = None

	@property
	def Yld(self):
		return self._Yld

	@Yld.setter
	def Yld(self, value):
		self._Yld = value if type(value) != base_types.auto else self.make_default("Yld")

	@Yld.deleter
	def Yld(self):
		del self._Yld
		self._Yld = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ByPrdfndTmPrds', type=StatisticsByPredefinedTimePeriods2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ByUsrDfndTmPrd', type=StatisticsByUserDefinedTimePeriod3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricChng', type=PriceValueChange1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricTpChngBsis', type=PriceType2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Yld', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))

