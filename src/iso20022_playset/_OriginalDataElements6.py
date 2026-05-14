# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalFee4 import AdditionalFee4
from ._DateTime2 import DateTime2
from ._Exact6AlphaNumericText import Exact6AlphaNumericText
from ._ISO8583ResponseCode import ISO8583ResponseCode
from ._ISO8583TransactionTypeCode import ISO8583TransactionTypeCode
from ._ISODate import ISODate
from ._Max11NumericText import Max11NumericText
from ._MessageClass2Code import MessageClass2Code
from ._MessageFunction16Code import MessageFunction16Code
from ._OriginalTransactionAmounts4 import OriginalTransactionAmounts4
from ._OriginalTransactionIdentification2 import OriginalTransactionIdentification2

class OriginalDataElements6(base_types._BaseFieldType):

	__slots__ = ["_AcqrrId", "_AddtlFee", "_ApprvlCd", "_ConvsDtTm", "_DfrrdSttlmDt", "_MsgClss", "_MsgFctn", "_RspnCd", "_SndrId", "_TxAmts", "_TxId", "_TxTp"]
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
	def AddtlFee(self):
		return self._AddtlFee

	@AddtlFee.setter
	def AddtlFee(self, value):
		self._AddtlFee = value if type(value) != base_types.auto else self.make_default("AddtlFee")

	@AddtlFee.deleter
	def AddtlFee(self):
		del self._AddtlFee
		self._AddtlFee = None

	@property
	def ApprvlCd(self):
		return self._ApprvlCd

	@ApprvlCd.setter
	def ApprvlCd(self, value):
		self._ApprvlCd = value if type(value) != base_types.auto else self.make_default("ApprvlCd")

	@ApprvlCd.deleter
	def ApprvlCd(self):
		del self._ApprvlCd
		self._ApprvlCd = None

	@property
	def ConvsDtTm(self):
		return self._ConvsDtTm

	@ConvsDtTm.setter
	def ConvsDtTm(self, value):
		self._ConvsDtTm = value if type(value) != base_types.auto else self.make_default("ConvsDtTm")

	@ConvsDtTm.deleter
	def ConvsDtTm(self):
		del self._ConvsDtTm
		self._ConvsDtTm = None

	@property
	def DfrrdSttlmDt(self):
		return self._DfrrdSttlmDt

	@DfrrdSttlmDt.setter
	def DfrrdSttlmDt(self, value):
		self._DfrrdSttlmDt = value if type(value) != base_types.auto else self.make_default("DfrrdSttlmDt")

	@DfrrdSttlmDt.deleter
	def DfrrdSttlmDt(self):
		del self._DfrrdSttlmDt
		self._DfrrdSttlmDt = None

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
	def SndrId(self):
		return self._SndrId

	@SndrId.setter
	def SndrId(self, value):
		self._SndrId = value if type(value) != base_types.auto else self.make_default("SndrId")

	@SndrId.deleter
	def SndrId(self):
		del self._SndrId
		self._SndrId = None

	@property
	def TxAmts(self):
		return self._TxAmts

	@TxAmts.setter
	def TxAmts(self, value):
		self._TxAmts = value if type(value) != base_types.auto else self.make_default("TxAmts")

	@TxAmts.deleter
	def TxAmts(self):
		del self._TxAmts
		self._TxAmts = None

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