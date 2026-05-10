from . import base_types
from .SupplementaryData1 import SupplementaryData1
from .PartyIdentification100 import PartyIdentification100
from .MessageIdentification1 import MessageIdentification1
from .StatementReference1 import StatementReference1
from .ReportItemStatus1Choice import ReportItemStatus1Choice
from .NumberOfItemsPerStatus1 import NumberOfItemsPerStatus1

class SecuritiesBalanceTransparencyReportStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_Sts", "_SndrId", "_RltdStmt", "_RcvrId", "_NbOfItmsPerSts", "_MsgId"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

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
	def RltdStmt(self):
		return self._RltdStmt

	@RltdStmt.setter
	def RltdStmt(self, value):
		self._RltdStmt = value if type(value) != base_types.auto else self.make_default("RltdStmt")

	@RltdStmt.deleter
	def RltdStmt(self):
		del self._RltdStmt
		self._RltdStmt = None

	@property
	def RcvrId(self):
		return self._RcvrId

	@RcvrId.setter
	def RcvrId(self, value):
		self._RcvrId = value if type(value) != base_types.auto else self.make_default("RcvrId")

	@RcvrId.deleter
	def RcvrId(self):
		del self._RcvrId
		self._RcvrId = None

	@property
	def NbOfItmsPerSts(self):
		return self._NbOfItmsPerSts

	@NbOfItmsPerSts.setter
	def NbOfItmsPerSts(self, value):
		self._NbOfItmsPerSts = value if type(value) != base_types.auto else self.make_default("NbOfItmsPerSts")

	@NbOfItmsPerSts.deleter
	def NbOfItmsPerSts(self):
		del self._NbOfItmsPerSts
		self._NbOfItmsPerSts = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=ReportItemStatus1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrId', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdStmt', type=StatementReference1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcvrId', type=PartyIdentification100, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfItmsPerSts', type=NumberOfItemsPerStatus1, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

