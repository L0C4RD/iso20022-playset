import base_types
import Max4Text
import Exemption2Code
import AttestationValue1Code

class Exemption2(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_Val", "_RsnNotHnrd"]
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

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	@property
	def RsnNotHnrd(self):
		return self._RsnNotHnrd

	@RsnNotHnrd.setter
	def RsnNotHnrd(self, value):
		self._RsnNotHnrd = value if type(value) != auto else self.make_default("RsnNotHnrd")

	@RsnNotHnrd.deleter
	def RsnNotHnrd(self):
		del self._RsnNotHnrd
		self._RsnNotHnrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=Exemption2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=AttestationValue1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsnNotHnrd', type=Max4Text, min=0, max=None, mutex_group=None, array=True),
	))

