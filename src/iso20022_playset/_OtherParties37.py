# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification157
from . import PartyIdentification170

class OtherParties37(base_types._BaseFieldType):

	__slots__ = ["_Invstr", "_QlfdFrgnIntrmy", "_StockXchg", "_TradRgltr", "_TrptyAgt"]
	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if value is not None else base_types.UninitialisedField(self, 'Invstr', PartyIdentification170, False)

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = base_types.UninitialisedField(self, 'Invstr', PartyIdentification170, False)

	@property
	def QlfdFrgnIntrmy(self):
		return self._QlfdFrgnIntrmy

	@QlfdFrgnIntrmy.setter
	def QlfdFrgnIntrmy(self, value):
		self._QlfdFrgnIntrmy = value if value is not None else base_types.UninitialisedField(self, 'QlfdFrgnIntrmy', PartyIdentification157, False)

	@QlfdFrgnIntrmy.deleter
	def QlfdFrgnIntrmy(self):
		del self._QlfdFrgnIntrmy
		self._QlfdFrgnIntrmy = base_types.UninitialisedField(self, 'QlfdFrgnIntrmy', PartyIdentification157, False)

	@property
	def StockXchg(self):
		return self._StockXchg

	@StockXchg.setter
	def StockXchg(self, value):
		self._StockXchg = value if value is not None else base_types.UninitialisedField(self, 'StockXchg', PartyIdentification157, False)

	@StockXchg.deleter
	def StockXchg(self):
		del self._StockXchg
		self._StockXchg = base_types.UninitialisedField(self, 'StockXchg', PartyIdentification157, False)

	@property
	def TradRgltr(self):
		return self._TradRgltr

	@TradRgltr.setter
	def TradRgltr(self, value):
		self._TradRgltr = value if value is not None else base_types.UninitialisedField(self, 'TradRgltr', PartyIdentification157, False)

	@TradRgltr.deleter
	def TradRgltr(self):
		del self._TradRgltr
		self._TradRgltr = base_types.UninitialisedField(self, 'TradRgltr', PartyIdentification157, False)

	@property
	def TrptyAgt(self):
		return self._TrptyAgt

	@TrptyAgt.setter
	def TrptyAgt(self, value):
		self._TrptyAgt = value if value is not None else base_types.UninitialisedField(self, 'TrptyAgt', PartyIdentification157, False)

	@TrptyAgt.deleter
	def TrptyAgt(self):
		del self._TrptyAgt
		self._TrptyAgt = base_types.UninitialisedField(self, 'TrptyAgt', PartyIdentification157, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Invstr', type=PartyIdentification170, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QlfdFrgnIntrmy', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchg', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradRgltr', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrptyAgt', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
	))