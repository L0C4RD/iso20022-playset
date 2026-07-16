# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import Max15NumericText

class CashDeposit1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_NbOfNotes", "_NoteDnmtn"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ActiveCurrencyAndAmount, False)

	@property
	def NbOfNotes(self):
		return self._NbOfNotes

	@NbOfNotes.setter
	def NbOfNotes(self, value):
		self._NbOfNotes = value if value is not None else base_types.UninitialisedField(self, 'NbOfNotes', Max15NumericText, False)

	@NbOfNotes.deleter
	def NbOfNotes(self):
		del self._NbOfNotes
		self._NbOfNotes = base_types.UninitialisedField(self, 'NbOfNotes', Max15NumericText, False)

	@property
	def NoteDnmtn(self):
		return self._NoteDnmtn

	@NoteDnmtn.setter
	def NoteDnmtn(self, value):
		self._NoteDnmtn = value if value is not None else base_types.UninitialisedField(self, 'NoteDnmtn', ActiveCurrencyAndAmount, False)

	@NoteDnmtn.deleter
	def NoteDnmtn(self):
		del self._NoteDnmtn
		self._NoteDnmtn = base_types.UninitialisedField(self, 'NoteDnmtn', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfNotes', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NoteDnmtn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))