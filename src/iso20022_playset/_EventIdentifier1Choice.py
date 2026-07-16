# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PostTradeRiskReductionIdentifier1
from . import UTIIdentifier

class EventIdentifier1Choice(base_types._BaseFieldType):

	__slots__ = ["_EvtIdr", "_PstTradRskRdctnIdr"]
	@property
	def EvtIdr(self):
		return self._EvtIdr

	@EvtIdr.setter
	def EvtIdr(self, value):
		self._EvtIdr = value if value is not None else base_types.UninitialisedField(self, 'EvtIdr', UTIIdentifier, False)

	@EvtIdr.deleter
	def EvtIdr(self):
		del self._EvtIdr
		self._EvtIdr = base_types.UninitialisedField(self, 'EvtIdr', UTIIdentifier, False)

	@property
	def PstTradRskRdctnIdr(self):
		return self._PstTradRskRdctnIdr

	@PstTradRskRdctnIdr.setter
	def PstTradRskRdctnIdr(self, value):
		self._PstTradRskRdctnIdr = value if value is not None else base_types.UninitialisedField(self, 'PstTradRskRdctnIdr', PostTradeRiskReductionIdentifier1, False)

	@PstTradRskRdctnIdr.deleter
	def PstTradRskRdctnIdr(self):
		del self._PstTradRskRdctnIdr
		self._PstTradRskRdctnIdr = base_types.UninitialisedField(self, 'PstTradRskRdctnIdr', PostTradeRiskReductionIdentifier1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtIdr', type=UTIIdentifier, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PstTradRskRdctnIdr', type=PostTradeRiskReductionIdentifier1, min=0, max=1, mutex_group=1, array=False),
	))