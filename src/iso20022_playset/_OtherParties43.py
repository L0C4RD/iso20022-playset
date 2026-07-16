# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentificationAndAccount165
from . import PartyIdentificationAndAccount197
from . import PartyIdentificationAndAccount198

class OtherParties43(base_types._BaseFieldType):

	__slots__ = ["_Brkr", "_Invstr", "_QlfdFrgnIntrmy", "_StockXchg", "_TradRgltr", "_TrptyAgt"]
	@property
	def Brkr(self):
		return self._Brkr

	@Brkr.setter
	def Brkr(self, value):
		self._Brkr = value if value is not None else base_types.UninitialisedField(self, 'Brkr', PartyIdentificationAndAccount198, False)

	@Brkr.deleter
	def Brkr(self):
		del self._Brkr
		self._Brkr = base_types.UninitialisedField(self, 'Brkr', PartyIdentificationAndAccount198, False)

	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if value is not None else base_types.UninitialisedField(self, 'Invstr', PartyIdentificationAndAccount197, True)

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = base_types.UninitialisedField(self, 'Invstr', PartyIdentificationAndAccount197, True)

	@property
	def QlfdFrgnIntrmy(self):
		return self._QlfdFrgnIntrmy

	@QlfdFrgnIntrmy.setter
	def QlfdFrgnIntrmy(self, value):
		self._QlfdFrgnIntrmy = value if value is not None else base_types.UninitialisedField(self, 'QlfdFrgnIntrmy', PartyIdentificationAndAccount198, False)

	@QlfdFrgnIntrmy.deleter
	def QlfdFrgnIntrmy(self):
		del self._QlfdFrgnIntrmy
		self._QlfdFrgnIntrmy = base_types.UninitialisedField(self, 'QlfdFrgnIntrmy', PartyIdentificationAndAccount198, False)

	@property
	def StockXchg(self):
		return self._StockXchg

	@StockXchg.setter
	def StockXchg(self, value):
		self._StockXchg = value if value is not None else base_types.UninitialisedField(self, 'StockXchg', PartyIdentificationAndAccount165, False)

	@StockXchg.deleter
	def StockXchg(self):
		del self._StockXchg
		self._StockXchg = base_types.UninitialisedField(self, 'StockXchg', PartyIdentificationAndAccount165, False)

	@property
	def TradRgltr(self):
		return self._TradRgltr

	@TradRgltr.setter
	def TradRgltr(self, value):
		self._TradRgltr = value if value is not None else base_types.UninitialisedField(self, 'TradRgltr', PartyIdentificationAndAccount165, False)

	@TradRgltr.deleter
	def TradRgltr(self):
		del self._TradRgltr
		self._TradRgltr = base_types.UninitialisedField(self, 'TradRgltr', PartyIdentificationAndAccount165, False)

	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgt', PartyIdentificationAndAccount198, False)

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = base_types.UninitialisedField(self, 'TrptyAgt', PartyIdentificationAndAccount198, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Brkr', type=PartyIdentificationAndAccount198, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invstr', type=PartyIdentificationAndAccount197, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='QlfdFrgnIntrmy', type=PartyIdentificationAndAccount198, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchg', type=PartyIdentificationAndAccount165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradRgltr', type=PartyIdentificationAndAccount165, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgt', type=PartyIdentificationAndAccount198, min=0, max=1, mutex_group=None, array=False),
	))