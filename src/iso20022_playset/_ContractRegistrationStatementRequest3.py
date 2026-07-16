# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import ContractRegistrationStatementCriteria1
from . import Max35Text
from . import ReportingPeriod4
from . import SupplementaryData1
from . import TradeParty6

class ContractRegistrationStatementRequest3(base_types._BaseFieldType):

	__slots__ = ["_RegdCtrctId", "_RegnAgt", "_RptgPrd", "_RptgPty", "_RtrCrit", "_SplmtryData", "_StmtReqId"]
	@property
	def RegdCtrctId(self):
		return self._RegdCtrctId

	@RegdCtrctId.setter
	def RegdCtrctId(self, value):
		self._RegdCtrctId = value if value is not None else base_types.UninitialisedField(self, 'RegdCtrctId', Max35Text, False)

	@RegdCtrctId.deleter
	def RegdCtrctId(self):
		del self._RegdCtrctId
		self._RegdCtrctId = base_types.UninitialisedField(self, 'RegdCtrctId', Max35Text, False)

	@property
	def RegnAgt(self):
		return self._RegnAgt

	@RegnAgt.setter
	def RegnAgt(self, value):
		self._RegnAgt = value if value is not None else base_types.UninitialisedField(self, 'RegnAgt', BranchAndFinancialInstitutionIdentification8, False)

	@RegnAgt.deleter
	def RegnAgt(self):
		del self._RegnAgt
		self._RegnAgt = base_types.UninitialisedField(self, 'RegnAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def RptgPrd(self):
		return self._RptgPrd

	@RptgPrd.setter
	def RptgPrd(self, value):
		self._RptgPrd = value if value is not None else base_types.UninitialisedField(self, 'RptgPrd', ReportingPeriod4, False)

	@RptgPrd.deleter
	def RptgPrd(self):
		del self._RptgPrd
		self._RptgPrd = base_types.UninitialisedField(self, 'RptgPrd', ReportingPeriod4, False)

	@property
	def RptgPty(self):
		return self._RptgPty

	@RptgPty.setter
	def RptgPty(self, value):
		self._RptgPty = value if value is not None else base_types.UninitialisedField(self, 'RptgPty', TradeParty6, False)

	@RptgPty.deleter
	def RptgPty(self):
		del self._RptgPty
		self._RptgPty = base_types.UninitialisedField(self, 'RptgPty', TradeParty6, False)

	@property
	def RtrCrit(self):
		return self._RtrCrit

	@RtrCrit.setter
	def RtrCrit(self, value):
		self._RtrCrit = value if value is not None else base_types.UninitialisedField(self, 'RtrCrit', ContractRegistrationStatementCriteria1, False)

	@RtrCrit.deleter
	def RtrCrit(self):
		del self._RtrCrit
		self._RtrCrit = base_types.UninitialisedField(self, 'RtrCrit', ContractRegistrationStatementCriteria1, False)

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
	def StmtReqId(self):
		return self._StmtReqId

	@StmtReqId.setter
	def StmtReqId(self, value):
		self._StmtReqId = value if value is not None else base_types.UninitialisedField(self, 'StmtReqId', Max35Text, False)

	@StmtReqId.deleter
	def StmtReqId(self):
		del self._StmtReqId
		self._StmtReqId = base_types.UninitialisedField(self, 'StmtReqId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegdCtrctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPrd', type=ReportingPeriod4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RtrCrit', type=ContractRegistrationStatementCriteria1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtReqId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))