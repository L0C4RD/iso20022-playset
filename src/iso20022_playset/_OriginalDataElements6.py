# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalFee4
from . import DateTime2
from . import Exact6AlphaNumericText
from . import ISO8583ResponseCode
from . import ISO8583TransactionTypeCode
from . import ISODate
from . import Max11NumericText
from . import MessageClass2Code
from . import MessageFunction16Code
from . import OriginalTransactionAmounts4
from . import OriginalTransactionIdentification2

class OriginalDataElements6(base_types._BaseFieldType):

	__slots__ = ["_AcqrrId", "_AddtlFee", "_ApprvlCd", "_ConvsDtTm", "_DfrrdSttlmDt", "_MsgClss", "_MsgFctn", "_RspnCd", "_SndrId", "_TxAmts", "_TxId", "_TxTp"]
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
	def AddtlFee(self):
		return self._AddtlFee

	@AddtlFee.setter
	def AddtlFee(self, value):
		self._AddtlFee = value if value is not None else base_types.UninitialisedField(self, 'AddtlFee', AdditionalFee4, True)

	@AddtlFee.deleter
	def AddtlFee(self):
		del self._AddtlFee
		self._AddtlFee = base_types.UninitialisedField(self, 'AddtlFee', AdditionalFee4, True)

	@property
	def ApprvlCd(self):
		return self._ApprvlCd

	@ApprvlCd.setter
	def ApprvlCd(self, value):
		self._ApprvlCd = value if value is not None else base_types.UninitialisedField(self, 'ApprvlCd', Exact6AlphaNumericText, False)

	@ApprvlCd.deleter
	def ApprvlCd(self):
		del self._ApprvlCd
		self._ApprvlCd = base_types.UninitialisedField(self, 'ApprvlCd', Exact6AlphaNumericText, False)

	@property
	def ConvsDtTm(self):
		return self._ConvsDtTm

	@ConvsDtTm.setter
	def ConvsDtTm(self, value):
		self._ConvsDtTm = value if value is not None else base_types.UninitialisedField(self, 'ConvsDtTm', DateTime2, False)

	@ConvsDtTm.deleter
	def ConvsDtTm(self):
		del self._ConvsDtTm
		self._ConvsDtTm = base_types.UninitialisedField(self, 'ConvsDtTm', DateTime2, False)

	@property
	def DfrrdSttlmDt(self):
		return self._DfrrdSttlmDt

	@DfrrdSttlmDt.setter
	def DfrrdSttlmDt(self, value):
		self._DfrrdSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'DfrrdSttlmDt', ISODate, False)

	@DfrrdSttlmDt.deleter
	def DfrrdSttlmDt(self):
		del self._DfrrdSttlmDt
		self._DfrrdSttlmDt = base_types.UninitialisedField(self, 'DfrrdSttlmDt', ISODate, False)

	@property
	def MsgClss(self):
		return self._MsgClss

	@MsgClss.setter
	def MsgClss(self, value):
		self._MsgClss = value if value is not None else base_types.UninitialisedField(self, 'MsgClss', MessageClass2Code, False)

	@MsgClss.deleter
	def MsgClss(self):
		del self._MsgClss
		self._MsgClss = base_types.UninitialisedField(self, 'MsgClss', MessageClass2Code, False)

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
	def TxAmts(self):
		return self._TxAmts

	@TxAmts.setter
	def TxAmts(self, value):
		self._TxAmts = value if value is not None else base_types.UninitialisedField(self, 'TxAmts', OriginalTransactionAmounts4, False)

	@TxAmts.deleter
	def TxAmts(self):
		del self._TxAmts
		self._TxAmts = base_types.UninitialisedField(self, 'TxAmts', OriginalTransactionAmounts4, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', OriginalTransactionIdentification2, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', OriginalTransactionIdentification2, False)

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
		base_types.FieldEntry(name='AddtlFee', type=AdditionalFee4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApprvlCd', type=Exact6AlphaNumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ConvsDtTm', type=DateTime2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfrrdSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgClss', type=MessageClass2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgFctn', type=MessageFunction16Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspnCd', type=ISO8583ResponseCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrId', type=Max11NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAmts', type=OriginalTransactionAmounts4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=OriginalTransactionIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ISO8583TransactionTypeCode, min=0, max=1, mutex_group=None, array=False),
	))