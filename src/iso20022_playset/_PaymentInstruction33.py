# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateTimePeriod1Choice
from . import Instruction1Code
from . import PaymentType4Choice
from . import Priority1Choice

class PaymentInstruction33(base_types._BaseFieldType):

	__slots__ = ["_Instr", "_PrcgVldtyTm", "_Prty", "_Tp"]
	@property
	def Instr(self):
		return self._Instr

	@Instr.setter
	def Instr(self, value):
		self._Instr = value if value is not None else base_types.UninitialisedField(self, 'Instr', Instruction1Code, False)

	@Instr.deleter
	def Instr(self):
		del self._Instr
		self._Instr = base_types.UninitialisedField(self, 'Instr', Instruction1Code, False)

	@property
	def PrcgVldtyTm(self):
		return self._PrcgVldtyTm

	@PrcgVldtyTm.setter
	def PrcgVldtyTm(self, value):
		self._PrcgVldtyTm = value if value is not None else base_types.UninitialisedField(self, 'PrcgVldtyTm', DateTimePeriod1Choice, False)

	@PrcgVldtyTm.deleter
	def PrcgVldtyTm(self):
		del self._PrcgVldtyTm
		self._PrcgVldtyTm = base_types.UninitialisedField(self, 'PrcgVldtyTm', DateTimePeriod1Choice, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', Priority1Choice, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', Priority1Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', PaymentType4Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', PaymentType4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Instr', type=Instruction1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgVldtyTm', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=Priority1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PaymentType4Choice, min=0, max=1, mutex_group=None, array=False),
	))