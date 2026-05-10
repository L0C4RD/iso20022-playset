import base_types
import DateTimePeriod1Choice
import PaymentStatus6
import Amount3Choice
import Amount2Choice
import PaymentType4Choice
import Max10Text
import ISODate
import DateAndDateTime2Choice
import Max20000Text
import Max35Text
import PaymentOrigin1Choice
import PaymentTransactionParty4
import TrueFalseIndicator
import Priority1Choice

class PaymentInstruction47(base_types._BaseFieldType):

	__slots__ = ["_Prty", "_PrcgVldtyTm", "_IntrBkSttlmAmt", "_Pties", "_Purp", "_PmtMtd", "_IntrBkSttlmDt", "_InstrCpy", "_EndToEndId", "_Sts", "_InstdAmt", "_ReqdExctnDt", "_TxId", "_Tp", "_GnrtdOrdr", "_MsgId"]
	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def PrcgVldtyTm(self):
		return self._PrcgVldtyTm

	@PrcgVldtyTm.setter
	def PrcgVldtyTm(self, value):
		self._PrcgVldtyTm = value if type(value) != auto else self.make_default("PrcgVldtyTm")

	@PrcgVldtyTm.deleter
	def PrcgVldtyTm(self):
		del self._PrcgVldtyTm
		self._PrcgVldtyTm = None

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if type(value) != auto else self.make_default("IntrBkSttlmAmt")

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = None

	@property
	def Pties(self):
		return self._Pties

	@Pties.setter
	def Pties(self, value):
		self._Pties = value if type(value) != auto else self.make_default("Pties")

	@Pties.deleter
	def Pties(self):
		del self._Pties
		self._Pties = None

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
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if type(value) != auto else self.make_default("PmtMtd")

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = None

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

	@property
	def InstrCpy(self):
		return self._InstrCpy

	@InstrCpy.setter
	def InstrCpy(self, value):
		self._InstrCpy = value if type(value) != auto else self.make_default("InstrCpy")

	@InstrCpy.deleter
	def InstrCpy(self):
		del self._InstrCpy
		self._InstrCpy = None

	@property
	def EndToEndId(self):
		return self._EndToEndId

	@EndToEndId.setter
	def EndToEndId(self, value):
		self._EndToEndId = value if type(value) != auto else self.make_default("EndToEndId")

	@EndToEndId.deleter
	def EndToEndId(self):
		del self._EndToEndId
		self._EndToEndId = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if type(value) != auto else self.make_default("InstdAmt")

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = None

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if type(value) != auto else self.make_default("ReqdExctnDt")

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

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
	def GnrtdOrdr(self):
		return self._GnrtdOrdr

	@GnrtdOrdr.setter
	def GnrtdOrdr(self, value):
		self._GnrtdOrdr = value if type(value) != auto else self.make_default("GnrtdOrdr")

	@GnrtdOrdr.deleter
	def GnrtdOrdr(self):
		del self._GnrtdOrdr
		self._GnrtdOrdr = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prty', type=Priority1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgVldtyTm', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pties', type=PaymentTransactionParty4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=PaymentOrigin1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCpy', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=PaymentStatus6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstdAmt', type=Amount3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=PaymentType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnrtdOrdr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

