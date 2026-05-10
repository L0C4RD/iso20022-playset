from . import base_types
from ._CounterpartyTradeNature15Choice import CounterpartyTradeNature15Choice
from ._PartyIdentification248Choice import PartyIdentification248Choice
from ._TrueFalseIndicator import TrueFalseIndicator

class Counterparty46(base_types._BaseFieldType):

	__slots__ = ["_IdTp", "_Ntr", "_RptgOblgtn"]
	@property
	def IdTp(self):
		return self._IdTp

	@IdTp.setter
	def IdTp(self, value):
		self._IdTp = value if type(value) != base_types.auto else self.make_default("IdTp")

	@IdTp.deleter
	def IdTp(self):
		del self._IdTp
		self._IdTp = None

	@property
	def Ntr(self):
		return self._Ntr

	@Ntr.setter
	def Ntr(self, value):
		self._Ntr = value if type(value) != base_types.auto else self.make_default("Ntr")

	@Ntr.deleter
	def Ntr(self):
		del self._Ntr
		self._Ntr = None

	@property
	def RptgOblgtn(self):
		return self._RptgOblgtn

	@RptgOblgtn.setter
	def RptgOblgtn(self, value):
		self._RptgOblgtn = value if type(value) != base_types.auto else self.make_default("RptgOblgtn")

	@RptgOblgtn.deleter
	def RptgOblgtn(self):
		del self._RptgOblgtn
		self._RptgOblgtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdTp', type=PartyIdentification248Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntr', type=CounterpartyTradeNature15Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgOblgtn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

