import base_types
import StatisticsByPredefinedTimePeriods2
import PriceType2
import PriceValueChange1
import ActiveOrHistoricCurrencyCode
import PercentageRate
import StatisticsByUserDefinedTimePeriod2

class ValuationStatistics3(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_PricTpChngBsis", "_PricChng", "_ByPrdfndTmPrds", "_Yld", "_ByUsrDfndTmPrd"]
	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def PricTpChngBsis(self):
		return self._PricTpChngBsis

	@PricTpChngBsis.setter
	def PricTpChngBsis(self, value):
		self._PricTpChngBsis = value if type(value) != auto else self.make_default("PricTpChngBsis")

	@PricTpChngBsis.deleter
	def PricTpChngBsis(self):
		del self._PricTpChngBsis
		self._PricTpChngBsis = None

	@property
	def PricChng(self):
		return self._PricChng

	@PricChng.setter
	def PricChng(self, value):
		self._PricChng = value if type(value) != auto else self.make_default("PricChng")

	@PricChng.deleter
	def PricChng(self):
		del self._PricChng
		self._PricChng = None

	@property
	def ByPrdfndTmPrds(self):
		return self._ByPrdfndTmPrds

	@ByPrdfndTmPrds.setter
	def ByPrdfndTmPrds(self, value):
		self._ByPrdfndTmPrds = value if type(value) != auto else self.make_default("ByPrdfndTmPrds")

	@ByPrdfndTmPrds.deleter
	def ByPrdfndTmPrds(self):
		del self._ByPrdfndTmPrds
		self._ByPrdfndTmPrds = None

	@property
	def Yld(self):
		return self._Yld

	@Yld.setter
	def Yld(self, value):
		self._Yld = value if type(value) != auto else self.make_default("Yld")

	@Yld.deleter
	def Yld(self):
		del self._Yld
		self._Yld = None

	@property
	def ByUsrDfndTmPrd(self):
		return self._ByUsrDfndTmPrd

	@ByUsrDfndTmPrd.setter
	def ByUsrDfndTmPrd(self, value):
		self._ByUsrDfndTmPrd = value if type(value) != auto else self.make_default("ByUsrDfndTmPrd")

	@ByUsrDfndTmPrd.deleter
	def ByUsrDfndTmPrd(self):
		del self._ByUsrDfndTmPrd
		self._ByUsrDfndTmPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricTpChngBsis', type=PriceType2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricChng', type=PriceValueChange1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ByPrdfndTmPrds', type=StatisticsByPredefinedTimePeriods2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Yld', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ByUsrDfndTmPrd', type=StatisticsByUserDefinedTimePeriod2, min=0, max=None, mutex_group=None, array=True),
	))

