# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BranchAndFinancialInstitutionIdentification8
from . import GenericValidationRuleIdentification1
from . import Max35Text
from . import RegisteredContract18
from . import ReportingPeriod4
from . import SupplementaryData1
from . import SupportingDocument4
from . import TradeParty6
from . import TransactionCertificate4

class ContractRegistrationStatement4(base_types._BaseFieldType):

	__slots__ = ["_AddtlSpprtgDocJrnl", "_RegdCtrct", "_RegnAgt", "_RgltryRuleVldtn", "_RptgPrd", "_RptgPty", "_SplmtryData", "_SpprtgDocJrnl", "_StmtId", "_TtlCtrctTrnvrSum", "_TxJrnl"]
	@property
	def AddtlSpprtgDocJrnl(self):
		return self._AddtlSpprtgDocJrnl

	@AddtlSpprtgDocJrnl.setter
	def AddtlSpprtgDocJrnl(self, value):
		self._AddtlSpprtgDocJrnl = value if value is not None else base_types.UninitialisedField(self, 'AddtlSpprtgDocJrnl', SupportingDocument4, True)

	@AddtlSpprtgDocJrnl.deleter
	def AddtlSpprtgDocJrnl(self):
		del self._AddtlSpprtgDocJrnl
		self._AddtlSpprtgDocJrnl = base_types.UninitialisedField(self, 'AddtlSpprtgDocJrnl', SupportingDocument4, True)

	@property
	def RegdCtrct(self):
		return self._RegdCtrct

	@RegdCtrct.setter
	def RegdCtrct(self, value):
		self._RegdCtrct = value if value is not None else base_types.UninitialisedField(self, 'RegdCtrct', RegisteredContract18, False)

	@RegdCtrct.deleter
	def RegdCtrct(self):
		del self._RegdCtrct
		self._RegdCtrct = base_types.UninitialisedField(self, 'RegdCtrct', RegisteredContract18, False)

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
	def RgltryRuleVldtn(self):
		return self._RgltryRuleVldtn

	@RgltryRuleVldtn.setter
	def RgltryRuleVldtn(self, value):
		self._RgltryRuleVldtn = value if value is not None else base_types.UninitialisedField(self, 'RgltryRuleVldtn', GenericValidationRuleIdentification1, True)

	@RgltryRuleVldtn.deleter
	def RgltryRuleVldtn(self):
		del self._RgltryRuleVldtn
		self._RgltryRuleVldtn = base_types.UninitialisedField(self, 'RgltryRuleVldtn', GenericValidationRuleIdentification1, True)

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
	def SpprtgDocJrnl(self):
		return self._SpprtgDocJrnl

	@SpprtgDocJrnl.setter
	def SpprtgDocJrnl(self, value):
		self._SpprtgDocJrnl = value if value is not None else base_types.UninitialisedField(self, 'SpprtgDocJrnl', SupportingDocument4, True)

	@SpprtgDocJrnl.deleter
	def SpprtgDocJrnl(self):
		del self._SpprtgDocJrnl
		self._SpprtgDocJrnl = base_types.UninitialisedField(self, 'SpprtgDocJrnl', SupportingDocument4, True)

	@property
	def StmtId(self):
		return self._StmtId

	@StmtId.setter
	def StmtId(self, value):
		self._StmtId = value if value is not None else base_types.UninitialisedField(self, 'StmtId', Max35Text, False)

	@StmtId.deleter
	def StmtId(self):
		del self._StmtId
		self._StmtId = base_types.UninitialisedField(self, 'StmtId', Max35Text, False)

	@property
	def TtlCtrctTrnvrSum(self):
		return self._TtlCtrctTrnvrSum

	@TtlCtrctTrnvrSum.setter
	def TtlCtrctTrnvrSum(self, value):
		self._TtlCtrctTrnvrSum = value if value is not None else base_types.UninitialisedField(self, 'TtlCtrctTrnvrSum', ActiveCurrencyAndAmount, False)

	@TtlCtrctTrnvrSum.deleter
	def TtlCtrctTrnvrSum(self):
		del self._TtlCtrctTrnvrSum
		self._TtlCtrctTrnvrSum = base_types.UninitialisedField(self, 'TtlCtrctTrnvrSum', ActiveCurrencyAndAmount, False)

	@property
	def TxJrnl(self):
		return self._TxJrnl

	@TxJrnl.setter
	def TxJrnl(self, value):
		self._TxJrnl = value if value is not None else base_types.UninitialisedField(self, 'TxJrnl', TransactionCertificate4, True)

	@TxJrnl.deleter
	def TxJrnl(self):
		del self._TxJrnl
		self._TxJrnl = base_types.UninitialisedField(self, 'TxJrnl', TransactionCertificate4, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlSpprtgDocJrnl', type=SupportingDocument4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RegdCtrct', type=RegisteredContract18, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryRuleVldtn', type=GenericValidationRuleIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RptgPrd', type=ReportingPeriod4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptgPty', type=TradeParty6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SpprtgDocJrnl', type=SupportingDocument4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StmtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlCtrctTrnvrSum', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxJrnl', type=TransactionCertificate4, min=0, max=None, mutex_group=None, array=True),
	))