# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveAmountRange3Choice
from . import ActiveCurrencyCode
from . import ActiveOrHistoricAmountRange2Choice
from . import ActiveOrHistoricCurrencyCode
from . import CreditDebitCode
from . import DateAndDateTimeSearch3Choice
from . import DateTimePeriod1Choice
from . import ISODate
from . import Instruction1Code
from . import InstructionStatusSearch5
from . import Max35Text
from . import PaymentIdentification8Choice
from . import PaymentOrigin1Choice
from . import PaymentTransactionParty4
from . import PaymentType4Choice
from . import Priority1Choice
from . import UUIDv4Identifier

class PaymentSearch10(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_EndToEndId", "_InstdAmt", "_InstdAmtCcy", "_Instr", "_IntrBkSttlmAmt", "_IntrBkSttlmAmtCcy", "_IntrBkSttlmDt", "_MsgId", "_PmtId", "_PmtMtd", "_PmtTp", "_PrcgVldtyTm", "_Prty", "_Pties", "_ReqdExctnDt", "_Sts", "_TxId", "_UETR"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def EndToEndId(self):
		return self._EndToEndId

	@EndToEndId.setter
	def EndToEndId(self, value):
		self._EndToEndId = value if value is not None else base_types.UninitialisedField(self, 'EndToEndId', Max35Text, True)

	@EndToEndId.deleter
	def EndToEndId(self):
		del self._EndToEndId
		self._EndToEndId = base_types.UninitialisedField(self, 'EndToEndId', Max35Text, True)

	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if value is not None else base_types.UninitialisedField(self, 'InstdAmt', ActiveOrHistoricAmountRange2Choice, True)

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = base_types.UninitialisedField(self, 'InstdAmt', ActiveOrHistoricAmountRange2Choice, True)

	@property
	def InstdAmtCcy(self):
		return self._InstdAmtCcy

	@InstdAmtCcy.setter
	def InstdAmtCcy(self, value):
		self._InstdAmtCcy = value if value is not None else base_types.UninitialisedField(self, 'InstdAmtCcy', ActiveOrHistoricCurrencyCode, True)

	@InstdAmtCcy.deleter
	def InstdAmtCcy(self):
		del self._InstdAmtCcy
		self._InstdAmtCcy = base_types.UninitialisedField(self, 'InstdAmtCcy', ActiveOrHistoricCurrencyCode, True)

	@property
	def Instr(self):
		return self._Instr

	@Instr.setter
	def Instr(self, value):
		self._Instr = value if value is not None else base_types.UninitialisedField(self, 'Instr', Instruction1Code, True)

	@Instr.deleter
	def Instr(self):
		del self._Instr
		self._Instr = base_types.UninitialisedField(self, 'Instr', Instruction1Code, True)

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmAmt', ActiveAmountRange3Choice, True)

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = base_types.UninitialisedField(self, 'IntrBkSttlmAmt', ActiveAmountRange3Choice, True)

	@property
	def IntrBkSttlmAmtCcy(self):
		return self._IntrBkSttlmAmtCcy

	@IntrBkSttlmAmtCcy.setter
	def IntrBkSttlmAmtCcy(self, value):
		self._IntrBkSttlmAmtCcy = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmAmtCcy', ActiveCurrencyCode, True)

	@IntrBkSttlmAmtCcy.deleter
	def IntrBkSttlmAmtCcy(self):
		del self._IntrBkSttlmAmtCcy
		self._IntrBkSttlmAmtCcy = base_types.UninitialisedField(self, 'IntrBkSttlmAmtCcy', ActiveCurrencyCode, True)

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, True)

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, True)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, True)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, True)

	@property
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if value is not None else base_types.UninitialisedField(self, 'PmtId', PaymentIdentification8Choice, True)

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = base_types.UninitialisedField(self, 'PmtId', PaymentIdentification8Choice, True)

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if value is not None else base_types.UninitialisedField(self, 'PmtMtd', PaymentOrigin1Choice, True)

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = base_types.UninitialisedField(self, 'PmtMtd', PaymentOrigin1Choice, True)

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if value is not None else base_types.UninitialisedField(self, 'PmtTp', PaymentType4Choice, True)

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = base_types.UninitialisedField(self, 'PmtTp', PaymentType4Choice, True)

	@property
	def PrcgVldtyTm(self):
		return self._PrcgVldtyTm

	@PrcgVldtyTm.setter
	def PrcgVldtyTm(self, value):
		self._PrcgVldtyTm = value if value is not None else base_types.UninitialisedField(self, 'PrcgVldtyTm', DateTimePeriod1Choice, True)

	@PrcgVldtyTm.deleter
	def PrcgVldtyTm(self):
		del self._PrcgVldtyTm
		self._PrcgVldtyTm = base_types.UninitialisedField(self, 'PrcgVldtyTm', DateTimePeriod1Choice, True)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', Priority1Choice, True)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', Priority1Choice, True)

	@property
	def Pties(self):
		return self._Pties

	@Pties.setter
	def Pties(self, value):
		self._Pties = value if value is not None else base_types.UninitialisedField(self, 'Pties', PaymentTransactionParty4, False)

	@Pties.deleter
	def Pties(self):
		del self._Pties
		self._Pties = base_types.UninitialisedField(self, 'Pties', PaymentTransactionParty4, False)

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDt', DateAndDateTimeSearch3Choice, True)

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = base_types.UninitialisedField(self, 'ReqdExctnDt', DateAndDateTimeSearch3Choice, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', InstructionStatusSearch5, True)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', InstructionStatusSearch5, True)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', Max35Text, True)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', Max35Text, True)

	@property
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if value is not None else base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, True)

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = base_types.UninitialisedField(self, 'UETR', UUIDv4Identifier, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndToEndId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstdAmt', type=ActiveOrHistoricAmountRange2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstdAmtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Instr', type=Instruction1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ActiveAmountRange3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrBkSttlmAmtCcy', type=ActiveCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification8Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtMtd', type=PaymentOrigin1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtTp', type=PaymentType4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgVldtyTm', type=DateTimePeriod1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prty', type=Priority1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pties', type=PaymentTransactionParty4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTimeSearch3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=InstructionStatusSearch5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=None, mutex_group=None, array=True),
	))