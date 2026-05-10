from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._AmountAndDirection102 import AmountAndDirection102
from ._Flows1 import Flows1
from ._Max10NumericText import Max10NumericText

class ConcentrationAccount1(base_types._BaseFieldType):

	__slots__ = ["_EndOfDay", "_InFlow", "_LatePmtConf", "_OutFlow", "_PeakCdt", "_PeakDbt"]
	@property
	def EndOfDay(self):
		return self._EndOfDay

	@EndOfDay.setter
	def EndOfDay(self, value):
		self._EndOfDay = value if type(value) != base_types.auto else self.make_default("EndOfDay")

	@EndOfDay.deleter
	def EndOfDay(self):
		del self._EndOfDay
		self._EndOfDay = None

	@property
	def InFlow(self):
		return self._InFlow

	@InFlow.setter
	def InFlow(self, value):
		self._InFlow = value if type(value) != base_types.auto else self.make_default("InFlow")

	@InFlow.deleter
	def InFlow(self):
		del self._InFlow
		self._InFlow = None

	@property
	def LatePmtConf(self):
		return self._LatePmtConf

	@LatePmtConf.setter
	def LatePmtConf(self, value):
		self._LatePmtConf = value if type(value) != base_types.auto else self.make_default("LatePmtConf")

	@LatePmtConf.deleter
	def LatePmtConf(self):
		del self._LatePmtConf
		self._LatePmtConf = None

	@property
	def OutFlow(self):
		return self._OutFlow

	@OutFlow.setter
	def OutFlow(self, value):
		self._OutFlow = value if type(value) != base_types.auto else self.make_default("OutFlow")

	@OutFlow.deleter
	def OutFlow(self):
		del self._OutFlow
		self._OutFlow = None

	@property
	def PeakCdt(self):
		return self._PeakCdt

	@PeakCdt.setter
	def PeakCdt(self, value):
		self._PeakCdt = value if type(value) != base_types.auto else self.make_default("PeakCdt")

	@PeakCdt.deleter
	def PeakCdt(self):
		del self._PeakCdt
		self._PeakCdt = None

	@property
	def PeakDbt(self):
		return self._PeakDbt

	@PeakDbt.setter
	def PeakDbt(self, value):
		self._PeakDbt = value if type(value) != base_types.auto else self.make_default("PeakDbt")

	@PeakDbt.deleter
	def PeakDbt(self):
		del self._PeakDbt
		self._PeakDbt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndOfDay', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InFlow', type=Flows1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LatePmtConf', type=Max10NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutFlow', type=Flows1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PeakCdt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PeakDbt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

