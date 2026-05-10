import base_types
import ReferredMandateDocument2
import PartyIdentification272
import CashAccount40
import MandateOccurrences5
import MandateAdjustment1
import Max35Text
import BranchAndFinancialInstitutionIdentification8
import TrueFalseIndicator
import MandateSetupReason1Choice
import ActiveOrHistoricCurrencyAndAmount
import MandateTypeInformation2
import MandateAuthentication1

class Mandate20(base_types._BaseFieldType):

	__slots__ = ["_MndtRef", "_CdtrSchmeId", "_ColltnAmt", "_UltmtCdtr", "_MndtReqId", "_Tp", "_CdtrAgt", "_DbtrAgt", "_Cdtr", "_UltmtDbtr", "_Adjstmnt", "_RfrdDoc", "_CdtrAcct", "_MndtId", "_TrckgInd", "_Dbtr", "_Authntcn", "_Ocrncs", "_Rsn", "_MaxAmt", "_DbtrAcct", "_FrstColltnAmt"]
	@property
	def MndtRef(self):
		return self._MndtRef

	@MndtRef.setter
	def MndtRef(self, value):
		self._MndtRef = value if type(value) != auto else self.make_default("MndtRef")

	@MndtRef.deleter
	def MndtRef(self):
		del self._MndtRef
		self._MndtRef = None

	@property
	def CdtrSchmeId(self):
		return self._CdtrSchmeId

	@CdtrSchmeId.setter
	def CdtrSchmeId(self, value):
		self._CdtrSchmeId = value if type(value) != auto else self.make_default("CdtrSchmeId")

	@CdtrSchmeId.deleter
	def CdtrSchmeId(self):
		del self._CdtrSchmeId
		self._CdtrSchmeId = None

	@property
	def ColltnAmt(self):
		return self._ColltnAmt

	@ColltnAmt.setter
	def ColltnAmt(self, value):
		self._ColltnAmt = value if type(value) != auto else self.make_default("ColltnAmt")

	@ColltnAmt.deleter
	def ColltnAmt(self):
		del self._ColltnAmt
		self._ColltnAmt = None

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
	def MndtReqId(self):
		return self._MndtReqId

	@MndtReqId.setter
	def MndtReqId(self, value):
		self._MndtReqId = value if type(value) != auto else self.make_default("MndtReqId")

	@MndtReqId.deleter
	def MndtReqId(self):
		del self._MndtReqId
		self._MndtReqId = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

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
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

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
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if type(value) != auto else self.make_default("Adjstmnt")

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = None

	@property
	def RfrdDoc(self):
		return self._RfrdDoc

	@RfrdDoc.setter
	def RfrdDoc(self, value):
		self._RfrdDoc = value if type(value) != auto else self.make_default("RfrdDoc")

	@RfrdDoc.deleter
	def RfrdDoc(self):
		del self._RfrdDoc
		self._RfrdDoc = None

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
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if type(value) != auto else self.make_default("MndtId")

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = None

	@property
	def TrckgInd(self):
		return self._TrckgInd

	@TrckgInd.setter
	def TrckgInd(self, value):
		self._TrckgInd = value if type(value) != auto else self.make_default("TrckgInd")

	@TrckgInd.deleter
	def TrckgInd(self):
		del self._TrckgInd
		self._TrckgInd = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

	@property
	def Authntcn(self):
		return self._Authntcn

	@Authntcn.setter
	def Authntcn(self, value):
		self._Authntcn = value if type(value) != auto else self.make_default("Authntcn")

	@Authntcn.deleter
	def Authntcn(self):
		del self._Authntcn
		self._Authntcn = None

	@property
	def Ocrncs(self):
		return self._Ocrncs

	@Ocrncs.setter
	def Ocrncs(self, value):
		self._Ocrncs = value if type(value) != auto else self.make_default("Ocrncs")

	@Ocrncs.deleter
	def Ocrncs(self):
		del self._Ocrncs
		self._Ocrncs = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def MaxAmt(self):
		return self._MaxAmt

	@MaxAmt.setter
	def MaxAmt(self, value):
		self._MaxAmt = value if type(value) != auto else self.make_default("MaxAmt")

	@MaxAmt.deleter
	def MaxAmt(self):
		del self._MaxAmt
		self._MaxAmt = None

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if type(value) != auto else self.make_default("DbtrAcct")

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = None

	@property
	def FrstColltnAmt(self):
		return self._FrstColltnAmt

	@FrstColltnAmt.setter
	def FrstColltnAmt(self, value):
		self._FrstColltnAmt = value if type(value) != auto else self.make_default("FrstColltnAmt")

	@FrstColltnAmt.deleter
	def FrstColltnAmt(self):
		del self._FrstColltnAmt
		self._FrstColltnAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MndtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrSchmeId', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ColltnAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtReqId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MandateTypeInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adjstmnt', type=MandateAdjustment1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdDoc', type=ReferredMandateDocument2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckgInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Authntcn', type=MandateAuthentication1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ocrncs', type=MandateOccurrences5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=MandateSetupReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstColltnAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

