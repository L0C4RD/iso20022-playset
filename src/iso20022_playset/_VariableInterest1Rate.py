from . import base_types
from ._Max35Text import Max35Text
from ._Number import Number

class VariableInterest1Rate(base_types._BaseFieldType):

	__slots__ = ["_BsisPtSprd", "_Indx"]
	@property
	def BsisPtSprd(self):
		return self._BsisPtSprd

	@BsisPtSprd.setter
	def BsisPtSprd(self, value):
		self._BsisPtSprd = value if type(value) != base_types.auto else self.make_default("BsisPtSprd")

	@BsisPtSprd.deleter
	def BsisPtSprd(self):
		del self._BsisPtSprd
		self._BsisPtSprd = None

	@property
	def Indx(self):
		return self._Indx

	@Indx.setter
	def Indx(self, value):
		self._Indx = value if type(value) != base_types.auto else self.make_default("Indx")

	@Indx.deleter
	def Indx(self):
		del self._Indx
		self._Indx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsisPtSprd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Indx', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

