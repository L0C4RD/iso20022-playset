# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageIdentification1
from . import NumberOfItemsPerStatus1
from . import PartyIdentification100
from . import ReportItemStatus1Choice
from . import StatementReference1
from . import SupplementaryData1

class SecuritiesBalanceTransparencyReportStatusAdviceV01(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_NbOfItmsPerSts", "_RcvrId", "_RltdStmt", "_SndrId", "_SplmtryData", "_Sts"]
	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', MessageIdentification1, False)

	@property
	def NbOfItmsPerSts(self):
		return self._NbOfItmsPerSts

	@NbOfItmsPerSts.setter
	def NbOfItmsPerSts(self, value):
		self._NbOfItmsPerSts = value if value is not None else base_types.UninitialisedField(self, 'NbOfItmsPerSts', NumberOfItemsPerStatus1, True)

	@NbOfItmsPerSts.deleter
	def NbOfItmsPerSts(self):
		del self._NbOfItmsPerSts
		self._NbOfItmsPerSts = base_types.UninitialisedField(self, 'NbOfItmsPerSts', NumberOfItemsPerStatus1, True)

	@property
	def RcvrId(self):
		return self._RcvrId

	@RcvrId.setter
	def RcvrId(self, value):
		self._RcvrId = value if value is not None else base_types.UninitialisedField(self, 'RcvrId', PartyIdentification100, False)

	@RcvrId.deleter
	def RcvrId(self):
		del self._RcvrId
		self._RcvrId = base_types.UninitialisedField(self, 'RcvrId', PartyIdentification100, False)

	@property
	def RltdStmt(self):
		return self._RltdStmt

	@RltdStmt.setter
	def RltdStmt(self, value):
		self._RltdStmt = value if value is not None else base_types.UninitialisedField(self, 'RltdStmt', StatementReference1, False)

	@RltdStmt.deleter
	def RltdStmt(self):
		del self._RltdStmt
		self._RltdStmt = base_types.UninitialisedField(self, 'RltdStmt', StatementReference1, False)

	@property
	def SndrId(self):
		return self._SndrId

	@SndrId.setter
	def SndrId(self, value):
		self._SndrId = value if value is not None else base_types.UninitialisedField(self, 'SndrId', PartyIdentification100, False)

	@SndrId.deleter
	def SndrId(self):
		del self._SndrId
		self._SndrId = base_types.UninitialisedField(self, 'SndrId', PartyIdentification100, False)

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
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', ReportItemStatus1Choice, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', ReportItemStatus1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfItmsPerSts', type=NumberOfItemsPerStatus1, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='RcvrId', type=PartyIdentification100, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdStmt', type=StatementReference1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndrId', type=PartyIdentification100, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=ReportItemStatus1Choice, min=1, max=1, mutex_group=None, array=False),
	))