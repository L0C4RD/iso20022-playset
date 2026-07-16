# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification157
from . import PartyIdentification170

class OtherParties42(base_types._BaseFieldType):

	__slots__ = ["_Invstr", "_StockXchg", "_TradRgltr"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Invstr', type=PartyIdentification170, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchg', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradRgltr', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
	))