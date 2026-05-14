from . import base_types
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._AmountOrCoefficientPrice2Choice import AmountOrCoefficientPrice2Choice
from ._ForeignExchangeTerms23 import ForeignExchangeTerms23
from ._ISODate import ISODate
from ._PercentageRate import PercentageRate
from ._PriceRateOrAmount6Choice import PriceRateOrAmount6Choice
from ._SecurityIdentification19 import SecurityIdentification19

class CollateralValue5(base_types._BaseFieldType):

	__slots__ = ["_AcrdIntrst", "_CleanPric", "_ClsLkHrcut", "_FX", "_Hrcut", "_PoolFctr", "_SctyId", "_ValtnCcy", "_ValtnClsLkPric", "_ValtnDt", "_ValtnPric"]
	@property
	def AcrdIntrst(self):
		return self._AcrdIntrst

	@AcrdIntrst.setter
	def AcrdIntrst(self, value):
		self._AcrdIntrst = value if type(value) != base_types.auto else self.make_default("AcrdIntrst")

	@AcrdIntrst.deleter
	def AcrdIntrst(self):
		del self._AcrdIntrst
		self._AcrdIntrst = None

	@property
	def CleanPric(self):
		return self._CleanPric

	@CleanPric.setter
	def CleanPric(self, value):
		self._CleanPric = value if type(value) != base_types.auto else self.make_default("CleanPric")

	@CleanPric.deleter
	def CleanPric(self):
		del self._CleanPric
		self._CleanPric = None

	@property
	def ClsLkHrcut(self):
		return self._ClsLkHrcut

	@ClsLkHrcut.setter
	def ClsLkHrcut(self, value):
		self._ClsLkHrcut = value if type(value) != base_types.auto else self.make_default("ClsLkHrcut")

	@ClsLkHrcut.deleter
	def ClsLkHrcut(self):
		del self._ClsLkHrcut
		self._ClsLkHrcut = None

	@property
	def FX(self):
		return self._FX

	@FX.setter
	def FX(self, value):
		self._FX = value if type(value) != base_types.auto else self.make_default("FX")

	@FX.deleter
	def FX(self):
		del self._FX
		self._FX = None

	@property
	def Hrcut(self):
		return self._Hrcut

	@Hrcut.setter
	def Hrcut(self, value):
		self._Hrcut = value if type(value) != base_types.auto else self.make_default("Hrcut")

	@Hrcut.deleter
	def Hrcut(self):
		del self._Hrcut
		self._Hrcut = None

	@property
	def PoolFctr(self):
		return self._PoolFctr

	@PoolFctr.setter
	def PoolFctr(self, value):
		self._PoolFctr = value if type(value) != base_types.auto else self.make_default("PoolFctr")

	@PoolFctr.deleter
	def PoolFctr(self):
		del self._PoolFctr
		self._PoolFctr = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	@property
	def ValtnCcy(self):
		return self._ValtnCcy

	@ValtnCcy.setter
	def ValtnCcy(self, value):
		self._ValtnCcy = value if type(value) != base_types.auto else self.make_default("ValtnCcy")

	@ValtnCcy.deleter
	def ValtnCcy(self):
		del self._ValtnCcy
		self._ValtnCcy = None

	@property
	def ValtnClsLkPric(self):
		return self._ValtnClsLkPric

	@ValtnClsLkPric.setter
	def ValtnClsLkPric(self, value):
		self._ValtnClsLkPric = value if type(value) != base_types.auto else self.make_default("ValtnClsLkPric")

	@ValtnClsLkPric.deleter
	def ValtnClsLkPric(self):
		del self._ValtnClsLkPric
		self._ValtnClsLkPric = None

	@property
	def ValtnDt(self):
		return self._ValtnDt

	@ValtnDt.setter
	def ValtnDt(self, value):
		self._ValtnDt = value if type(value) != base_types.auto else self.make_default("ValtnDt")

	@ValtnDt.deleter
	def ValtnDt(self):
		del self._ValtnDt
		self._ValtnDt = None

	@property
	def ValtnPric(self):
		return self._ValtnPric

	@ValtnPric.setter
	def ValtnPric(self, value):
		self._ValtnPric = value if type(value) != base_types.auto else self.make_default("ValtnPric")

	@ValtnPric.deleter
	def ValtnPric(self):
		del self._ValtnPric
		self._ValtnPric = None

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

