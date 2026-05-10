import base_types
import PartyIdentification170
import PartyIdentification157

class OtherParties42(base_types._BaseFieldType):

	__slots__ = ["_TradRgltr", "_Invstr", "_StockXchg"]
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
		base_types.FieldEntry(name='TradRgltr', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Invstr', type=PartyIdentification170, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StockXchg', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
	))

