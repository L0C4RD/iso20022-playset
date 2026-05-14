# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyIdentification157 import PartyIdentification157
from ._PartyIdentification170 import PartyIdentification170

class OtherParties42(base_types._BaseFieldType):

	__slots__ = ["_Invstr", "_StockXchg", "_TradRgltr"]
	@property
	def Invstr(self):
		return self._Invstr

	@Invstr.setter
	def Invstr(self, value):
		self._Invstr = value if type(value) != base_types.auto else self.make_default("Invstr")

	@Invstr.deleter
	def Invstr(self):
		del self._Invstr
		self._Invstr = None

	@property
	def StockXchg(self):
		return self._StockXchg

	@StockXchg.setter
	def StockXchg(self, value):
		self._StockXchg = value if type(value) != base_types.auto else self.make_default("StockXchg")

	@StockXchg.deleter
	def StockXchg(self):
		del self._StockXchg
		self._StockXchg = None

	@property
	def TradRgltr(self):
		return self._TradRgltr

	@TradRgltr.setter
	def TradRgltr(self, value):
		self._TradRgltr = value if type(value) != base_types.auto else self.make_default("TradRgltr")

	@TradRgltr.deleter
	def TradRgltr(self):
		del self._TradRgltr
		self._TradRgltr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Invstr', type=PartyIdentification170, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchg', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradRgltr', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
	))