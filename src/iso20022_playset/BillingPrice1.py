from . import base_types
from .Max20Text import Max20Text
from .ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from .AmountAndDirection34 import AmountAndDirection34
from .BillingChargeMethod1Code import BillingChargeMethod1Code

class BillingPrice1(base_types._BaseFieldType):

	__slots__ = ["_Ccy", "_Mtd", "_UnitPric", "_Rule"]
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
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if type(value) != auto else self.make_default("Mtd")

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def Rule(self):
		return self._Rule

	@Rule.setter
	def Rule(self, value):
		self._Rule = value if type(value) != auto else self.make_default("Rule")

	@Rule.deleter
	def Rule(self):
		del self._Rule
		self._Rule = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ccy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtd', type=BillingChargeMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rule', type=Max20Text, min=0, max=1, mutex_group=None, array=False),
	))

