# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AgreedRate3 import AgreedRate3
from ._AmountsAndValueDate8 import AmountsAndValueDate8
from ._TradeData16 import TradeData16

class SplitTradeDetails5(base_types._BaseFieldType):

	__slots__ = ["_AgrdRate", "_StsDtls", "_TradAmts"]
	@property
	def AgrdRate(self):
		return self._AgrdRate

	@AgrdRate.setter
	def AgrdRate(self, value):
		self._AgrdRate = value if type(value) != base_types.auto else self.make_default("AgrdRate")

	@AgrdRate.deleter
	def AgrdRate(self):
		del self._AgrdRate
		self._AgrdRate = None

	@property
	def StsDtls(self):
		return self._StsDtls

	@StsDtls.setter
	def StsDtls(self, value):
		self._StsDtls = value if type(value) != base_types.auto else self.make_default("StsDtls")

	@StsDtls.deleter
	def StsDtls(self):
		del self._StsDtls
		self._StsDtls = None

	@property
	def TradAmts(self):
		return self._TradAmts

	@TradAmts.setter
	def TradAmts(self, value):
		self._TradAmts = value if type(value) != base_types.auto else self.make_default("TradAmts")

	@TradAmts.deleter
	def TradAmts(self):
		del self._TradAmts
		self._TradAmts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrdRate', type=AgreedRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDtls', type=TradeData16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradAmts', type=AmountsAndValueDate8, min=1, max=1, mutex_group=None, array=False),
	))