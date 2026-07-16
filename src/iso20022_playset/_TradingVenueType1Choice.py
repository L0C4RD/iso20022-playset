# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import NoReasonCode
from . import TradeMarket2Code

class TradingVenueType1Choice(base_types._BaseFieldType):

	__slots__ = ["_OffVn", "_OnVn"]
	@property
	def OffVn(self):
		return self._OffVn

	@OffVn.setter
	def OffVn(self, value):
		self._OffVn = value if value is not None else base_types.UninitialisedField(self, 'OffVn', NoReasonCode, False)

	@OffVn.deleter
	def OffVn(self):
		del self._OffVn
		self._OffVn = base_types.UninitialisedField(self, 'OffVn', NoReasonCode, False)

	@property
	def OnVn(self):
		return self._OnVn

	@OnVn.setter
	def OnVn(self, value):
		self._OnVn = value if value is not None else base_types.UninitialisedField(self, 'OnVn', TradeMarket2Code, False)

	@OnVn.deleter
	def OnVn(self):
		del self._OnVn
		self._OnVn = base_types.UninitialisedField(self, 'OnVn', TradeMarket2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OffVn', type=NoReasonCode, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OnVn', type=TradeMarket2Code, min=0, max=1, mutex_group=1, array=False),
	))