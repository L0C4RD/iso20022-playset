# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BuyIn3
from . import Max35Text
from . import SettlementObligation7
from . import SupplementaryData1

class BuyInResponseV03(base_types._BaseFieldType):

	__slots__ = ["_BuyInRspnDtls", "_OrgnlSttlmOblgtnDtls", "_SplmtryData", "_TxId"]
	@property
	def BuyInRspnDtls(self):
		return self._BuyInRspnDtls

	@BuyInRspnDtls.setter
	def BuyInRspnDtls(self, value):
		self._BuyInRspnDtls = value if value is not None else base_types.UninitialisedField(self, 'BuyInRspnDtls', BuyIn3, False)

	@BuyInRspnDtls.deleter
	def BuyInRspnDtls(self):
		del self._BuyInRspnDtls
		self._BuyInRspnDtls = base_types.UninitialisedField(self, 'BuyInRspnDtls', BuyIn3, False)

	@property
	def OrgnlSttlmOblgtnDtls(self):
		return self._OrgnlSttlmOblgtnDtls

	@OrgnlSttlmOblgtnDtls.setter
	def OrgnlSttlmOblgtnDtls(self, value):
		self._OrgnlSttlmOblgtnDtls = value if value is not None else base_types.UninitialisedField(self, 'OrgnlSttlmOblgtnDtls', SettlementObligation7, False)

	@OrgnlSttlmOblgtnDtls.deleter
	def OrgnlSttlmOblgtnDtls(self):
		del self._OrgnlSttlmOblgtnDtls
		self._OrgnlSttlmOblgtnDtls = base_types.UninitialisedField(self, 'OrgnlSttlmOblgtnDtls', SettlementObligation7, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyInRspnDtls', type=BuyIn3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlSttlmOblgtnDtls', type=SettlementObligation7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))