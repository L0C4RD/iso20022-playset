from . import base_types
from ._PercentageRate import PercentageRate
from ._LongFraction19DecimalNumber import LongFraction19DecimalNumber
from ._BaseOneRate import BaseOneRate
from ._AmountAndDirection106 import AmountAndDirection106
from ._SecuritiesTransactionPrice5 import SecuritiesTransactionPrice5
from ._PriceStatus1Code import PriceStatus1Code

class SecuritiesTransactionPrice17Choice(base_types._BaseFieldType):

	__slots__ = ["_Othr", "_Yld", "_PdgPric", "_MntryVal", "_Pctg", "_Dcml", "_Unit"]
	@property
	def Dcml(self):
		return self._Dcml

	@Dcml.setter
	def Dcml(self, value):
		self._Dcml = value if type(value) != base_types.auto else self.make_default("Dcml")

	@Dcml.deleter
	def Dcml(self):
		del self._Dcml
		self._Dcml = None

	@property
	def MntryVal(self):
		return self._MntryVal

	@MntryVal.setter
	def MntryVal(self, value):
		self._MntryVal = value if type(value) != base_types.auto else self.make_default("MntryVal")

	@MntryVal.deleter
	def MntryVal(self):
		del self._MntryVal
		self._MntryVal = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != base_types.auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if type(value) != base_types.auto else self.make_default("Pctg")

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = None

	@property
	def PdgPric(self):
		return self._PdgPric

	@PdgPric.setter
	def PdgPric(self, value):
		self._PdgPric = value if type(value) != base_types.auto else self.make_default("PdgPric")

	@PdgPric.deleter
	def PdgPric(self):
		del self._PdgPric
		self._PdgPric = None

	@property
	def Unit(self):
		return self._Unit

	@Unit.setter
	def Unit(self, value):
		self._Unit = value if type(value) != base_types.auto else self.make_default("Unit")

	@Unit.deleter
	def Unit(self):
		del self._Unit
		self._Unit = None

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
		base_types.FieldEntry(name='Dcml', type=BaseOneRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MntryVal', type=AmountAndDirection106, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Othr', type=SecuritiesTransactionPrice5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PdgPric', type=PriceStatus1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Unit', type=LongFraction19DecimalNumber, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Yld', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
	))

