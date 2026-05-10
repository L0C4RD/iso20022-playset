from . import base_types
from .NoReasonCode import NoReasonCode
from .TradeMarket2Code import TradeMarket2Code

class TradingVenueType1Choice(base_types._BaseFieldType):

	__slots__ = ["_OnVn", "_OffVn"]
	@property
	def OnVn(self):
		return self._OnVn

	@OnVn.setter
	def OnVn(self, value):
		self._OnVn = value if type(value) != auto else self.make_default("OnVn")

	@OnVn.deleter
	def OnVn(self):
		del self._OnVn
		self._OnVn = None

	@property
	def OffVn(self):
		return self._OffVn

	@OffVn.setter
	def OffVn(self, value):
		self._OffVn = value if type(value) != auto else self.make_default("OffVn")

	@OffVn.deleter
	def OffVn(self):
		del self._OffVn
		self._OffVn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OnVn', type=TradeMarket2Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OffVn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
	))

