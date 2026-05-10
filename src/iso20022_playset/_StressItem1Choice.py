from . import base_types
from ._RiskFactor1 import RiskFactor1
from ._Strategy1 import Strategy1
from ._StressedProduct1 import StressedProduct1

class StressItem1Choice(base_types._BaseFieldType):

	__slots__ = ["_Pdct", "_RskFctr", "_Strtgy"]
	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if type(value) != base_types.auto else self.make_default("Pdct")

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = None

	@property
	def RskFctr(self):
		return self._RskFctr

	@RskFctr.setter
	def RskFctr(self, value):
		self._RskFctr = value if type(value) != base_types.auto else self.make_default("RskFctr")

	@RskFctr.deleter
	def RskFctr(self):
		del self._RskFctr
		self._RskFctr = None

	@property
	def Strtgy(self):
		return self._Strtgy

	@Strtgy.setter
	def Strtgy(self, value):
		self._Strtgy = value if type(value) != base_types.auto else self.make_default("Strtgy")

	@Strtgy.deleter
	def Strtgy(self):
		del self._Strtgy
		self._Strtgy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Pdct', type=StressedProduct1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RskFctr', type=RiskFactor1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Strtgy', type=Strategy1, min=0, max=1, mutex_group=1, array=False),
	))

