from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._Max15NumericText import Max15NumericText

class CashDeposit1(base_types._BaseFieldType):

	__slots__ = ["_NbOfNotes", "_Amt", "_NoteDnmtn"]
	@property
	def NbOfNotes(self):
		return self._NbOfNotes

	@NbOfNotes.setter
	def NbOfNotes(self, value):
		self._NbOfNotes = value if type(value) != base_types.auto else self.make_default("NbOfNotes")

	@NbOfNotes.deleter
	def NbOfNotes(self):
		del self._NbOfNotes
		self._NbOfNotes = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def NoteDnmtn(self):
		return self._NoteDnmtn

	@NoteDnmtn.setter
	def NoteDnmtn(self, value):
		self._NoteDnmtn = value if type(value) != base_types.auto else self.make_default("NoteDnmtn")

	@NoteDnmtn.deleter
	def NoteDnmtn(self):
		del self._NoteDnmtn
		self._NoteDnmtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfNotes', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoteDnmtn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

