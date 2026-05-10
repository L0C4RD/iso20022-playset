from . import base_types
from ._AdditionalData1 import AdditionalData1
from ._ISO8583MessageReasonCode import ISO8583MessageReasonCode
from ._ISO8583TransactionTypeCode import ISO8583TransactionTypeCode
from ._Max1000Text import Max1000Text
from ._Max256Text import Max256Text
from ._Max35Text import Max35Text
from ._Max6NumericText import Max6NumericText
from ._TransactionAttribute2Code import TransactionAttribute2Code
from ._TrueFalseIndicator import TrueFalseIndicator

class TransactionCharacteristics1(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AltrnMsgRsn", "_Cxl", "_MsgRsn", "_OthrTxAttr", "_PreAuthstnTmLmt", "_TxAttr", "_TxDesc", "_TxSubTp", "_TxTp"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if type(value) != base_types.auto else self.make_default("AddtlData")

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = None

	@property
	def AltrnMsgRsn(self):
		return self._AltrnMsgRsn

	@AltrnMsgRsn.setter
	def AltrnMsgRsn(self, value):
		self._AltrnMsgRsn = value if type(value) != base_types.auto else self.make_default("AltrnMsgRsn")

	@AltrnMsgRsn.deleter
	def AltrnMsgRsn(self):
		del self._AltrnMsgRsn
		self._AltrnMsgRsn = None

	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if type(value) != base_types.auto else self.make_default("Cxl")

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = None

	@property
	def MsgRsn(self):
		return self._MsgRsn

	@MsgRsn.setter
	def MsgRsn(self, value):
		self._MsgRsn = value if type(value) != base_types.auto else self.make_default("MsgRsn")

	@MsgRsn.deleter
	def MsgRsn(self):
		del self._MsgRsn
		self._MsgRsn = None

	@property
	def OthrTxAttr(self):
		return self._OthrTxAttr

	@OthrTxAttr.setter
	def OthrTxAttr(self, value):
		self._OthrTxAttr = value if type(value) != base_types.auto else self.make_default("OthrTxAttr")

	@OthrTxAttr.deleter
	def OthrTxAttr(self):
		del self._OthrTxAttr
		self._OthrTxAttr = None

	@property
	def PreAuthstnTmLmt(self):
		return self._PreAuthstnTmLmt

	@PreAuthstnTmLmt.setter
	def PreAuthstnTmLmt(self, value):
		self._PreAuthstnTmLmt = value if type(value) != base_types.auto else self.make_default("PreAuthstnTmLmt")

	@PreAuthstnTmLmt.deleter
	def PreAuthstnTmLmt(self):
		del self._PreAuthstnTmLmt
		self._PreAuthstnTmLmt = None

	@property
	def TxAttr(self):
		return self._TxAttr

	@TxAttr.setter
	def TxAttr(self, value):
		self._TxAttr = value if type(value) != base_types.auto else self.make_default("TxAttr")

	@TxAttr.deleter
	def TxAttr(self):
		del self._TxAttr
		self._TxAttr = None

	@property
	def TxDesc(self):
		return self._TxDesc

	@TxDesc.setter
	def TxDesc(self, value):
		self._TxDesc = value if type(value) != base_types.auto else self.make_default("TxDesc")

	@TxDesc.deleter
	def TxDesc(self):
		del self._TxDesc
		self._TxDesc = None

	@property
	def TxSubTp(self):
		return self._TxSubTp

	@TxSubTp.setter
	def TxSubTp(self, value):
		self._TxSubTp = value if type(value) != base_types.auto else self.make_default("TxSubTp")

	@TxSubTp.deleter
	def TxSubTp(self):
		del self._TxSubTp
		self._TxSubTp = None

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if type(value) != base_types.auto else self.make_default("TxTp")

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cxl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrTxAttr', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PreAuthstnTmLmt', type=Max6NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAttr', type=TransactionAttribute2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxDesc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ISO8583TransactionTypeCode, min=1, max=1, mutex_group=None, array=False),
	))

