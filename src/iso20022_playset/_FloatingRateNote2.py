from . import base_types
from ._ISINOct2015Identifier import ISINOct2015Identifier
from ._Number import Number

class FloatingRateNote2(base_types._BaseFieldType):

	__slots__ = ["_BsisPtSprd", "_RefRateIndx"]
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
	def RefRateIndx(self):
		return self._RefRateIndx

	@RefRateIndx.setter
	def RefRateIndx(self, value):
		self._RefRateIndx = value if type(value) != base_types.auto else self.make_default("RefRateIndx")

	@RefRateIndx.deleter
	def RefRateIndx(self):
		del self._RefRateIndx
		self._RefRateIndx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BsisPtSprd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefRateIndx', type=ISINOct2015Identifier, min=1, max=1, mutex_group=None, array=False),
	))

