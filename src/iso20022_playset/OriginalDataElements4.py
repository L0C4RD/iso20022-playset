from . import base_types
from .OriginalTransactionIdentification1 import OriginalTransactionIdentification1
from .ISO8583TransactionTypeCode import ISO8583TransactionTypeCode
from .MessageFunction16Code import MessageFunction16Code
from .ISO8583ResponseCode import ISO8583ResponseCode
from .Max11NumericText import Max11NumericText
from .MessageClass1Code import MessageClass1Code

class OriginalDataElements4(base_types._BaseFieldType):

	__slots__ = ["_RspnCd", "_AcqrrId", "_MsgFctn", "_MsgClss", "_TxTp", "_TxId", "_SndrId"]
	@property
	def RspnCd(self):
		return self._RspnCd

	@RspnCd.setter
	def RspnCd(self, value):
		self._RspnCd = value if type(value) != base_types.auto else self.make_default("RspnCd")

	@RspnCd.deleter
	def RspnCd(self):
		del self._RspnCd
		self._RspnCd = None

	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if type(value) != base_types.auto else self.make_default("AcqrrId")

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = None

	@property
	def MsgFctn(self):
		return self._MsgFctn

	@MsgFctn.setter
	def MsgFctn(self, value):
		self._MsgFctn = value if type(value) != base_types.auto else self.make_default("MsgFctn")

	@MsgFctn.deleter
	def MsgFctn(self):
		del self._MsgFctn
		self._MsgFctn = None

	@property
	def MsgClss(self):
		return self._MsgClss

	@MsgClss.setter
	def MsgClss(self, value):
		self._MsgClss = value if type(value) != base_types.auto else self.make_default("MsgClss")

	@MsgClss.deleter
	def MsgClss(self):
		del self._MsgClss
		self._MsgClss = None

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

	@property
	def SndrId(self):
		return self._SndrId

	@SndrId.setter
	def SndrId(self, value):
		self._SndrId = value if type(value) != base_types.auto else self.make_default("SndrId")

	@SndrId.deleter
	def SndrId(self):
		del self._SndrId
		self._SndrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcqrrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgFctn', type=MessageFunction16Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgClss', type=MessageClass1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ISO8583TransactionTypeCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=OriginalTransactionIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
	))

