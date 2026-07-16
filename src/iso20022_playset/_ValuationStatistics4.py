# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyCode
from . import PercentageRate
from . import PriceType2
from . import PriceValueChange1
from . import StatisticsByPredefinedTimePeriods2
from . import StatisticsByUserDefinedTimePeriod3

class ValuationStatistics4(base_types._BaseFieldType):

	__slots__ = ["_ByPrdfndTmPrds", "_ByUsrDfndTmPrd", "_Ccy", "_PricChng", "_PricTpChngBsis", "_Yld"]
	@property
	def ByPrdfndTmPrds(self):
		return self._ByPrdfndTmPrds

	@ByPrdfndTmPrds.setter
	def ByPrdfndTmPrds(self, value):
		self._ByPrdfndTmPrds = value if value is not None else base_types.UninitialisedField(self, 'ByPrdfndTmPrds', StatisticsByPredefinedTimePeriods2, False)

	@ByPrdfndTmPrds.deleter
	def ByPrdfndTmPrds(self):
		del self._ByPrdfndTmPrds
		self._ByPrdfndTmPrds = base_types.UninitialisedField(self, 'ByPrdfndTmPrds', StatisticsByPredefinedTimePeriods2, False)

	@property
	def ByUsrDfndTmPrd(self):
		return self._ByUsrDfndTmPrd

	@ByUsrDfndTmPrd.setter
	def ByUsrDfndTmPrd(self, value):
		self._ByUsrDfndTmPrd = value if value is not None else base_types.UninitialisedField(self, 'ByUsrDfndTmPrd', StatisticsByUserDefinedTimePeriod3, True)

	@ByUsrDfndTmPrd.deleter
	def ByUsrDfndTmPrd(self):
		del self._ByUsrDfndTmPrd
		self._ByUsrDfndTmPrd = base_types.UninitialisedField(self, 'ByUsrDfndTmPrd', StatisticsByUserDefinedTimePeriod3, True)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ActiveOrHistoricCurrencyCode, False)

	@property
	def PricChng(self):
		return self._PricChng

	@PricChng.setter
	def PricChng(self, value):
		self._PricChng = value if value is not None else base_types.UninitialisedField(self, 'PricChng', PriceValueChange1, False)

	@PricChng.deleter
	def PricChng(self):
		del self._PricChng
		self._PricChng = base_types.UninitialisedField(self, 'PricChng', PriceValueChange1, False)

	@property
	def PricTpChngBsis(self):
		return self._PricTpChngBsis

	@PricTpChngBsis.setter
	def PricTpChngBsis(self, value):
		self._PricTpChngBsis = value if value is not None else base_types.UninitialisedField(self, 'PricTpChngBsis', PriceType2, False)

	@PricTpChngBsis.deleter
	def PricTpChngBsis(self):
		del self._PricTpChngBsis
		self._PricTpChngBsis = base_types.UninitialisedField(self, 'PricTpChngBsis', PriceType2, False)

	@property
	def Yld(self):
		return self._Yld

	@Yld.setter
	def Yld(self, value):
		self._Yld = value if value is not None else base_types.UninitialisedField(self, 'Yld', PercentageRate, False)

	@Yld.deleter
	def Yld(self):
		del self._Yld
		self._Yld = base_types.UninitialisedField(self, 'Yld', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ByPrdfndTmPrds', type=StatisticsByPredefinedTimePeriods2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ByUsrDfndTmPrd', type=StatisticsByUserDefinedTimePeriod3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricChng', type=PriceValueChange1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricTpChngBsis', type=PriceType2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Yld', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
	))