# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification6
from . import Charges7
from . import DateAndDateTime2Choice
from . import ExternalPaymentTransactionStatus1Code
from . import ISODateTime
from . import Max35Text
from . import OriginalGroupInformation29
from . import OriginalTransactionReference35
from . import StatusReasonInformation12
from . import SupplementaryData1
from . import UUIDv4Identifier

class PaymentTransaction130(base_types._BaseFieldType):

	__slots__ = ["_AccptncDtTm", "_AcctSvcrRef", "_ChrgsInf", "_ClrSysRef", "_FctvIntrBkSttlmDt", "_InstdAgt", "_InstgAgt", "_OrgnlEndToEndId", "_OrgnlGrpInf", "_OrgnlInstrId", "_OrgnlTxId", "_OrgnlTxRef", "_OrgnlUETR", "_SplmtryData", "_StsId", "_StsRsnInf", "_TxSts"]
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
		self._ChrgsInf = value if value is not None else base_types.UninitialisedField(self, 'ChrgsInf', Charges7, True)

	@ChrgsInf.deleter
	def ChrgsInf(self):
		del self._ChrgsInf
		self._ChrgsInf = base_types.UninitialisedField(self, 'ChrgsInf', Charges7, True)

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
	def FctvIntrBkSttlmDt(self):
		return self._FctvIntrBkSttlmDt

	@FctvIntrBkSttlmDt.setter
	def FctvIntrBkSttlmDt(self, value):
		self._FctvIntrBkSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'FctvIntrBkSttlmDt', DateAndDateTime2Choice, False)

	@FctvIntrBkSttlmDt.deleter
	def FctvIntrBkSttlmDt(self):
		del self._FctvIntrBkSttlmDt
		self._FctvIntrBkSttlmDt = base_types.UninitialisedField(self, 'FctvIntrBkSttlmDt', DateAndDateTime2Choice, False)

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if value is not None else base_types.UninitialisedField(self, 'InstdAgt', BranchAndFinancialInstitutionIdentification6, False)

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = base_types.UninitialisedField(self, 'InstdAgt', BranchAndFinancialInstitutionIdentification6, False)

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if value is not None else base_types.UninitialisedField(self, 'InstgAgt', BranchAndFinancialInstitutionIdentification6, False)

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = base_types.UninitialisedField(self, 'InstgAgt', BranchAndFinancialInstitutionIdentification6, False)

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
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if value is not None else base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation29, False)

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = base_types.UninitialisedField(self, 'OrgnlGrpInf', OriginalGroupInformation29, False)

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
	def OrgnlTxId(self):
		return self._OrgnlTxId

	@OrgnlTxId.setter
	def OrgnlTxId(self, value):
		self._OrgnlTxId = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTxId', Max35Text, False)

	@OrgnlTxId.deleter
	def OrgnlTxId(self):
		del self._OrgnlTxId
		self._OrgnlTxId = base_types.UninitialisedField(self, 'OrgnlTxId', Max35Text, False)

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if value is not None else base_types.UninitialisedField(self, 'OrgnlTxRef', OriginalTransactionReference35, False)

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = base_types.UninitialisedField(self, 'OrgnlTxRef', OriginalTransactionReference35, False)

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
		self._StsRsnInf = value if value is not None else base_types.UninitialisedField(self, 'StsRsnInf', StatusReasonInformation12, True)

	@StsRsnInf.deleter
	def StsRsnInf(self):
		del self._StsRsnInf
		self._StsRsnInf = base_types.UninitialisedField(self, 'StsRsnInf', StatusReasonInformation12, True)

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
		base_types.FieldEntry(name='ChrgsInf', type=Charges7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClrSysRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvIntrBkSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference35, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsRsnInf', type=StatusReasonInformation12, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxSts', type=ExternalPaymentTransactionStatus1Code, min=0, max=1, mutex_group=None, array=False),
	))