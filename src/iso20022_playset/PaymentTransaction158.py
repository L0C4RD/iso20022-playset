from . import base_types
import OriginalGroupInformation29
import UUIDv4Identifier
import ISODateTime
import Max35Text
import SupplementaryData1
import BranchAndFinancialInstitutionIdentification8
import OriginalTransactionReference42

class PaymentTransaction158(base_types._BaseFieldType):

	__slots__ = ["_OrgnlEndToEndId", "_ClrSysRef", "_StsReqId", "_SplmtryData", "_OrgnlGrpInf", "_AccptncDtTm", "_InstdAgt", "_OrgnlInstrId", "_InstgAgt", "_OrgnlTxId", "_OrgnlUETR", "_OrgnlTxRef"]
	@property
	def OrgnlEndToEndId(self):
		return self._OrgnlEndToEndId

	@OrgnlEndToEndId.setter
	def OrgnlEndToEndId(self, value):
		self._OrgnlEndToEndId = value if type(value) != auto else self.make_default("OrgnlEndToEndId")

	@OrgnlEndToEndId.deleter
	def OrgnlEndToEndId(self):
		del self._OrgnlEndToEndId
		self._OrgnlEndToEndId = None

	@property
	def ClrSysRef(self):
		return self._ClrSysRef

	@ClrSysRef.setter
	def ClrSysRef(self, value):
		self._ClrSysRef = value if type(value) != auto else self.make_default("ClrSysRef")

	@ClrSysRef.deleter
	def ClrSysRef(self):
		del self._ClrSysRef
		self._ClrSysRef = None

	@property
	def StsReqId(self):
		return self._StsReqId

	@StsReqId.setter
	def StsReqId(self, value):
		self._StsReqId = value if type(value) != auto else self.make_default("StsReqId")

	@StsReqId.deleter
	def StsReqId(self):
		del self._StsReqId
		self._StsReqId = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def OrgnlGrpInf(self):
		return self._OrgnlGrpInf

	@OrgnlGrpInf.setter
	def OrgnlGrpInf(self, value):
		self._OrgnlGrpInf = value if type(value) != auto else self.make_default("OrgnlGrpInf")

	@OrgnlGrpInf.deleter
	def OrgnlGrpInf(self):
		del self._OrgnlGrpInf
		self._OrgnlGrpInf = None

	@property
	def AccptncDtTm(self):
		return self._AccptncDtTm

	@AccptncDtTm.setter
	def AccptncDtTm(self, value):
		self._AccptncDtTm = value if type(value) != auto else self.make_default("AccptncDtTm")

	@AccptncDtTm.deleter
	def AccptncDtTm(self):
		del self._AccptncDtTm
		self._AccptncDtTm = None

	@property
	def InstdAgt(self):
		return self._InstdAgt

	@InstdAgt.setter
	def InstdAgt(self, value):
		self._InstdAgt = value if type(value) != auto else self.make_default("InstdAgt")

	@InstdAgt.deleter
	def InstdAgt(self):
		del self._InstdAgt
		self._InstdAgt = None

	@property
	def OrgnlInstrId(self):
		return self._OrgnlInstrId

	@OrgnlInstrId.setter
	def OrgnlInstrId(self, value):
		self._OrgnlInstrId = value if type(value) != auto else self.make_default("OrgnlInstrId")

	@OrgnlInstrId.deleter
	def OrgnlInstrId(self):
		del self._OrgnlInstrId
		self._OrgnlInstrId = None

	@property
	def InstgAgt(self):
		return self._InstgAgt

	@InstgAgt.setter
	def InstgAgt(self, value):
		self._InstgAgt = value if type(value) != auto else self.make_default("InstgAgt")

	@InstgAgt.deleter
	def InstgAgt(self):
		del self._InstgAgt
		self._InstgAgt = None

	@property
	def OrgnlTxId(self):
		return self._OrgnlTxId

	@OrgnlTxId.setter
	def OrgnlTxId(self, value):
		self._OrgnlTxId = value if type(value) != auto else self.make_default("OrgnlTxId")

	@OrgnlTxId.deleter
	def OrgnlTxId(self):
		del self._OrgnlTxId
		self._OrgnlTxId = None

	@property
	def OrgnlUETR(self):
		return self._OrgnlUETR

	@OrgnlUETR.setter
	def OrgnlUETR(self, value):
		self._OrgnlUETR = value if type(value) != auto else self.make_default("OrgnlUETR")

	@OrgnlUETR.deleter
	def OrgnlUETR(self):
		del self._OrgnlUETR
		self._OrgnlUETR = None

	@property
	def OrgnlTxRef(self):
		return self._OrgnlTxRef

	@OrgnlTxRef.setter
	def OrgnlTxRef(self, value):
		self._OrgnlTxRef = value if type(value) != auto else self.make_default("OrgnlTxRef")

	@OrgnlTxRef.deleter
	def OrgnlTxRef(self):
		del self._OrgnlTxRef
		self._OrgnlTxRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlEndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrSysRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsReqId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrgnlGrpInf', type=OriginalGroupInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlInstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstgAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlUETR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlTxRef', type=OriginalTransactionReference42, min=0, max=1, mutex_group=None, array=False),
	))

