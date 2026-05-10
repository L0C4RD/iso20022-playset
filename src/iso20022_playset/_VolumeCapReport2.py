from . import base_types
from .Max35Text import Max35Text
from .ISINOct2015Identifier import ISINOct2015Identifier
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode

class VolumeCapReport2(base_types._BaseFieldType):

	__slots__ = ["_TtlTradgVol", "_TtlRefPricTradgVol", "_Ccy", "_TtlNgtdTxsTradgVol", "_Id", "_TechRcrdId"]
	@property
	def TtlTradgVol(self):
		return self._TtlTradgVol

	@TtlTradgVol.setter
	def TtlTradgVol(self, value):
		self._TtlTradgVol = value if type(value) != base_types.auto else self.make_default("TtlTradgVol")

	@TtlTradgVol.deleter
	def TtlTradgVol(self):
		del self._TtlTradgVol
		self._TtlTradgVol = None

	@property
	def TtlRefPricTradgVol(self):
		return self._TtlRefPricTradgVol

	@TtlRefPricTradgVol.setter
	def TtlRefPricTradgVol(self, value):
		self._TtlRefPricTradgVol = value if type(value) != base_types.auto else self.make_default("TtlRefPricTradgVol")

	@TtlRefPricTradgVol.deleter
	def TtlRefPricTradgVol(self):
		del self._TtlRefPricTradgVol
		self._TtlRefPricTradgVol = None

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
	def TtlNgtdTxsTradgVol(self):
		return self._TtlNgtdTxsTradgVol

	@TtlNgtdTxsTradgVol.setter
	def TtlNgtdTxsTradgVol(self, value):
		self._TtlNgtdTxsTradgVol = value if type(value) != base_types.auto else self.make_default("TtlNgtdTxsTradgVol")

	@TtlNgtdTxsTradgVol.deleter
	def TtlNgtdTxsTradgVol(self):
		del self._TtlNgtdTxsTradgVol
		self._TtlNgtdTxsTradgVol = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def TechRcrdId(self):
		return self._TechRcrdId

	@TechRcrdId.setter
	def TechRcrdId(self, value):
		self._TechRcrdId = value if type(value) != base_types.auto else self.make_default("TechRcrdId")

	@TechRcrdId.deleter
	def TechRcrdId(self):
		del self._TechRcrdId
		self._TechRcrdId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlTradgVol', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlRefPricTradgVol', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlNgtdTxsTradgVol', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TechRcrdId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

