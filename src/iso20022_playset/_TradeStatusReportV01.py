# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyAndSignature2
from . import TradeStatusReport1

class TradeStatusReportV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_TradStsAdvcDtls"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@property
	def TradStsAdvcDtls(self):
		return self._TradStsAdvcDtls

	@TradStsAdvcDtls.setter
	def TradStsAdvcDtls(self, value):
		self._TradStsAdvcDtls = value if value is not None else base_types.UninitialisedField(self, 'TradStsAdvcDtls', TradeStatusReport1, False)

	@TradStsAdvcDtls.deleter
	def TradStsAdvcDtls(self):
		del self._TradStsAdvcDtls
		self._TradStsAdvcDtls = base_types.UninitialisedField(self, 'TradStsAdvcDtls', TradeStatusReport1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradStsAdvcDtls', type=TradeStatusReport1, min=1, max=1, mutex_group=None, array=False),
	))