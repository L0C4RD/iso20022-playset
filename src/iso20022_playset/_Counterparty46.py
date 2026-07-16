# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CounterpartyTradeNature15Choice
from . import PartyIdentification248Choice
from . import TrueFalseIndicator

class Counterparty46(base_types._BaseFieldType):

	__slots__ = ["_IdTp", "_Ntr", "_RptgOblgtn"]
	@property
	def IdTp(self):
		return self._IdTp

	@IdTp.setter
	def IdTp(self, value):
		self._IdTp = value if value is not None else base_types.UninitialisedField(self, 'IdTp', PartyIdentification248Choice, False)

	@IdTp.deleter
	def IdTp(self):
		del self._IdTp
		self._IdTp = base_types.UninitialisedField(self, 'IdTp', PartyIdentification248Choice, False)

	@property
	def Ntr(self):
		return self._Ntr

	@Ntr.setter
	def Ntr(self, value):
		self._Ntr = value if value is not None else base_types.UninitialisedField(self, 'Ntr', CounterpartyTradeNature15Choice, False)

	@Ntr.deleter
	def Ntr(self):
		del self._Ntr
		self._Ntr = base_types.UninitialisedField(self, 'Ntr', CounterpartyTradeNature15Choice, False)

	@property
	def RptgOblgtn(self):
		return self._RptgOblgtn

	@RptgOblgtn.setter
	def RptgOblgtn(self, value):
		self._RptgOblgtn = value if value is not None else base_types.UninitialisedField(self, 'RptgOblgtn', TrueFalseIndicator, False)

	@RptgOblgtn.deleter
	def RptgOblgtn(self):
		del self._RptgOblgtn
		self._RptgOblgtn = base_types.UninitialisedField(self, 'RptgOblgtn', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdTp', type=PartyIdentification248Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntr', type=CounterpartyTradeNature15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgOblgtn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))