# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Charges16
from . import Document15
from . import ExternalPaymentTransactionStatus1Code
from . import ISODateTime
from . import Max35Text
from . import OriginalTransactionReference46
from . import PaymentConditionStatus2
from . import StatusReasonInformation14
from . import SupplementaryData1
from . import UUIDv4Identifier

class PaymentTransaction169(base_types._BaseFieldType):

	__slots__ = ["_AccptncDtTm", "_AcctSvcrRef", "_ChrgsInf", "_ClrSysRef", "_DbtrDcsnDtTm", "_NclsdFile", "_OrgnlEndToEndId", "_OrgnlInstrId", "_OrgnlTxRef", "_OrgnlUETR", "_PmtCondSts", "_SplmtryData", "_StsId", "_StsRsnInf", "_TxSts"]
	@property
	def AccptncDtTm(self):
		return self._AccptncDtTm

	@AccptncDtTm.setter
	def AccptncDtTm(self, value):
		self._AccptncDtTm = value if value is not None else base_types.UninitialisedField(self, 'AccptncDtTm', ISODateTime, False)

	@AccptncDtTm.deleter
	def AccptncDtTm(self):
		del self._AccptncDtTm
		self._AccptncDtTm = base_types.UninitialisedField(self, 'AccptncDtTm', ISODateTime, False)

	@property
	def AcctSvcrRef(self):
		return self._AcctSvcrRef

	@AcctSvcrRef.setter
	def AcctSvcrRef(self, value):
		self._AcctSvcrRef = value if value is not None else base_types.UninitialisedField(self, 'AcctSvcrRef', Max35Text, False)

	@AcctSvcrRef.deleter
	def AcctSvcrRef(self):
		del self._AcctSvcrRef
		self._AcctSvcrRef = base_types.UninitialisedField(self, 'AcctSvcrRef', Max35Text, False)

	@property
	def ChrgsInf(self):
		return self._ChrgsInf

	@ChrgsInf.setter
	def ChrgsInf(self, value):
		self._ChrgsInf = value if value is not None else base_types.UninitialisedField(self, 'ChrgsInf', Charges16, True)

	@ChrgsInf.deleter
	def ChrgsInf(self):
		del self._ChrgsInf
		self._ChrgsInf = base_types.UninitialisedField(self, 'ChrgsInf', Charges16, True)

	@property
	def ClrSysRef(self):
		return self._ClrSysRef

	@ClrSysRef.setter
	def ClrSysRef(self, value):
		self._ClrSysRef = value if value is not None else base_types.UninitialisedField(self, 'ClrSysRef', Max35Text, False)

	@ClrSysRef.deleter
	def ClrSysRef(self):
		del self._ClrSysRef
		self._ClrSysRef = base_types.UninitialisedField(self, 'ClrSysRef', Max35Text, False)

	@property
	def DbtrDcsnDtTm(self):
		return self._DbtrDcsnDtTm

	@DbtrDcsnDtTm.setter
	def DbtrDcsnDtTm(self, value):
		self._DbtrDcsnDtTm = value if value is not None else base_types.UninitialisedField(self, 'DbtrDcsnDtTm', ISODateTime, False)

	@DbtrDcsnDtTm.deleter
	def DbtrDcsnDtTm(self):
		del self._DbtrDcsnDtTm
		self._DbtrDcsnDtTm = base_types.UninitialisedField(self, 'DbtrDcsnDtTm', ISODateTime, False)

	@property
	def NclsdFile(self):
		return self._NclsdFile

	@NclsdFile.setter
	def NclsdFile(self, value):
		self._NclsdFile = value if value is not None else base_types.UninitialisedField(self, 'NclsdFile', Document15, True)

	@NclsdFile.deleter
	def NclsdFile(self):
		del self._NclsdFile
		self._NclsdFile = base_types.UninitialisedField(self, 'NclsdFile', Document15, True)

	@property
	def OrgnlEndToEndId(self):
		return self._OrgnlEndToEndId

	@OrgnlEndToEndId.setter
	def OrgnlEndToEndId(self, value):
		self._OrgnlEndToEndId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlEndToEndId', Max35Text, False)

	@OrgnlEndToEndId.deleter
	def OrgnlEndToEndId(self):
		del self._OrgnlEndToEndId
		self._OrgnlEndToEndId = base_types.UninitialisedField(self, 'OrgnlEndToEndId', Max35Text, False)

	@property
	def OrgnlInstrId(self):
		return self._OrgnlInstrId

	@OrgnlInstrId.setter
	def OrgnlInstrId(self, value):
		self._OrgnlInstrId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlInstrId', Max35Text, False)

	@OrgnlInstrId.deleter
	def OrgnlInstrId(self):
		del self._OrgnlInstrId
		self._OrgnlInstrId = base_types.UninitialisedField(self, 'OrgnlInstrId', Max35Text, False)

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTxRef', OriginalTransactionReference46, False)

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = base_types.UninitialisedField(self, 'OrgnlTxRef', OriginalTransactionReference46, False)

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if value is not None else base_types.UninitialisedField(self, 'OrgnlUETR', UUIDv4Identifier, False)

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = base_types.UninitialisedField(self, 'OrgnlUETR', UUIDv4Identifier, False)

	@property
	def PmtCondSts(self):
		return self._PmtCondSts

	@PmtCondSts.setter
	def PmtCondSts(self, value):
		self._PmtCondSts = value if value is not None else base_types.UninitialisedField(self, 'PmtCondSts', PaymentConditionStatus2, False)

	@PmtCondSts.deleter
	def PmtCondSts(self):
		del self._PmtCondSts
		self._PmtCondSts = base_types.UninitialisedField(self, 'PmtCondSts', PaymentConditionStatus2, False)

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
	def StsId(self):
		return self._StsId

	@StsId.setter
	def StsId(self, value):
		self._StsId = value if value is not None else base_types.UninitialisedField(self, 'StsId', Max35Text, False)

	@StsId.deleter
	def StsId(self):
		del self._StsId
		self._StsId = base_types.UninitialisedField(self, 'StsId', Max35Text, False)

	@property
	def StsRsnInf(self):
		return self._StsRsnInf

	@StsRsnInf.setter
	def StsRsnInf(self, value):
		self._StsRsnInf = value if value is not None else base_types.UninitialisedField(self, 'StsRsnInf', StatusReasonInformation14, True)

	@StsRsnInf.deleter
	def StsRsnInf(self):
		del self._StsRsnInf
		self._StsRsnInf = base_types.UninitialisedField(self, 'StsRsnInf', StatusReasonInformation14, True)

	@property
	def TxSts(self):
		return self._TxSts

	@TxSts.setter
	def TxSts(self, value):
		self._TxSts = value if value is not None else base_types.UninitialisedField(self, 'TxSts', ExternalPaymentTransactionStatus1Code, False)

	@TxSts.deleter
	def TxSts(self):
		del self._TxSts
		self._TxSts = base_types.UninitialisedField(self, 'TxSts', ExternalPaymentTransactionStatus1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptncDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctSvcrRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsInf', type=Charges16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrSysRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrDcsnDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NclsdFile', type=Document15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference46, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtCondSts', type=PaymentConditionStatus2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsnInf', type=StatusReasonInformation14, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSts', type=ExternalPaymentTransactionStatus1Code, min=0, max=1, mutex_group=None, array=False),
	))