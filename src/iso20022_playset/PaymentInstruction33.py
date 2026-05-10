import base_types
import DateTimePeriod1Choice
import Instruction1Code
import PaymentType4Choice
import Priority1Choice

class PaymentInstruction33(base_types._BaseFieldType):

	__slots__ = ["_Prty", "_Instr", "_PrcgVldtyTm", "_Tp"]
	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def Instr(self):
		return self._Instr

	@Instr.setter
	def Instr(self, value):
		self._Instr = value if type(value) != auto else self.make_default("Instr")

	@Instr.deleter
	def Instr(self):
		del self._Instr
		self._Instr = None

	@property
	def PrcgVldtyTm(self):
		return self._PrcgVldtyTm

	@PrcgVldtyTm.setter
	def PrcgVldtyTm(self, value):
		self._PrcgVldtyTm = value if type(value) != auto else self.make_default("PrcgVldtyTm")

	@PrcgVldtyTm.deleter
	def PrcgVldtyTm(self):
		del self._PrcgVldtyTm
		self._PrcgVldtyTm = None

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
		base_types.FieldEntry(name='Prty', type=Priority1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Instr', type=Instruction1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgVldtyTm', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PaymentType4Choice, min=0, max=1, mutex_group=None, array=False),
	))

