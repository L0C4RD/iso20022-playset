# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import ISO8583MessageReasonCode
from . import ISO8583TransactionTypeCode
from . import LocalData22
from . import Max1000Text
from . import Max256Text
from . import Max35Text
from . import Max6NumericText
from . import TransactionAttribute3Code
from . import TrueFalseIndicator

class TransactionCharacteristics5(base_types._BaseFieldType):

	__slots__ = ["_AltrnMsgRsn", "_Colltn", "_Cxl", "_LclData", "_MsgRsn", "_NtlData", "_PreAuthstnTmLmt", "_PrvtData", "_RtgTblId", "_SbsqntTxTp", "_TxAttr", "_TxDesc", "_TxSubTp", "_TxTp"]
	@property
	def AltrnMsgRsn(self):
		return self._AltrnMsgRsn

	@AltrnMsgRsn.setter
	def AltrnMsgRsn(self, value):
		self._AltrnMsgRsn = value if value is not None else base_types.UninitialisedField(self, 'AltrnMsgRsn', Max256Text, True)

	@AltrnMsgRsn.deleter
	def AltrnMsgRsn(self):
		del self._AltrnMsgRsn
		self._AltrnMsgRsn = base_types.UninitialisedField(self, 'AltrnMsgRsn', Max256Text, True)

	@property
	def Colltn(self):
		return self._Colltn

	@Colltn.setter
	def Colltn(self, value):
		self._Colltn = value if value is not None else base_types.UninitialisedField(self, 'Colltn', TrueFalseIndicator, False)

	@Colltn.deleter
	def Colltn(self):
		del self._Colltn
		self._Colltn = base_types.UninitialisedField(self, 'Colltn', TrueFalseIndicator, False)

	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if value is not None else base_types.UninitialisedField(self, 'Cxl', TrueFalseIndicator, False)

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = base_types.UninitialisedField(self, 'Cxl', TrueFalseIndicator, False)

	@property
	def LclData(self):
		return self._LclData

	@LclData.setter
	def LclData(self, value):
		self._LclData = value if value is not None else base_types.UninitialisedField(self, 'LclData', LocalData22, True)

	@LclData.deleter
	def LclData(self):
		del self._LclData
		self._LclData = base_types.UninitialisedField(self, 'LclData', LocalData22, True)

	@property
	def MsgRsn(self):
		return self._MsgRsn

	@MsgRsn.setter
	def MsgRsn(self, value):
		self._MsgRsn = value if value is not None else base_types.UninitialisedField(self, 'MsgRsn', ISO8583MessageReasonCode, True)

	@MsgRsn.deleter
	def MsgRsn(self):
		del self._MsgRsn
		self._MsgRsn = base_types.UninitialisedField(self, 'MsgRsn', ISO8583MessageReasonCode, True)

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PreAuthstnTmLmt(self):
		return self._PreAuthstnTmLmt

	@PreAuthstnTmLmt.setter
	def PreAuthstnTmLmt(self, value):
		self._PreAuthstnTmLmt = value if value is not None else base_types.UninitialisedField(self, 'PreAuthstnTmLmt', Max6NumericText, False)

	@PreAuthstnTmLmt.deleter
	def PreAuthstnTmLmt(self):
		del self._PreAuthstnTmLmt
		self._PreAuthstnTmLmt = base_types.UninitialisedField(self, 'PreAuthstnTmLmt', Max6NumericText, False)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@property
	def RtgTblId(self):
		return self._RtgTblId

	@RtgTblId.setter
	def RtgTblId(self, value):
		self._RtgTblId = value if value is not None else base_types.UninitialisedField(self, 'RtgTblId', Max35Text, False)

	@RtgTblId.deleter
	def RtgTblId(self):
		del self._RtgTblId
		self._RtgTblId = base_types.UninitialisedField(self, 'RtgTblId', Max35Text, False)

	@property
	def SbsqntTxTp(self):
		return self._SbsqntTxTp

	@SbsqntTxTp.setter
	def SbsqntTxTp(self, value):
		self._SbsqntTxTp = value if value is not None else base_types.UninitialisedField(self, 'SbsqntTxTp', ISO8583TransactionTypeCode, False)

	@SbsqntTxTp.deleter
	def SbsqntTxTp(self):
		del self._SbsqntTxTp
		self._SbsqntTxTp = base_types.UninitialisedField(self, 'SbsqntTxTp', ISO8583TransactionTypeCode, False)

	@property
	def TxAttr(self):
		return self._TxAttr

	@TxAttr.setter
	def TxAttr(self, value):
		self._TxAttr = value if value is not None else base_types.UninitialisedField(self, 'TxAttr', TransactionAttribute3Code, True)

	@TxAttr.deleter
	def TxAttr(self):
		del self._TxAttr
		self._TxAttr = base_types.UninitialisedField(self, 'TxAttr', TransactionAttribute3Code, True)

	@property
	def TxDesc(self):
		return self._TxDesc

	@TxDesc.setter
	def TxDesc(self, value):
		self._TxDesc = value if value is not None else base_types.UninitialisedField(self, 'TxDesc', Max1000Text, False)

	@TxDesc.deleter
	def TxDesc(self):
		del self._TxDesc
		self._TxDesc = base_types.UninitialisedField(self, 'TxDesc', Max1000Text, False)

	@property
	def TxSubTp(self):
		return self._TxSubTp

	@TxSubTp.setter
	def TxSubTp(self, value):
		self._TxSubTp = value if value is not None else base_types.UninitialisedField(self, 'TxSubTp', Max35Text, False)

	@TxSubTp.deleter
	def TxSubTp(self):
		del self._TxSubTp
		self._TxSubTp = base_types.UninitialisedField(self, 'TxSubTp', Max35Text, False)

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
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Colltn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cxl', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LclData', type=LocalData22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PreAuthstnTmLmt', type=Max6NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RtgTblId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbsqntTxTp', type=ISO8583TransactionTypeCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAttr', type=TransactionAttribute3Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxDesc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ISO8583TransactionTypeCode, min=1, max=1, mutex_group=None, array=False),
	))