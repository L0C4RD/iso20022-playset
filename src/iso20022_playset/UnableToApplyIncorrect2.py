import base_types
import IncorrectData1Choice
import Max140Text

class UnableToApplyIncorrect2(base_types._BaseFieldType):

	__slots__ = ["_AddtlIncrrctInf", "_Tp"]
	@property
	def AddtlIncrrctInf(self):
		return self._AddtlIncrrctInf

	@AddtlIncrrctInf.setter
	def AddtlIncrrctInf(self, value):
		self._AddtlIncrrctInf = value if type(value) != auto else self.make_default("AddtlIncrrctInf")

	@AddtlIncrrctInf.deleter
	def AddtlIncrrctInf(self):
		del self._AddtlIncrrctInf
		self._AddtlIncrrctInf = None

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
		base_types.FieldEntry(name='AddtlIncrrctInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=IncorrectData1Choice, min=1, max=1, mutex_group=None, array=False),
	))

