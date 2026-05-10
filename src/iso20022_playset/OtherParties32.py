from . import base_types
from .PartyIdentificationAndAccount154 import PartyIdentificationAndAccount154
from .PartyIdentificationAndAccount150 import PartyIdentificationAndAccount150
from .PartyIdentificationAndAccount152 import PartyIdentificationAndAccount152
from .PartyIdentificationAndAccount151 import PartyIdentificationAndAccount151

class OtherParties32(base_types._BaseFieldType):

	__slots__ = ["_TrptyAgt", "_Invstr", "_QlfdFrgnIntrmy", "_TradRgltr", "_StockXchg"]
	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if type(value) != auto else self.make_default("TrptyAgt")

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = None

	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if type(value) != auto else self.make_default("Invstr")

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = None

	@property
	def QlfdFrgnIntrmy(self):
		return self._QlfdFrgnIntrmy

	@QlfdFrgnIntrmy.setter
	def QlfdFrgnIntrmy(self, value):
		self._QlfdFrgnIntrmy = value if type(value) != auto else self.make_default("QlfdFrgnIntrmy")

	@QlfdFrgnIntrmy.deleter
	def QlfdFrgnIntrmy(self):
		del self._QlfdFrgnIntrmy
		self._QlfdFrgnIntrmy = None

	@property
	def TradRgltr(self):
		return self._TradRgltr

	@TradRgltr.setter
	def TradRgltr(self, value):
		self._TradRgltr = value if type(value) != auto else self.make_default("TradRgltr")

	@TradRgltr.deleter
	def TradRgltr(self):
		del self._TradRgltr
		self._TradRgltr = None

	@property
	def StockXchg(self):
		return self._StockXchg

	@StockXchg.setter
	def StockXchg(self, value):
		self._StockXchg = value if type(value) != auto else self.make_default("StockXchg")

	@StockXchg.deleter
	def StockXchg(self):
		del self._StockXchg
		self._StockXchg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TrptyAgt', type=PartyIdentificationAndAccount154, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invstr', type=PartyIdentificationAndAccount150, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QlfdFrgnIntrmy', type=PartyIdentificationAndAccount151, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradRgltr', type=PartyIdentificationAndAccount152, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchg', type=PartyIdentificationAndAccount152, min=0, max=1, mutex_group=None, array=False),
	))

