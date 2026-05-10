from . import base_types
from .TradeData16 import TradeData16
from .AmountsAndValueDate8 import AmountsAndValueDate8
from .AgreedRate3 import AgreedRate3

class SplitTradeDetails5(base_types._BaseFieldType):

	__slots__ = ["_TradAmts", "_AgrdRate", "_StsDtls"]
	@property
	def TradAmts(self):
		return self._TradAmts

	@TradAmts.setter
	def TradAmts(self, value):
		self._TradAmts = value if type(value) != auto else self.make_default("TradAmts")

	@TradAmts.deleter
	def TradAmts(self):
		del self._TradAmts
		self._TradAmts = None

	@property
	def AgrdRate(self):
		return self._AgrdRate

	@AgrdRate.setter
	def AgrdRate(self, value):
		self._AgrdRate = value if type(value) != auto else self.make_default("AgrdRate")

	@AgrdRate.deleter
	def AgrdRate(self):
		del self._AgrdRate
		self._AgrdRate = None

	@property
	def StsDtls(self):
		return self._StsDtls

	@StsDtls.setter
	def StsDtls(self, value):
		self._StsDtls = value if type(value) != auto else self.make_default("StsDtls")

	@StsDtls.deleter
	def StsDtls(self):
		del self._StsDtls
		self._StsDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TradAmts', type=AmountsAndValueDate8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgrdRate', type=AgreedRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDtls', type=TradeData16, min=0, max=1, mutex_group=None, array=False),
	))

