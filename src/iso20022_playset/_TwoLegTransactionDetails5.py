# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection29
from . import AmountAndDirection5
from . import ClosingDate4Choice
from . import Max140Text
from . import Max35Text
from . import OtherAmounts16
from . import Price14
from . import TradeDate7Choice
from . import TradeDate8Choice
from . import TwoLegTransactionType4Choice

class TwoLegTransactionDetails5(base_types._BaseFieldType):

	__slots__ = ["_ClsgDt", "_ClsgLegId", "_ClsgSttlmAmt", "_EndPric", "_GrssTradAmt", "_OpngLegId", "_OthrAmts", "_PrcgDt", "_ScndLegNrrtv", "_TradDt", "_TwoLegTxTp"]
	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if value is not None else base_types.UninitialisedField(self, 'ClsgDt', ClosingDate4Choice, False)

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = base_types.UninitialisedField(self, 'ClsgDt', ClosingDate4Choice, False)

	@property
	def ClsgLegId(self):
		return self._ClsgLegId

	@ClsgLegId.setter
	def ClsgLegId(self, value):
		self._ClsgLegId = value if value is not None else base_types.UninitialisedField(self, 'ClsgLegId', Max35Text, False)

	@ClsgLegId.deleter
	def ClsgLegId(self):
		del self._ClsgLegId
		self._ClsgLegId = base_types.UninitialisedField(self, 'ClsgLegId', Max35Text, False)

	@property
	def ClsgSttlmAmt(self):
		return self._ClsgSttlmAmt

	@ClsgSttlmAmt.setter
	def ClsgSttlmAmt(self, value):
		self._ClsgSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'ClsgSttlmAmt', AmountAndDirection5, False)

	@ClsgSttlmAmt.deleter
	def ClsgSttlmAmt(self):
		del self._ClsgSttlmAmt
		self._ClsgSttlmAmt = base_types.UninitialisedField(self, 'ClsgSttlmAmt', AmountAndDirection5, False)

	@property
	def EndPric(self):
		return self._EndPric

	@EndPric.setter
	def EndPric(self, value):
		self._EndPric = value if value is not None else base_types.UninitialisedField(self, 'EndPric', Price14, False)

	@EndPric.deleter
	def EndPric(self):
		del self._EndPric
		self._EndPric = base_types.UninitialisedField(self, 'EndPric', Price14, False)

	@property
	def GrssTradAmt(self):
		return self._GrssTradAmt

	@GrssTradAmt.setter
	def GrssTradAmt(self, value):
		self._GrssTradAmt = value if value is not None else base_types.UninitialisedField(self, 'GrssTradAmt', AmountAndDirection29, False)

	@GrssTradAmt.deleter
	def GrssTradAmt(self):
		del self._GrssTradAmt
		self._GrssTradAmt = base_types.UninitialisedField(self, 'GrssTradAmt', AmountAndDirection29, False)

	@property
	def OpngLegId(self):
		return self._OpngLegId

	@OpngLegId.setter
	def OpngLegId(self, value):
		self._OpngLegId = value if value is not None else base_types.UninitialisedField(self, 'OpngLegId', Max35Text, False)

	@OpngLegId.deleter
	def OpngLegId(self):
		del self._OpngLegId
		self._OpngLegId = base_types.UninitialisedField(self, 'OpngLegId', Max35Text, False)

	@property
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if value is not None else base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts16, True)

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = base_types.UninitialisedField(self, 'OthrAmts', OtherAmounts16, True)

	@property
	def PrcgDt(self):
		return self._PrcgDt

	@PrcgDt.setter
	def PrcgDt(self, value):
		self._PrcgDt = value if value is not None else base_types.UninitialisedField(self, 'PrcgDt', TradeDate7Choice, False)

	@PrcgDt.deleter
	def PrcgDt(self):
		del self._PrcgDt
		self._PrcgDt = base_types.UninitialisedField(self, 'PrcgDt', TradeDate7Choice, False)

	@property
	def ScndLegNrrtv(self):
		return self._ScndLegNrrtv

	@ScndLegNrrtv.setter
	def ScndLegNrrtv(self, value):
		self._ScndLegNrrtv = value if value is not None else base_types.UninitialisedField(self, 'ScndLegNrrtv', Max140Text, False)

	@ScndLegNrrtv.deleter
	def ScndLegNrrtv(self):
		del self._ScndLegNrrtv
		self._ScndLegNrrtv = base_types.UninitialisedField(self, 'ScndLegNrrtv', Max140Text, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', TradeDate8Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', TradeDate8Choice, False)

	@property
	def TwoLegTxTp(self):
		return self._TwoLegTxTp

	@TwoLegTxTp.setter
	def TwoLegTxTp(self, value):
		self._TwoLegTxTp = value if value is not None else base_types.UninitialisedField(self, 'TwoLegTxTp', TwoLegTransactionType4Choice, False)

	@TwoLegTxTp.deleter
	def TwoLegTxTp(self):
		del self._TwoLegTxTp
		self._TwoLegTxTp = base_types.UninitialisedField(self, 'TwoLegTxTp', TwoLegTransactionType4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClsgDt', type=ClosingDate4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgLegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgSttlmAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssTradAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngLegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgDt', type=TradeDate7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ScndLegNrrtv', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TwoLegTxTp', type=TwoLegTransactionType4Choice, min=0, max=1, mutex_group=None, array=False),
	))