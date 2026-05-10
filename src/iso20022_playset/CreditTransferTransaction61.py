import base_types
import PaymentTypeInformation26
import AmountType4Choice
import RemittanceInformation22
import Cheque19
import InstructionForCreditorAgent3
import TaxData1
import Purpose2Choice
import ExchangeRate1
import PartyIdentification272
import PaymentIdentification6
import SupplementaryData1
import InstructionForDebtorAgent1
import RemittanceLocation8
import RegulatoryReporting3
import CashAccount40
import ChargeBearerType1Code
import CreditTransferMandateData1
import BranchAndFinancialInstitutionIdentification8

class CreditTransferTransaction61(base_types._BaseFieldType):

	__slots__ = ["_IntrmyAgt1", "_UltmtCdtr", "_IntrmyAgt2", "_CdtrAgtAcct", "_CdtrAcct", "_IntrmyAgt1Acct", "_Tax", "_CdtrAgt", "_RgltryRptg", "_Purp", "_IntrmyAgt3", "_ChrgBr", "_PmtId", "_UltmtDbtr", "_RltdRmtInf", "_MndtRltdInf", "_ChqInstr", "_Amt", "_XchgRateInf", "_Cdtr", "_InstrForCdtrAgt", "_IntrmyAgt2Acct", "_InstrForDbtrAgt", "_RmtInf", "_PmtTpInf", "_SplmtryData", "_IntrmyAgt3Acct"]
	@property
	def IntrmyAgt1(self):
		return self._IntrmyAgt1

	@IntrmyAgt1.setter
	def IntrmyAgt1(self, value):
		self._IntrmyAgt1 = value if type(value) != auto else self.make_default("IntrmyAgt1")

	@IntrmyAgt1.deleter
	def IntrmyAgt1(self):
		del self._IntrmyAgt1
		self._IntrmyAgt1 = None

	@property
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if type(value) != auto else self.make_default("UltmtCdtr")

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = None

	@property
	def IntrmyAgt2(self):
		return self._IntrmyAgt2

	@IntrmyAgt2.setter
	def IntrmyAgt2(self, value):
		self._IntrmyAgt2 = value if type(value) != auto else self.make_default("IntrmyAgt2")

	@IntrmyAgt2.deleter
	def IntrmyAgt2(self):
		del self._IntrmyAgt2
		self._IntrmyAgt2 = None

	@property
	def CdtrAgtAcct(self):
		return self._CdtrAgtAcct

	@CdtrAgtAcct.setter
	def CdtrAgtAcct(self, value):
		self._CdtrAgtAcct = value if type(value) != auto else self.make_default("CdtrAgtAcct")

	@CdtrAgtAcct.deleter
	def CdtrAgtAcct(self):
		del self._CdtrAgtAcct
		self._CdtrAgtAcct = None

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if type(value) != auto else self.make_default("CdtrAcct")

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = None

	@property
	def IntrmyAgt1Acct(self):
		return self._IntrmyAgt1Acct

	@IntrmyAgt1Acct.setter
	def IntrmyAgt1Acct(self, value):
		self._IntrmyAgt1Acct = value if type(value) != auto else self.make_default("IntrmyAgt1Acct")

	@IntrmyAgt1Acct.deleter
	def IntrmyAgt1Acct(self):
		del self._IntrmyAgt1Acct
		self._IntrmyAgt1Acct = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

	@property
	def RgltryRptg(self):
		return self._RgltryRptg

	@RgltryRptg.setter
	def RgltryRptg(self, value):
		self._RgltryRptg = value if type(value) != auto else self.make_default("RgltryRptg")

	@RgltryRptg.deleter
	def RgltryRptg(self):
		del self._RgltryRptg
		self._RgltryRptg = None

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if type(value) != auto else self.make_default("Purp")

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = None

	@property
	def IntrmyAgt3(self):
		return self._IntrmyAgt3

	@IntrmyAgt3.setter
	def IntrmyAgt3(self, value):
		self._IntrmyAgt3 = value if type(value) != auto else self.make_default("IntrmyAgt3")

	@IntrmyAgt3.deleter
	def IntrmyAgt3(self):
		del self._IntrmyAgt3
		self._IntrmyAgt3 = None

	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

	@property
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if type(value) != auto else self.make_default("PmtId")

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = None

	@property
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if type(value) != auto else self.make_default("UltmtDbtr")

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = None

	@property
	def RltdRmtInf(self):
		return self._RltdRmtInf

	@RltdRmtInf.setter
	def RltdRmtInf(self, value):
		self._RltdRmtInf = value if type(value) != auto else self.make_default("RltdRmtInf")

	@RltdRmtInf.deleter
	def RltdRmtInf(self):
		del self._RltdRmtInf
		self._RltdRmtInf = None

	@property
	def MndtRltdInf(self):
		return self._MndtRltdInf

	@MndtRltdInf.setter
	def MndtRltdInf(self, value):
		self._MndtRltdInf = value if type(value) != auto else self.make_default("MndtRltdInf")

	@MndtRltdInf.deleter
	def MndtRltdInf(self):
		del self._MndtRltdInf
		self._MndtRltdInf = None

	@property
	def ChqInstr(self):
		return self._ChqInstr

	@ChqInstr.setter
	def ChqInstr(self, value):
		self._ChqInstr = value if type(value) != auto else self.make_default("ChqInstr")

	@ChqInstr.deleter
	def ChqInstr(self):
		del self._ChqInstr
		self._ChqInstr = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def XchgRateInf(self):
		return self._XchgRateInf

	@XchgRateInf.setter
	def XchgRateInf(self, value):
		self._XchgRateInf = value if type(value) != auto else self.make_default("XchgRateInf")

	@XchgRateInf.deleter
	def XchgRateInf(self):
		del self._XchgRateInf
		self._XchgRateInf = None

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def InstrForCdtrAgt(self):
		return self._InstrForCdtrAgt

	@InstrForCdtrAgt.setter
	def InstrForCdtrAgt(self, value):
		self._InstrForCdtrAgt = value if type(value) != auto else self.make_default("InstrForCdtrAgt")

	@InstrForCdtrAgt.deleter
	def InstrForCdtrAgt(self):
		del self._InstrForCdtrAgt
		self._InstrForCdtrAgt = None

	@property
	def IntrmyAgt2Acct(self):
		return self._IntrmyAgt2Acct

	@IntrmyAgt2Acct.setter
	def IntrmyAgt2Acct(self, value):
		self._IntrmyAgt2Acct = value if type(value) != auto else self.make_default("IntrmyAgt2Acct")

	@IntrmyAgt2Acct.deleter
	def IntrmyAgt2Acct(self):
		del self._IntrmyAgt2Acct
		self._IntrmyAgt2Acct = None

	@property
	def InstrForDbtrAgt(self):
		return self._InstrForDbtrAgt

	@InstrForDbtrAgt.setter
	def InstrForDbtrAgt(self, value):
		self._InstrForDbtrAgt = value if type(value) != auto else self.make_default("InstrForDbtrAgt")

	@InstrForDbtrAgt.deleter
	def InstrForDbtrAgt(self):
		del self._InstrForDbtrAgt
		self._InstrForDbtrAgt = None

	@property
	def RmtInf(self):
		return self._RmtInf

	@RmtInf.setter
	def RmtInf(self, value):
		self._RmtInf = value if type(value) != auto else self.make_default("RmtInf")

	@RmtInf.deleter
	def RmtInf(self):
		del self._RmtInf
		self._RmtInf = None

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if type(value) != auto else self.make_default("PmtTpInf")

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = None

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
	def IntrmyAgt3Acct(self):
		return self._IntrmyAgt3Acct

	@IntrmyAgt3Acct.setter
	def IntrmyAgt3Acct(self, value):
		self._IntrmyAgt3Acct = value if type(value) != auto else self.make_default("IntrmyAgt3Acct")

	@IntrmyAgt3Acct.deleter
	def IntrmyAgt3Acct(self):
		del self._IntrmyAgt3Acct
		self._IntrmyAgt3Acct = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrmyAgt1', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt2', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt1Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=TaxData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgltryRptg', type=RegulatoryReporting3, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt3', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification6, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRmtInf', type=RemittanceLocation8, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='MndtRltdInf', type=CreditTransferMandateData1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChqInstr', type=Cheque19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=AmountType4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XchgRateInf', type=ExchangeRate1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForCdtrAgt', type=InstructionForCreditorAgent3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrmyAgt2Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForDbtrAgt', type=InstructionForDebtorAgent1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmtInf', type=RemittanceInformation22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrmyAgt3Acct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
	))

