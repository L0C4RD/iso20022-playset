import base_types
import Frequency6Code
import DecimalNumber

class FrequencyPeriod1(base_types._BaseFieldType):

	__slots__ = ["_CntPerPrd", "_Tp"]
	@property
	def CntPerPrd(self):
		return self._CntPerPrd

	@CntPerPrd.setter
	def CntPerPrd(self, value):
		self._CntPerPrd = value if type(value) != auto else self.make_default("CntPerPrd")

	@CntPerPrd.deleter
	def CntPerPrd(self):
		del self._CntPerPrd
		self._CntPerPrd = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntPerPrd', type=DecimalNumber, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Frequency6Code, min=1, max=1, mutex_group=None, array=False),
	))

