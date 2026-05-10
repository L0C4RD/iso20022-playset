from . import base_types
from .TransactionDetails174 import TransactionDetails174
from .TransactionIdentifications52 import TransactionIdentifications52
from .SupplementaryData1 import SupplementaryData1
from .ProcessingStatus84Choice import ProcessingStatus84Choice
from .Max35Text import Max35Text

class SecuritiesTransactionCancellationRequestStatusAdviceV08(base_types._BaseFieldType):

	__slots__ = ["_CxlReqRef", "_SplmtryData", "_TxDtls", "_PrcgSts", "_TxId"]
	@property
	def CxlReqRef(self):
		return self._CxlReqRef

	@CxlReqRef.setter
	def CxlReqRef(self, value):
		self._CxlReqRef = value if type(value) != base_types.auto else self.make_default("CxlReqRef")

	@CxlReqRef.deleter
	def CxlReqRef(self):
		del self._CxlReqRef
		self._CxlReqRef = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if type(value) != base_types.auto else self.make_default("TxDtls")

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = None

	@property
	def PrcgSts(self):
		return self._PrcgSts

	@PrcgSts.setter
	def PrcgSts(self, value):
		self._PrcgSts = value if type(value) != base_types.auto else self.make_default("PrcgSts")

	@PrcgSts.deleter
	def PrcgSts(self):
		del self._PrcgSts
		self._PrcgSts = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CxlReqRef', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxDtls', type=TransactionDetails174, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgSts', type=ProcessingStatus84Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifications52, min=0, max=1, mutex_group=None, array=False),
	))

