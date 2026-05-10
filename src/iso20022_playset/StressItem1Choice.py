import base_types
import StressedProduct1
import Strategy1
import RiskFactor1

class StressItem1Choice(base_types._BaseFieldType):

	__slots__ = ["_Strtgy", "_RskFctr", "_Pdct"]
	@property
	def Strtgy(self):
		return self._Strtgy

	@Strtgy.setter
	def Strtgy(self, value):
		self._Strtgy = value if type(value) != auto else self.make_default("Strtgy")

	@Strtgy.deleter
	def Strtgy(self):
		del self._Strtgy
		self._Strtgy = None

	@property
	def RskFctr(self):
		return self._RskFctr

	@RskFctr.setter
	def RskFctr(self, value):
		self._RskFctr = value if type(value) != auto else self.make_default("RskFctr")

	@RskFctr.deleter
	def RskFctr(self):
		del self._RskFctr
		self._RskFctr = None

	@property
	def Pdct(self):
		return self._Pdct

	@Pdct.setter
	def Pdct(self, value):
		self._Pdct = value if type(value) != auto else self.make_default("Pdct")

	@Pdct.deleter
	def Pdct(self):
		del self._Pdct
		self._Pdct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Strtgy', type=Strategy1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RskFctr', type=RiskFactor1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Pdct', type=StressedProduct1, min=0, max=1, mutex_group=1, array=False),
	))

