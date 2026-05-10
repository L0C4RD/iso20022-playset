import base_types
import SupplementaryData1
import SettlementObligation7
import BuyIn3
import Max35Text

class BuyInResponseV03(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_BuyInRspnDtls", "_TxId", "_OrgnlSttlmOblgtnDtls"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def BuyInRspnDtls(self):
		return self._BuyInRspnDtls

	@BuyInRspnDtls.setter
	def BuyInRspnDtls(self, value):
		self._BuyInRspnDtls = value if type(value) != auto else self.make_default("BuyInRspnDtls")

	@BuyInRspnDtls.deleter
	def BuyInRspnDtls(self):
		del self._BuyInRspnDtls
		self._BuyInRspnDtls = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def OrgnlSttlmOblgtnDtls(self):
		return self._OrgnlSttlmOblgtnDtls

	@OrgnlSttlmOblgtnDtls.setter
	def OrgnlSttlmOblgtnDtls(self, value):
		self._OrgnlSttlmOblgtnDtls = value if type(value) != auto else self.make_default("OrgnlSttlmOblgtnDtls")

	@OrgnlSttlmOblgtnDtls.deleter
	def OrgnlSttlmOblgtnDtls(self):
		del self._OrgnlSttlmOblgtnDtls
		self._OrgnlSttlmOblgtnDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyInRspnDtls', type=BuyIn3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlSttlmOblgtnDtls', type=SettlementObligation7, min=0, max=1, mutex_group=None, array=False),
	))

