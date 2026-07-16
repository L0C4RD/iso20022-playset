# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import ISO8583MessageReasonCode
from . import ISO8583TransactionTypeCode
from . import Max1000Text
from . import Max256Text
from . import Max35Text
from . import Max6NumericText
from . import TransactionAttribute2Code

class OriginalTransactionCharacteristics1(base_types._BaseFieldType):

	__slots__ = ["_AddtlData", "_AltrnMsgRsn", "_MsgRsn", "_OthrTxAttr", "_PreAuthstnTmLmt", "_TxAttr", "_TxDesc", "_TxSubTp", "_TxTp"]
	@property
	def AddtlData(self):
		return self._AddtlData

	@AddtlData.setter
	def AddtlData(self, value):
		self._AddtlData = value if value is not None else base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

	@AddtlData.deleter
	def AddtlData(self):
		del self._AddtlData
		self._AddtlData = base_types.UninitialisedField(self, 'AddtlData', AdditionalData1, True)

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
	def OthrTxAttr(self):
		return self._OthrTxAttr

	@OthrTxAttr.setter
	def OthrTxAttr(self, value):
		self._OthrTxAttr = value if value is not None else base_types.UninitialisedField(self, 'OthrTxAttr', Max35Text, False)

	@OthrTxAttr.deleter
	def OthrTxAttr(self):
		del self._OthrTxAttr
		self._OthrTxAttr = base_types.UninitialisedField(self, 'OthrTxAttr', Max35Text, False)

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
	def TxAttr(self):
		return self._TxAttr

	@TxAttr.setter
	def TxAttr(self, value):
		self._TxAttr = value if value is not None else base_types.UninitialisedField(self, 'TxAttr', TransactionAttribute2Code, True)

	@TxAttr.deleter
	def TxAttr(self):
		del self._TxAttr
		self._TxAttr = base_types.UninitialisedField(self, 'TxAttr', TransactionAttribute2Code, True)

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
		base_types.FieldEntry(name='AddtlData', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AltrnMsgRsn', type=Max256Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgRsn', type=ISO8583MessageReasonCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OthrTxAttr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreAuthstnTmLmt', type=Max6NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxAttr', type=TransactionAttribute2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxDesc', type=Max1000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxSubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ISO8583TransactionTypeCode, min=0, max=1, mutex_group=None, array=False),
	))