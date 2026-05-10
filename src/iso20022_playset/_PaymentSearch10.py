from . import base_types
from ._ActiveOrHistoricAmountRange2Choice import ActiveOrHistoricAmountRange2Choice
from ._PaymentTransactionParty4 import PaymentTransactionParty4
from ._InstructionStatusSearch5 import InstructionStatusSearch5
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._Priority1Choice import Priority1Choice
from ._PaymentType4Choice import PaymentType4Choice
from ._DateTimePeriod1Choice import DateTimePeriod1Choice
from ._ISODate import ISODate
from ._ActiveCurrencyCode import ActiveCurrencyCode
from ._PaymentIdentification8Choice import PaymentIdentification8Choice
from ._UUIDv4Identifier import UUIDv4Identifier
from ._Instruction1Code import Instruction1Code
from ._ActiveAmountRange3Choice import ActiveAmountRange3Choice
from ._DateAndDateTimeSearch3Choice import DateAndDateTimeSearch3Choice
from ._Max35Text import Max35Text
from ._PaymentOrigin1Choice import PaymentOrigin1Choice
from ._CreditDebitCode import CreditDebitCode

class PaymentSearch10(base_types._BaseFieldType):

	__slots__ = ["_IntrBkSttlmAmtCcy", "_PrcgVldtyTm", "_PmtId", "_PmtMtd", "_IntrBkSttlmDt", "_InstdAmt", "_CdtDbtInd", "_Prty", "_UETR", "_Instr", "_IntrBkSttlmAmt", "_PmtTp", "_Pties", "_TxId", "_EndToEndId", "_Sts", "_MsgId", "_ReqdExctnDt", "_InstdAmtCcy"]
	@property
	def IntrBkSttlmAmtCcy(self):
		return self._IntrBkSttlmAmtCcy

	@IntrBkSttlmAmtCcy.setter
	def IntrBkSttlmAmtCcy(self, value):
		self._IntrBkSttlmAmtCcy = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmAmtCcy")

	@IntrBkSttlmAmtCcy.deleter
	def IntrBkSttlmAmtCcy(self):
		del self._IntrBkSttlmAmtCcy
		self._IntrBkSttlmAmtCcy = None

	@property
	def PrcgVldtyTm(self):
		return self._PrcgVldtyTm

	@PrcgVldtyTm.setter
	def PrcgVldtyTm(self, value):
		self._PrcgVldtyTm = value if type(value) != base_types.auto else self.make_default("PrcgVldtyTm")

	@PrcgVldtyTm.deleter
	def PrcgVldtyTm(self):
		del self._PrcgVldtyTm
		self._PrcgVldtyTm = None

	@property
	def PmtId(self):
		return self._PmtId

	@PmtId.setter
	def PmtId(self, value):
		self._PmtId = value if type(value) != base_types.auto else self.make_default("PmtId")

	@PmtId.deleter
	def PmtId(self):
		del self._PmtId
		self._PmtId = None

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
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if type(value) != base_types.auto else self.make_default("InstdAmt")

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != base_types.auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != base_types.auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def UETR(self):
		return self._UETR

	@UETR.setter
	def UETR(self, value):
		self._UETR = value if type(value) != base_types.auto else self.make_default("UETR")

	@UETR.deleter
	def UETR(self):
		del self._UETR
		self._UETR = None

	@property
	def Instr(self):
		return self._Instr

	@Instr.setter
	def Instr(self, value):
		self._Instr = value if type(value) != base_types.auto else self.make_default("Instr")

	@Instr.deleter
	def Instr(self):
		del self._Instr
		self._Instr = None

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmAmt")

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = None

	@property
	def PmtTp(self):
		return self._PmtTp

	@PmtTp.setter
	def PmtTp(self, value):
		self._PmtTp = value if type(value) != base_types.auto else self.make_default("PmtTp")

	@PmtTp.deleter
	def PmtTp(self):
		del self._PmtTp
		self._PmtTp = None

	@property
	def Pties(self):
		return self._Pties

	@Pties.setter
	def Pties(self, value):
		self._Pties = value if type(value) != base_types.auto else self.make_default("Pties")

	@Pties.deleter
	def Pties(self):
		del self._Pties
		self._Pties = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def EndToEndId(self):
		return self._EndToEndId

	@EndToEndId.setter
	def EndToEndId(self, value):
		self._EndToEndId = value if type(value) != base_types.auto else self.make_default("EndToEndId")

	@EndToEndId.deleter
	def EndToEndId(self):
		del self._EndToEndId
		self._EndToEndId = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

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
	def InstdAmtCcy(self):
		return self._InstdAmtCcy

	@InstdAmtCcy.setter
	def InstdAmtCcy(self, value):
		self._InstdAmtCcy = value if type(value) != base_types.auto else self.make_default("InstdAmtCcy")

	@InstdAmtCcy.deleter
	def InstdAmtCcy(self):
		del self._InstdAmtCcy
		self._InstdAmtCcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntrBkSttlmAmtCcy', type=ActiveCurrencyCode, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrcgVldtyTm', type=DateTimePeriod1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtId', type=PaymentIdentification8Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtMtd', type=PaymentOrigin1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstdAmt', type=ActiveOrHistoricAmountRange2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=Priority1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UETR', type=UUIDv4Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Instr', type=Instruction1Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=ActiveAmountRange3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PmtTp', type=PaymentType4Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Pties', type=PaymentTransactionParty4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EndToEndId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=InstructionStatusSearch5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTimeSearch3Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstdAmtCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=None, mutex_group=None, array=True),
	))

