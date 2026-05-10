from . import base_types
from .Price14 import Price14
from .ClosingDate4Choice import ClosingDate4Choice
from .Max35Text import Max35Text
from .OtherAmounts16 import OtherAmounts16
from .AmountAndDirection29 import AmountAndDirection29
from .TwoLegTransactionType4Choice import TwoLegTransactionType4Choice
from .Max140Text import Max140Text
from .TradeDate8Choice import TradeDate8Choice
from .TradeDate7Choice import TradeDate7Choice
from .AmountAndDirection5 import AmountAndDirection5

class TwoLegTransactionDetails5(base_types._BaseFieldType):

	__slots__ = ["_ScndLegNrrtv", "_EndPric", "_ClsgDt", "_ClsgSttlmAmt", "_PrcgDt", "_ClsgLegId", "_OpngLegId", "_TradDt", "_OthrAmts", "_TwoLegTxTp", "_GrssTradAmt"]
	@property
	def ScndLegNrrtv(self):
		return self._ScndLegNrrtv

	@ScndLegNrrtv.setter
	def ScndLegNrrtv(self, value):
		self._ScndLegNrrtv = value if type(value) != auto else self.make_default("ScndLegNrrtv")

	@ScndLegNrrtv.deleter
	def ScndLegNrrtv(self):
		del self._ScndLegNrrtv
		self._ScndLegNrrtv = None

	@property
	def EndPric(self):
		return self._EndPric

	@EndPric.setter
	def EndPric(self, value):
		self._EndPric = value if type(value) != auto else self.make_default("EndPric")

	@EndPric.deleter
	def EndPric(self):
		del self._EndPric
		self._EndPric = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def ClsgSttlmAmt(self):
		return self._ClsgSttlmAmt

	@ClsgSttlmAmt.setter
	def ClsgSttlmAmt(self, value):
		self._ClsgSttlmAmt = value if type(value) != auto else self.make_default("ClsgSttlmAmt")

	@ClsgSttlmAmt.deleter
	def ClsgSttlmAmt(self):
		del self._ClsgSttlmAmt
		self._ClsgSttlmAmt = None

	@property
	def PrcgDt(self):
		return self._PrcgDt

	@PrcgDt.setter
	def PrcgDt(self, value):
		self._PrcgDt = value if type(value) != auto else self.make_default("PrcgDt")

	@PrcgDt.deleter
	def PrcgDt(self):
		del self._PrcgDt
		self._PrcgDt = None

	@property
	def ClsgLegId(self):
		return self._ClsgLegId

	@ClsgLegId.setter
	def ClsgLegId(self, value):
		self._ClsgLegId = value if type(value) != auto else self.make_default("ClsgLegId")

	@ClsgLegId.deleter
	def ClsgLegId(self):
		del self._ClsgLegId
		self._ClsgLegId = None

	@property
	def OpngLegId(self):
		return self._OpngLegId

	@OpngLegId.setter
	def OpngLegId(self, value):
		self._OpngLegId = value if type(value) != auto else self.make_default("OpngLegId")

	@OpngLegId.deleter
	def OpngLegId(self):
		del self._OpngLegId
		self._OpngLegId = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def OthrAmts(self):
		return self._OthrAmts

	@OthrAmts.setter
	def OthrAmts(self, value):
		self._OthrAmts = value if type(value) != auto else self.make_default("OthrAmts")

	@OthrAmts.deleter
	def OthrAmts(self):
		del self._OthrAmts
		self._OthrAmts = None

	@property
	def TwoLegTxTp(self):
		return self._TwoLegTxTp

	@TwoLegTxTp.setter
	def TwoLegTxTp(self, value):
		self._TwoLegTxTp = value if type(value) != auto else self.make_default("TwoLegTxTp")

	@TwoLegTxTp.deleter
	def TwoLegTxTp(self):
		del self._TwoLegTxTp
		self._TwoLegTxTp = None

	@property
	def GrssTradAmt(self):
		return self._GrssTradAmt

	@GrssTradAmt.setter
	def GrssTradAmt(self, value):
		self._GrssTradAmt = value if type(value) != auto else self.make_default("GrssTradAmt")

	@GrssTradAmt.deleter
	def GrssTradAmt(self):
		del self._GrssTradAmt
		self._GrssTradAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ScndLegNrrtv', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndPric', type=Price14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=ClosingDate4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgSttlmAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgDt', type=TradeDate7Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgLegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngLegId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=TradeDate8Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrAmts', type=OtherAmounts16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TwoLegTxTp', type=TwoLegTransactionType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrssTradAmt', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
	))

