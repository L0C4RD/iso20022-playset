# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdviceType1
from . import BatchBookingIndicator
from . import BranchAndFinancialInstitutionIdentification8
from . import CashAccount40
from . import ChargeBearerType1Code
from . import DecimalNumber
from . import DirectDebitTransactionInformation34
from . import ISODate
from . import Max15NumericText
from . import Max35Text
from . import PartyIdentification272
from . import PaymentMethod2Code
from . import PaymentTypeInformation29

class PaymentInstruction50(base_types._BaseFieldType):

	__slots__ = ["_BtchBookg", "_Cdtr", "_CdtrAcct", "_CdtrAgt", "_CdtrAgtAcct", "_CdtrSchmeId", "_ChrgBr", "_ChrgsAcct", "_ChrgsAcctAgt", "_CtrlSum", "_DrctDbtTxInf", "_NbOfTxs", "_PmtInfId", "_PmtMtd", "_PmtTpInf", "_ReqdAdvcTp", "_ReqdColltnDt", "_UltmtCdtr"]
	@property
	def BtchBookg(self):
		return self._BtchBookg

	@BtchBookg.setter
	def BtchBookg(self, value):
		self._BtchBookg = value if value is not None else base_types.UninitialisedField(self, 'BtchBookg', BatchBookingIndicator, False)

	@BtchBookg.deleter
	def BtchBookg(self):
		del self._BtchBookg
		self._BtchBookg = base_types.UninitialisedField(self, 'BtchBookg', BatchBookingIndicator, False)

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
	def CdtrAgtAcct(self):
		return self._CdtrAgtAcct

	@CdtrAgtAcct.setter
	def CdtrAgtAcct(self, value):
		self._CdtrAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'CdtrAgtAcct', CashAccount40, False)

	@CdtrAgtAcct.deleter
	def CdtrAgtAcct(self):
		del self._CdtrAgtAcct
		self._CdtrAgtAcct = base_types.UninitialisedField(self, 'CdtrAgtAcct', CashAccount40, False)

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
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if value is not None else base_types.UninitialisedField(self, 'ChrgBr', ChargeBearerType1Code, False)

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = base_types.UninitialisedField(self, 'ChrgBr', ChargeBearerType1Code, False)

	@property
	def ChrgsAcct(self):
		return self._ChrgsAcct

	@ChrgsAcct.setter
	def ChrgsAcct(self, value):
		self._ChrgsAcct = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAcct', CashAccount40, False)

	@ChrgsAcct.deleter
	def ChrgsAcct(self):
		del self._ChrgsAcct
		self._ChrgsAcct = base_types.UninitialisedField(self, 'ChrgsAcct', CashAccount40, False)

	@property
	def ChrgsAcctAgt(self):
		return self._ChrgsAcctAgt

	@ChrgsAcctAgt.setter
	def ChrgsAcctAgt(self, value):
		self._ChrgsAcctAgt = value if value is not None else base_types.UninitialisedField(self, 'ChrgsAcctAgt', BranchAndFinancialInstitutionIdentification8, False)

	@ChrgsAcctAgt.deleter
	def ChrgsAcctAgt(self):
		del self._ChrgsAcctAgt
		self._ChrgsAcctAgt = base_types.UninitialisedField(self, 'ChrgsAcctAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if value is not None else base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@property
	def DrctDbtTxInf(self):
		return self._DrctDbtTxInf

	@DrctDbtTxInf.setter
	def DrctDbtTxInf(self, value):
		self._DrctDbtTxInf = value if value is not None else base_types.UninitialisedField(self, 'DrctDbtTxInf', DirectDebitTransactionInformation34, True)

	@DrctDbtTxInf.deleter
	def DrctDbtTxInf(self):
		del self._DrctDbtTxInf
		self._DrctDbtTxInf = base_types.UninitialisedField(self, 'DrctDbtTxInf', DirectDebitTransactionInformation34, True)

	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if value is not None else base_types.UninitialisedField(self, 'NbOfTxs', Max15NumericText, False)

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = base_types.UninitialisedField(self, 'NbOfTxs', Max15NumericText, False)

	@property
	def PmtInfId(self):
		return self._PmtInfId

	@PmtInfId.setter
	def PmtInfId(self, value):
		self._PmtInfId = value if value is not None else base_types.UninitialisedField(self, 'PmtInfId', Max35Text, False)

	@PmtInfId.deleter
	def PmtInfId(self):
		del self._PmtInfId
		self._PmtInfId = base_types.UninitialisedField(self, 'PmtInfId', Max35Text, False)

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if value is not None else base_types.UninitialisedField(self, 'PmtMtd', PaymentMethod2Code, False)

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = base_types.UninitialisedField(self, 'PmtMtd', PaymentMethod2Code, False)

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if value is not None else base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation29, False)

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation29, False)

	@property
	def ReqdAdvcTp(self):
		return self._ReqdAdvcTp

	@ReqdAdvcTp.setter
	def ReqdAdvcTp(self, value):
		self._ReqdAdvcTp = value if value is not None else base_types.UninitialisedField(self, 'ReqdAdvcTp', AdviceType1, False)

	@ReqdAdvcTp.deleter
	def ReqdAdvcTp(self):
		del self._ReqdAdvcTp
		self._ReqdAdvcTp = base_types.UninitialisedField(self, 'ReqdAdvcTp', AdviceType1, False)

	@property
	def ReqdColltnDt(self):
		return self._ReqdColltnDt

	@ReqdColltnDt.setter
	def ReqdColltnDt(self, value):
		self._ReqdColltnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdColltnDt', ISODate, False)

	@ReqdColltnDt.deleter
	def ReqdColltnDt(self):
		del self._ReqdColltnDt
		self._ReqdColltnDt = base_types.UninitialisedField(self, 'ReqdColltnDt', ISODate, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchBookg', type=BatchBookingIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrSchmeId', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrctDbtTxInf', type=DirectDebitTransactionInformation34, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=PaymentMethod2Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdAdvcTp', type=AdviceType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdColltnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
	))