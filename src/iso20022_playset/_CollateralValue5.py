# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import AmountOrCoefficientPrice2Choice
from . import ForeignExchangeTerms23
from . import ISODate
from . import PercentageRate
from . import PriceRateOrAmount6Choice
from . import SecurityIdentification19

class CollateralValue5(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrst", "_CleanPric", "_ClsLkHrcut", "_FX", "_Hrcut", "_PoolFctr", "_SctyId", "_ValtnCcy", "_ValtnClsLkPric", "_ValtnDt", "_ValtnPric"]
	@property
	def AcrdIntrst(self):
		return self._AcrdIntrst

	@AcrdIntrst.setter
	def AcrdIntrst(self, value):
		self._AcrdIntrst = value if value is not None else base_types.UninitialisedField(self, 'AcrdIntrst', PriceRateOrAmount6Choice, False)

	@AcrdIntrst.deleter
	def AcrdIntrst(self):
		del self._AcrdIntrst
		self._AcrdIntrst = base_types.UninitialisedField(self, 'AcrdIntrst', PriceRateOrAmount6Choice, False)

	@property
	def CleanPric(self):
		return self._CleanPric

	@CleanPric.setter
	def CleanPric(self, value):
		self._CleanPric = value if value is not None else base_types.UninitialisedField(self, 'CleanPric', PriceRateOrAmount6Choice, False)

	@CleanPric.deleter
	def CleanPric(self):
		del self._CleanPric
		self._CleanPric = base_types.UninitialisedField(self, 'CleanPric', PriceRateOrAmount6Choice, False)

	@property
	def ClsLkHrcut(self):
		return self._ClsLkHrcut

	@ClsLkHrcut.setter
	def ClsLkHrcut(self, value):
		self._ClsLkHrcut = value if value is not None else base_types.UninitialisedField(self, 'ClsLkHrcut', PercentageRate, False)

	@ClsLkHrcut.deleter
	def ClsLkHrcut(self):
		del self._ClsLkHrcut
		self._ClsLkHrcut = base_types.UninitialisedField(self, 'ClsLkHrcut', PercentageRate, False)

	@property
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if value is not None else base_types.UninitialisedField(self, 'FX', ForeignExchangeTerms23, False)

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = base_types.UninitialisedField(self, 'FX', ForeignExchangeTerms23, False)

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if value is not None else base_types.UninitialisedField(self, 'Hrcut', PercentageRate, False)

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = base_types.UninitialisedField(self, 'Hrcut', PercentageRate, False)

	@property
	def PoolFctr(self):
		return self._PoolFctr

	@PoolFctr.setter
	def PoolFctr(self, value):
		self._PoolFctr = value if value is not None else base_types.UninitialisedField(self, 'PoolFctr', PercentageRate, False)

	@PoolFctr.deleter
	def PoolFctr(self):
		del self._PoolFctr
		self._PoolFctr = base_types.UninitialisedField(self, 'PoolFctr', PercentageRate, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification19, False)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification19, False)

	@property
	def ValtnCcy(self):
		return self._ValtnCcy

	@ValtnCcy.setter
	def ValtnCcy(self, value):
		self._ValtnCcy = value if value is not None else base_types.UninitialisedField(self, 'ValtnCcy', ActiveCurrencyCode, False)

	@ValtnCcy.deleter
	def ValtnCcy(self):
		del self._ValtnCcy
		self._ValtnCcy = base_types.UninitialisedField(self, 'ValtnCcy', ActiveCurrencyCode, False)

	@property
	def ValtnClsLkPric(self):
		return self._ValtnClsLkPric

	@ValtnClsLkPric.setter
	def ValtnClsLkPric(self, value):
		self._ValtnClsLkPric = value if value is not None else base_types.UninitialisedField(self, 'ValtnClsLkPric', AmountOrCoefficientPrice2Choice, False)

	@ValtnClsLkPric.deleter
	def ValtnClsLkPric(self):
		del self._ValtnClsLkPric
		self._ValtnClsLkPric = base_types.UninitialisedField(self, 'ValtnClsLkPric', AmountOrCoefficientPrice2Choice, False)

	@property
	def ValtnDt(self):
		return self._ValtnDt

	@ValtnDt.setter
	def ValtnDt(self, value):
		self._ValtnDt = value if value is not None else base_types.UninitialisedField(self, 'ValtnDt', ISODate, False)

	@ValtnDt.deleter
	def ValtnDt(self):
		del self._ValtnDt
		self._ValtnDt = base_types.UninitialisedField(self, 'ValtnDt', ISODate, False)

	@property
	def ValtnPric(self):
		return self._ValtnPric

	@ValtnPric.setter
	def ValtnPric(self, value):
		self._ValtnPric = value if value is not None else base_types.UninitialisedField(self, 'ValtnPric', AmountOrCoefficientPrice2Choice, False)

	@ValtnPric.deleter
	def ValtnPric(self):
		del self._ValtnPric
		self._ValtnPric = base_types.UninitialisedField(self, 'ValtnPric', AmountOrCoefficientPrice2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcrdIntrst', type=PriceRateOrAmount6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CleanPric', type=PriceRateOrAmount6Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsLkHrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FX', type=ForeignExchangeTerms23, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Hrcut', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolFctr', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnCcy', type=ActiveCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnClsLkPric', type=AmountOrCoefficientPrice2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValtnPric', type=AmountOrCoefficientPrice2Choice, min=1, max=1, mutex_group=None, array=False),
	))