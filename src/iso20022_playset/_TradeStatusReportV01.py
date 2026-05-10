from . import base_types
from .PartyAndSignature2 import PartyAndSignature2
from .TradeStatusReport1 import TradeStatusReport1

class TradeStatusReportV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_TradStsAdvcDtls"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if type(value) != base_types.auto else self.make_default("DgtlSgntr")

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = None

	@property
	def TradStsAdvcDtls(self):
		return self._TradStsAdvcDtls

	@TradStsAdvcDtls.setter
	def TradStsAdvcDtls(self, value):
		self._TradStsAdvcDtls = value if type(value) != base_types.auto else self.make_default("TradStsAdvcDtls")

	@TradStsAdvcDtls.deleter
	def TradStsAdvcDtls(self):
		del self._TradStsAdvcDtls
		self._TradStsAdvcDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradStsAdvcDtls', type=TradeStatusReport1, min=1, max=1, mutex_group=None, array=False),
	))

