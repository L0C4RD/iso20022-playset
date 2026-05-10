from . import base_types
from .TrueFalseIndicator import TrueFalseIndicator
from .YesNoIndicator import YesNoIndicator
from .MissingOrIncorrectData1 import MissingOrIncorrectData1

class UnableToApplyJustification4Choice(base_types._BaseFieldType):

	__slots__ = ["_MssngOrIncrrctInf", "_PssblDplctInstr", "_AnyInf"]
	@property
	def MssngOrIncrrctInf(self):
		return self._MssngOrIncrrctInf

	@MssngOrIncrrctInf.setter
	def MssngOrIncrrctInf(self, value):
		self._MssngOrIncrrctInf = value if type(value) != base_types.auto else self.make_default("MssngOrIncrrctInf")

	@MssngOrIncrrctInf.deleter
	def MssngOrIncrrctInf(self):
		del self._MssngOrIncrrctInf
		self._MssngOrIncrrctInf = None

	@property
	def PssblDplctInstr(self):
		return self._PssblDplctInstr

	@PssblDplctInstr.setter
	def PssblDplctInstr(self, value):
		self._PssblDplctInstr = value if type(value) != base_types.auto else self.make_default("PssblDplctInstr")

	@PssblDplctInstr.deleter
	def PssblDplctInstr(self):
		del self._PssblDplctInstr
		self._PssblDplctInstr = None

	@property
	def AnyInf(self):
		return self._AnyInf

	@AnyInf.setter
	def AnyInf(self, value):
		self._AnyInf = value if type(value) != base_types.auto else self.make_default("AnyInf")

	@AnyInf.deleter
	def AnyInf(self):
		del self._AnyInf
		self._AnyInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MssngOrIncrrctInf', type=MissingOrIncorrectData1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PssblDplctInstr', type=TrueFalseIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AnyInf', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
	))

