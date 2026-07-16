# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MissingOrIncorrectData1
from . import TrueFalseIndicator
from . import YesNoIndicator

class UnableToApplyJustification4Choice(base_types._BaseFieldType):

	__slots__ = ["_AnyInf", "_MssngOrIncrrctInf", "_PssblDplctInstr"]
	@property
	def AnyInf(self):
		return self._AnyInf

	@AnyInf.setter
	def AnyInf(self, value):
		self._AnyInf = value if value is not None else base_types.UninitialisedField(self, 'AnyInf', YesNoIndicator, False)

	@AnyInf.deleter
	def AnyInf(self):
		del self._AnyInf
		self._AnyInf = base_types.UninitialisedField(self, 'AnyInf', YesNoIndicator, False)

	@property
	def MssngOrIncrrctInf(self):
		return self._MssngOrIncrrctInf

	@MssngOrIncrrctInf.setter
	def MssngOrIncrrctInf(self, value):
		self._MssngOrIncrrctInf = value if value is not None else base_types.UninitialisedField(self, 'MssngOrIncrrctInf', MissingOrIncorrectData1, False)

	@MssngOrIncrrctInf.deleter
	def MssngOrIncrrctInf(self):
		del self._MssngOrIncrrctInf
		self._MssngOrIncrrctInf = base_types.UninitialisedField(self, 'MssngOrIncrrctInf', MissingOrIncorrectData1, False)

	@property
	def PssblDplctInstr(self):
		return self._PssblDplctInstr

	@PssblDplctInstr.setter
	def PssblDplctInstr(self, value):
		self._PssblDplctInstr = value if value is not None else base_types.UninitialisedField(self, 'PssblDplctInstr', TrueFalseIndicator, False)

	@PssblDplctInstr.deleter
	def PssblDplctInstr(self):
		del self._PssblDplctInstr
		self._PssblDplctInstr = base_types.UninitialisedField(self, 'PssblDplctInstr', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AnyInf', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='MssngOrIncrrctInf', type=MissingOrIncorrectData1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PssblDplctInstr', type=TrueFalseIndicator, min=0, max=1, mutex_group=1, array=False),
	))