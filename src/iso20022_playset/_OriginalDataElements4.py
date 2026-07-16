# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISO8583ResponseCode
from . import ISO8583TransactionTypeCode
from . import Max11NumericText
from . import MessageClass1Code
from . import MessageFunction16Code
from . import OriginalTransactionIdentification1

class OriginalDataElements4(base_types._BaseFieldType):

	__slots__ = ["_AcqrrId", "_MsgClss", "_MsgFctn", "_RspnCd", "_SndrId", "_TxId", "_TxTp"]
	@property
	def AcqrrId(self):
		return self._AcqrrId

	@AcqrrId.setter
	def AcqrrId(self, value):
		self._AcqrrId = value if value is not None else base_types.UninitialisedField(self, 'AcqrrId', Max11NumericText, False)

	@AcqrrId.deleter
	def AcqrrId(self):
		del self._AcqrrId
		self._AcqrrId = base_types.UninitialisedField(self, 'AcqrrId', Max11NumericText, False)

	@property
	def MsgClss(self):
		return self._MsgClss

	@MsgClss.setter
	def MsgClss(self, value):
		self._MsgClss = value if value is not None else base_types.UninitialisedField(self, 'MsgClss', MessageClass1Code, False)

	@MsgClss.deleter
	def MsgClss(self):
		del self._MsgClss
		self._MsgClss = base_types.UninitialisedField(self, 'MsgClss', MessageClass1Code, False)

	@property
	def MsgFctn(self):
		return self._MsgFctn

	@MsgFctn.setter
	def MsgFctn(self, value):
		self._MsgFctn = value if value is not None else base_types.UninitialisedField(self, 'MsgFctn', MessageFunction16Code, False)

	@MsgFctn.deleter
	def MsgFctn(self):
		del self._MsgFctn
		self._MsgFctn = base_types.UninitialisedField(self, 'MsgFctn', MessageFunction16Code, False)

	@property
	def RspnCd(self):
		return self._RspnCd

	@RspnCd.setter
	def RspnCd(self, value):
		self._RspnCd = value if value is not None else base_types.UninitialisedField(self, 'RspnCd', ISO8583ResponseCode, False)

	@RspnCd.deleter
	def RspnCd(self):
		del self._RspnCd
		self._RspnCd = base_types.UninitialisedField(self, 'RspnCd', ISO8583ResponseCode, False)

	@property
	def SndrId(self):
		return self._SndrId

	@SndrId.setter
	def SndrId(self, value):
		self._SndrId = value if value is not None else base_types.UninitialisedField(self, 'SndrId', Max11NumericText, False)

	@SndrId.deleter
	def SndrId(self):
		del self._SndrId
		self._SndrId = base_types.UninitialisedField(self, 'SndrId', Max11NumericText, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', OriginalTransactionIdentification1, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', OriginalTransactionIdentification1, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', ISO8583TransactionTypeCode, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', ISO8583TransactionTypeCode, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgClss', type=MessageClass1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgFctn', type=MessageFunction16Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=OriginalTransactionIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ISO8583TransactionTypeCode, min=0, max=1, mutex_group=None, array=False),
	))