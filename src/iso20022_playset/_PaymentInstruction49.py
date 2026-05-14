from . import base_types
from ._BatchBookingIndicator import BatchBookingIndicator
from ._BranchAndFinancialInstitutionIdentification8 import BranchAndFinancialInstitutionIdentification8
from ._CashAccount40 import CashAccount40
from ._ChargeBearerType1Code import ChargeBearerType1Code
from ._CreditTransferTransaction78 import CreditTransferTransaction78
from ._DecimalNumber import DecimalNumber
from ._ISODate import ISODate
from ._Max140Text import Max140Text
from ._Max15NumericText import Max15NumericText
from ._Max35Text import Max35Text
from ._PartyIdentification272 import PartyIdentification272
from ._PaymentMethod3Code import PaymentMethod3Code
from ._PaymentTypeInformation26 import PaymentTypeInformation26

class PaymentInstruction49(base_types._BaseFieldType):

	__slots__ = ["_BtchBookg", "_CdtTrfTxInf", "_ChrgBr", "_ChrgsAcct", "_ChrgsAcctAgt", "_CtrlSum", "_Dbtr", "_DbtrAcct", "_DbtrAgt", "_DbtrAgtAcct", "_InstrForDbtrAgt", "_NbOfTxs", "_PmtInfId", "_PmtMtd", "_PmtTpInf", "_PoolgAdjstmntDt", "_ReqdExctnDt", "_UltmtDbtr"]
	@property
	def BtchBookg(self):
		return self._BtchBookg

	@BtchBookg.setter
	def BtchBookg(self, value):
		self._BtchBookg = value if type(value) != base_types.auto else self.make_default("BtchBookg")

	@BtchBookg.deleter
	def BtchBookg(self):
		del self._BtchBookg
		self._BtchBookg = None

	@property
	def CdtTrfTxInf(self):
		return self._CdtTrfTxInf

	@CdtTrfTxInf.setter
	def CdtTrfTxInf(self, value):
		self._CdtTrfTxInf = value if type(value) != base_types.auto else self.make_default("CdtTrfTxInf")

	@CdtTrfTxInf.deleter
	def CdtTrfTxInf(self):
		del self._CdtTrfTxInf
		self._CdtTrfTxInf = None

	@property
	def ChrgBr(self):
		return self._ChrgBr

	@ChrgBr.setter
	def ChrgBr(self, value):
		self._ChrgBr = value if type(value) != base_types.auto else self.make_default("ChrgBr")

	@ChrgBr.deleter
	def ChrgBr(self):
		del self._ChrgBr
		self._ChrgBr = None

	@property
	def ChrgsAcct(self):
		return self._ChrgsAcct

	@ChrgsAcct.setter
	def ChrgsAcct(self, value):
		self._ChrgsAcct = value if type(value) != base_types.auto else self.make_default("ChrgsAcct")

	@ChrgsAcct.deleter
	def ChrgsAcct(self):
		del self._ChrgsAcct
		self._ChrgsAcct = None

	@property
	def ChrgsAcctAgt(self):
		return self._ChrgsAcctAgt

	@ChrgsAcctAgt.setter
	def ChrgsAcctAgt(self, value):
		self._ChrgsAcctAgt = value if type(value) != base_types.auto else self.make_default("ChrgsAcctAgt")

	@ChrgsAcctAgt.deleter
	def ChrgsAcctAgt(self):
		del self._ChrgsAcctAgt
		self._ChrgsAcctAgt = None

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if type(value) != base_types.auto else self.make_default("CtrlSum")

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != base_types.auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

	@property
	def DbtrAcct(self):
		return self._DbtrAcct

	@DbtrAcct.setter
	def DbtrAcct(self, value):
		self._DbtrAcct = value if type(value) != base_types.auto else self.make_default("DbtrAcct")

	@DbtrAcct.deleter
	def DbtrAcct(self):
		del self._DbtrAcct
		self._DbtrAcct = None

	@property
	def DbtrAgt(self):
		return self._DbtrAgt

	@DbtrAgt.setter
	def DbtrAgt(self, value):
		self._DbtrAgt = value if type(value) != base_types.auto else self.make_default("DbtrAgt")

	@DbtrAgt.deleter
	def DbtrAgt(self):
		del self._DbtrAgt
		self._DbtrAgt = None

	@property
	def DbtrAgtAcct(self):
		return self._DbtrAgtAcct

	@DbtrAgtAcct.setter
	def DbtrAgtAcct(self, value):
		self._DbtrAgtAcct = value if type(value) != base_types.auto else self.make_default("DbtrAgtAcct")

	@DbtrAgtAcct.deleter
	def DbtrAgtAcct(self):
		del self._DbtrAgtAcct
		self._DbtrAgtAcct = None

	@property
	def InstrForDbtrAgt(self):
		return self._InstrForDbtrAgt

	@InstrForDbtrAgt.setter
	def InstrForDbtrAgt(self, value):
		self._InstrForDbtrAgt = value if type(value) != base_types.auto else self.make_default("InstrForDbtrAgt")

	@InstrForDbtrAgt.deleter
	def InstrForDbtrAgt(self):
		del self._InstrForDbtrAgt
		self._InstrForDbtrAgt = None

	@property
	def NbOfTxs(self):
		return self._NbOfTxs

	@NbOfTxs.setter
	def NbOfTxs(self, value):
		self._NbOfTxs = value if type(value) != base_types.auto else self.make_default("NbOfTxs")

	@NbOfTxs.deleter
	def NbOfTxs(self):
		del self._NbOfTxs
		self._NbOfTxs = None

	@property
	def PmtInfId(self):
		return self._PmtInfId

	@PmtInfId.setter
	def PmtInfId(self, value):
		self._PmtInfId = value if type(value) != base_types.auto else self.make_default("PmtInfId")

	@PmtInfId.deleter
	def PmtInfId(self):
		del self._PmtInfId
		self._PmtInfId = None

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if type(value) != base_types.auto else self.make_default("PmtMtd")

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = None

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if type(value) != base_types.auto else self.make_default("PmtTpInf")

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = None

	@property
	def PoolgAdjstmntDt(self):
		return self._PoolgAdjstmntDt

	@PoolgAdjstmntDt.setter
	def PoolgAdjstmntDt(self, value):
		self._PoolgAdjstmntDt = value if type(value) != base_types.auto else self.make_default("PoolgAdjstmntDt")

	@PoolgAdjstmntDt.deleter
	def PoolgAdjstmntDt(self):
		del self._PoolgAdjstmntDt
		self._PoolgAdjstmntDt = None

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if type(value) != base_types.auto else self.make_default("ReqdExctnDt")

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = None

	@property
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if type(value) != base_types.auto else self.make_default("UltmtDbtr")

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchBookg', type=BatchBookingIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtTrfTxInf', type=CreditTransferTransaction78, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgsAcctAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgt', type=BranchAndFinancialInstitutionIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForDbtrAgt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfTxs', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInfId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=PaymentMethod3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation26, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PoolgAdjstmntDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
	))

