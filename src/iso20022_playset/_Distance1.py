from . import base_types
from ._UnitOfMeasure10Code import UnitOfMeasure10Code
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max10NumericText import Max10NumericText

class Distance1(base_types._BaseFieldType):

	__slots__ = ["_OdmtrRtr", "_FreeDstnc", "_OdmtrStart", "_Rate", "_TtlDstnc", "_UnitOfMeasr"]
	@property
	def OdmtrRtr(self):
		return self._OdmtrRtr

	@OdmtrRtr.setter
	def OdmtrRtr(self, value):
		self._OdmtrRtr = value if type(value) != base_types.auto else self.make_default("OdmtrRtr")

	@OdmtrRtr.deleter
	def OdmtrRtr(self):
		del self._OdmtrRtr
		self._OdmtrRtr = None

	@property
	def FreeDstnc(self):
		return self._FreeDstnc

	@FreeDstnc.setter
	def FreeDstnc(self, value):
		self._FreeDstnc = value if type(value) != base_types.auto else self.make_default("FreeDstnc")

	@FreeDstnc.deleter
	def FreeDstnc(self):
		del self._FreeDstnc
		self._FreeDstnc = None

	@property
	def OdmtrStart(self):
		return self._OdmtrStart

	@OdmtrStart.setter
	def OdmtrStart(self, value):
		self._OdmtrStart = value if type(value) != base_types.auto else self.make_default("OdmtrStart")

	@OdmtrStart.deleter
	def OdmtrStart(self):
		del self._OdmtrStart
		self._OdmtrStart = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def TtlDstnc(self):
		return self._TtlDstnc

	@TtlDstnc.setter
	def TtlDstnc(self, value):
		self._TtlDstnc = value if type(value) != base_types.auto else self.make_default("TtlDstnc")

	@TtlDstnc.deleter
	def TtlDstnc(self):
		del self._TtlDstnc
		self._TtlDstnc = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != base_types.auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OdmtrRtr', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FreeDstnc', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OdmtrStart', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlDstnc', type=Max10NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure10Code, min=0, max=1, mutex_group=None, array=False),
	))

