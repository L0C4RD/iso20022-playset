# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import MandateAdjustment1
from . import MandateAuthentication1
from . import MandateOccurrences5
from . import MandateSetupReason1Choice
from . import MandateTypeInformation2
from . import Max35Text
from . import PartyIdentification272
from . import ReferredMandateDocument2
from . import TrueFalseIndicator

class Mandate21(base_types._BaseFieldType):

	__slots__ = ["_Adjstmnt", "_Authntcn", "_Cdtr", "_CdtrAcct", "_CdtrAgt", "_CdtrSchmeId", "_ColltnAmt", "_Dbtr", "_DbtrAcct", "_DbtrAgt", "_FrstColltnAmt", "_MaxAmt", "_MndtId", "_MndtRef", "_MndtReqId", "_Ocrncs", "_RfrdDoc", "_Rsn", "_Tp", "_TrckgInd", "_UltmtCdtr", "_UltmtDbtr"]
	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if value is not None else base_types.UninitialisedField(self, 'Adjstmnt', MandateAdjustment1, False)

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = base_types.UninitialisedField(self, 'Adjstmnt', MandateAdjustment1, False)

	@property
	def Authntcn(self):
		return self._Authntcn

	@Authntcn.setter
	def Authntcn(self, value):
		self._Authntcn = value if value is not None else base_types.UninitialisedField(self, 'Authntcn', MandateAuthentication1, False)

	@Authntcn.deleter
	def Authntcn(self):
		del self._Authntcn
		self._Authntcn = base_types.UninitialisedField(self, 'Authntcn', MandateAuthentication1, False)

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', PartyIdentification272, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', PartyIdentification272, False)

	@property
	def CdtrAcct(self):
		return self._CdtrAcct

	@CdtrAcct.setter
	def CdtrAcct(self, value):
		self._CdtrAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@CdtrAcct.deleter
	def CdtrAcct(self):
		del self._CdtrAcct
		self._CdtrAcct = base_types.UninitialisedField(self, 'CdtrAcct', CashAccount40, False)

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = base_types.UninitialisedField(self, 'CdtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def CdtrSchmeId(self):
		return self._CdtrSchmeId

	@CdtrSchmeId.setter
	def CdtrSchmeId(self, value):
		self._CdtrSchmeId = value if value is not None else base_types.UninitialisedField(self, 'CdtrSchmeId', PartyIdentification272, False)

	@CdtrSchmeId.deleter
	def CdtrSchmeId(self):
		del self._CdtrSchmeId
		self._CdtrSchmeId = base_types.UninitialisedField(self, 'CdtrSchmeId', PartyIdentification272, False)

	@property
	def ColltnAmt(self):
		return self._ColltnAmt

	@ColltnAmt.setter
	def ColltnAmt(self, value):
		self._ColltnAmt = value if value is not None else base_types.UninitialisedField(self, 'ColltnAmt', ActiveCurrencyAndAmount, False)

	@ColltnAmt.deleter
	def ColltnAmt(self):
		del self._ColltnAmt
		self._ColltnAmt = base_types.UninitialisedField(self, 'ColltnAmt', ActiveCurrencyAndAmount, False)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', PartyIdentification272, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', PartyIdentification272, False)

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = base_types.UninitialisedField(self, 'DbtrAcct', CashAccount40, False)

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = base_types.UninitialisedField(self, 'DbtrAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def FrstColltnAmt(self):
		return self._FrstColltnAmt

	@FrstColltnAmt.setter
	def FrstColltnAmt(self, value):
		self._FrstColltnAmt = value if value is not None else base_types.UninitialisedField(self, 'FrstColltnAmt', ActiveCurrencyAndAmount, False)

	@FrstColltnAmt.deleter
	def FrstColltnAmt(self):
		del self._FrstColltnAmt
		self._FrstColltnAmt = base_types.UninitialisedField(self, 'FrstColltnAmt', ActiveCurrencyAndAmount, False)

	@property
	def MaxAmt(self):
		return self._MaxAmt

	@MaxAmt.setter
	def MaxAmt(self, value):
		self._MaxAmt = value if value is not None else base_types.UninitialisedField(self, 'MaxAmt', ActiveCurrencyAndAmount, False)

	@MaxAmt.deleter
	def MaxAmt(self):
		del self._MaxAmt
		self._MaxAmt = base_types.UninitialisedField(self, 'MaxAmt', ActiveCurrencyAndAmount, False)

	@property
	def MndtId(self):
		return self._MndtId

	@MndtId.setter
	def MndtId(self, value):
		self._MndtId = value if value is not None else base_types.UninitialisedField(self, 'MndtId', Max35Text, False)

	@MndtId.deleter
	def MndtId(self):
		del self._MndtId
		self._MndtId = base_types.UninitialisedField(self, 'MndtId', Max35Text, False)

	@property
	def MndtRef(self):
		return self._MndtRef

	@MndtRef.setter
	def MndtRef(self, value):
		self._MndtRef = value if value is not None else base_types.UninitialisedField(self, 'MndtRef', Max35Text, False)

	@MndtRef.deleter
	def MndtRef(self):
		del self._MndtRef
		self._MndtRef = base_types.UninitialisedField(self, 'MndtRef', Max35Text, False)

	@property
	def MndtReqId(self):
		return self._MndtReqId

	@MndtReqId.setter
	def MndtReqId(self, value):
		self._MndtReqId = value if value is not None else base_types.UninitialisedField(self, 'MndtReqId', Max35Text, False)

	@MndtReqId.deleter
	def MndtReqId(self):
		del self._MndtReqId
		self._MndtReqId = base_types.UninitialisedField(self, 'MndtReqId', Max35Text, False)

	@property
	def Ocrncs(self):
		return self._Ocrncs

	@Ocrncs.setter
	def Ocrncs(self, value):
		self._Ocrncs = value if value is not None else base_types.UninitialisedField(self, 'Ocrncs', MandateOccurrences5, False)

	@Ocrncs.deleter
	def Ocrncs(self):
		del self._Ocrncs
		self._Ocrncs = base_types.UninitialisedField(self, 'Ocrncs', MandateOccurrences5, False)

	@property
	def RfrdDoc(self):
		return self._RfrdDoc

	@RfrdDoc.setter
	def RfrdDoc(self, value):
		self._RfrdDoc = value if value is not None else base_types.UninitialisedField(self, 'RfrdDoc', ReferredMandateDocument2, True)

	@RfrdDoc.deleter
	def RfrdDoc(self):
		del self._RfrdDoc
		self._RfrdDoc = base_types.UninitialisedField(self, 'RfrdDoc', ReferredMandateDocument2, True)

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if value is not None else base_types.UninitialisedField(self, 'Rsn', MandateSetupReason1Choice, False)

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = base_types.UninitialisedField(self, 'Rsn', MandateSetupReason1Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', MandateTypeInformation2, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', MandateTypeInformation2, False)

	@property
	def TrckgInd(self):
		return self._TrckgInd

	@TrckgInd.setter
	def TrckgInd(self, value):
		self._TrckgInd = value if value is not None else base_types.UninitialisedField(self, 'TrckgInd', TrueFalseIndicator, False)

	@TrckgInd.deleter
	def TrckgInd(self):
		del self._TrckgInd
		self._TrckgInd = base_types.UninitialisedField(self, 'TrckgInd', TrueFalseIndicator, False)

	@property
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if value is not None else base_types.UninitialisedField(self, 'UltmtCdtr', PartyIdentification272, False)

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = base_types.UninitialisedField(self, 'UltmtCdtr', PartyIdentification272, False)

	@property
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if value is not None else base_types.UninitialisedField(self, 'UltmtDbtr', PartyIdentification272, False)

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = base_types.UninitialisedField(self, 'UltmtDbtr', PartyIdentification272, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adjstmnt', type=MandateAdjustment1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Authntcn', type=MandateAuthentication1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrSchmeId', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ColltnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstColltnAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtReqId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ocrncs', type=MandateOccurrences5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RfrdDoc', type=ReferredMandateDocument2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Rsn', type=MandateSetupReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MandateTypeInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrckgInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
	))