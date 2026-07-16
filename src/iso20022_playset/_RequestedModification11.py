# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import AmountType4Choice
from . import CashAccount40
from . import ChargeBearerType1Code
from . import DateAndDateTime2Choice
from . import ISODate
from . import InstructionForCreditorAgent3
from . import InstructionForNextAgent1
from . import Max140Text
from . import Max35Text
from . import PartyIdentification272
from . import PaymentTypeInformation27
from . import Purpose2Choice
from . import RemittanceInformation22
from . import RemittanceLocation8
from . import SettlementDateTimeIndication1
from . import SettlementInstruction16

class RequestedModification11(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_Cdtr", "_CdtrAcct", "_CdtrAgtAcct", "_ChrgBr", "_Dbtr", "_DbtrAcct", "_DbtrAgtAcct", "_EndToEndId", "_InstrForCdtrAgt", "_InstrForDbtrAgt", "_InstrForNxtAgt", "_InstrId", "_IntrBkSttlmAmt", "_IntrBkSttlmDt", "_PmtTpInf", "_Purp", "_ReqdColltnDt", "_ReqdExctnDt", "_RltdRmtInf", "_RmtInf", "_SttlmInf", "_SttlmTmIndctn", "_TxId", "_UltmtCdtr", "_UltmtDbtr"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', AmountType4Choice, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', AmountType4Choice, False)

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
	def DbtrAgtAcct(self):
		return self._DbtrAgtAcct

	@DbtrAgtAcct.setter
	def DbtrAgtAcct(self, value):
		self._DbtrAgtAcct = value if value is not None else base_types.UninitialisedField(self, 'DbtrAgtAcct', CashAccount40, False)

	@DbtrAgtAcct.deleter
	def DbtrAgtAcct(self):
		del self._DbtrAgtAcct
		self._DbtrAgtAcct = base_types.UninitialisedField(self, 'DbtrAgtAcct', CashAccount40, False)

	@property
	def EndToEndId(self):
		return self._EndToEndId

	@EndToEndId.setter
	def EndToEndId(self, value):
		self._EndToEndId = value if value is not None else base_types.UninitialisedField(self, 'EndToEndId', Max35Text, False)

	@EndToEndId.deleter
	def EndToEndId(self):
		del self._EndToEndId
		self._EndToEndId = base_types.UninitialisedField(self, 'EndToEndId', Max35Text, False)

	@property
	def InstrForCdtrAgt(self):
		return self._InstrForCdtrAgt

	@InstrForCdtrAgt.setter
	def InstrForCdtrAgt(self, value):
		self._InstrForCdtrAgt = value if value is not None else base_types.UninitialisedField(self, 'InstrForCdtrAgt', InstructionForCreditorAgent3, True)

	@InstrForCdtrAgt.deleter
	def InstrForCdtrAgt(self):
		del self._InstrForCdtrAgt
		self._InstrForCdtrAgt = base_types.UninitialisedField(self, 'InstrForCdtrAgt', InstructionForCreditorAgent3, True)

	@property
	def InstrForDbtrAgt(self):
		return self._InstrForDbtrAgt

	@InstrForDbtrAgt.setter
	def InstrForDbtrAgt(self, value):
		self._InstrForDbtrAgt = value if value is not None else base_types.UninitialisedField(self, 'InstrForDbtrAgt', Max140Text, False)

	@InstrForDbtrAgt.deleter
	def InstrForDbtrAgt(self):
		del self._InstrForDbtrAgt
		self._InstrForDbtrAgt = base_types.UninitialisedField(self, 'InstrForDbtrAgt', Max140Text, False)

	@property
	def InstrForNxtAgt(self):
		return self._InstrForNxtAgt

	@InstrForNxtAgt.setter
	def InstrForNxtAgt(self, value):
		self._InstrForNxtAgt = value if value is not None else base_types.UninitialisedField(self, 'InstrForNxtAgt', InstructionForNextAgent1, True)

	@InstrForNxtAgt.deleter
	def InstrForNxtAgt(self):
		del self._InstrForNxtAgt
		self._InstrForNxtAgt = base_types.UninitialisedField(self, 'InstrForNxtAgt', InstructionForNextAgent1, True)

	@property
	def InstrId(self):
		return self._InstrId

	@InstrId.setter
	def InstrId(self, value):
		self._InstrId = value if value is not None else base_types.UninitialisedField(self, 'InstrId', Max35Text, False)

	@InstrId.deleter
	def InstrId(self):
		del self._InstrId
		self._InstrId = base_types.UninitialisedField(self, 'InstrId', Max35Text, False)

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = base_types.UninitialisedField(self, 'IntrBkSttlmAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, False)

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, False)

	@property
	def PmtTpInf(self):
		return self._PmtTpInf

	@PmtTpInf.setter
	def PmtTpInf(self, value):
		self._PmtTpInf = value if value is not None else base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation27, False)

	@PmtTpInf.deleter
	def PmtTpInf(self):
		del self._PmtTpInf
		self._PmtTpInf = base_types.UninitialisedField(self, 'PmtTpInf', PaymentTypeInformation27, False)

	@property
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', Purpose2Choice, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', Purpose2Choice, False)

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
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDt', DateAndDateTime2Choice, False)

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = base_types.UninitialisedField(self, 'ReqdExctnDt', DateAndDateTime2Choice, False)

	@property
	def RltdRmtInf(self):
		return self._RltdRmtInf

	@RltdRmtInf.setter
	def RltdRmtInf(self, value):
		self._RltdRmtInf = value if value is not None else base_types.UninitialisedField(self, 'RltdRmtInf', RemittanceLocation8, True)

	@RltdRmtInf.deleter
	def RltdRmtInf(self):
		del self._RltdRmtInf
		self._RltdRmtInf = base_types.UninitialisedField(self, 'RltdRmtInf', RemittanceLocation8, True)

	@property
	def RmtInf(self):
		return self._RmtInf

	@RmtInf.setter
	def RmtInf(self, value):
		self._RmtInf = value if value is not None else base_types.UninitialisedField(self, 'RmtInf', RemittanceInformation22, False)

	@RmtInf.deleter
	def RmtInf(self):
		del self._RmtInf
		self._RmtInf = base_types.UninitialisedField(self, 'RmtInf', RemittanceInformation22, False)

	@property
	def SttlmInf(self):
		return self._SttlmInf

	@SttlmInf.setter
	def SttlmInf(self, value):
		self._SttlmInf = value if value is not None else base_types.UninitialisedField(self, 'SttlmInf', SettlementInstruction16, False)

	@SttlmInf.deleter
	def SttlmInf(self):
		del self._SttlmInf
		self._SttlmInf = base_types.UninitialisedField(self, 'SttlmInf', SettlementInstruction16, False)

	@property
	def SttlmTmIndctn(self):
		return self._SttlmTmIndctn

	@SttlmTmIndctn.setter
	def SttlmTmIndctn(self, value):
		self._SttlmTmIndctn = value if value is not None else base_types.UninitialisedField(self, 'SttlmTmIndctn', SettlementDateTimeIndication1, False)

	@SttlmTmIndctn.deleter
	def SttlmTmIndctn(self):
		del self._SttlmTmIndctn
		self._SttlmTmIndctn = base_types.UninitialisedField(self, 'SttlmTmIndctn', SettlementDateTimeIndication1, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, False)

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
		base_types.FieldEntry(name='Amt', type=AmountType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChrgBr', type=ChargeBearerType1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Dbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrAgtAcct', type=CashAccount40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForCdtrAgt', type=InstructionForCreditorAgent3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrForDbtrAgt', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrForNxtAgt', type=InstructionForNextAgent1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtTpInf', type=PaymentTypeInformation27, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Purpose2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdColltnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdRmtInf', type=RemittanceLocation8, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='RmtInf', type=RemittanceInformation22, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmInf', type=SettlementInstruction16, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmTmIndctn', type=SettlementDateTimeIndication1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=PartyIdentification272, min=0, max=1, mutex_group=None, array=False),
	))