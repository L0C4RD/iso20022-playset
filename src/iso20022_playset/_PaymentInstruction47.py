# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2Choice
from . import Amount3Choice
from . import DateAndDateTime2Choice
from . import DateTimePeriod1Choice
from . import ISODate
from . import Max10Text
from . import Max20000Text
from . import Max35Text
from . import PaymentOrigin1Choice
from . import PaymentStatus6
from . import PaymentTransactionParty4
from . import PaymentType4Choice
from . import Priority1Choice
from . import TrueFalseIndicator

class PaymentInstruction47(base_types._BaseFieldType):

	__slots__ = ["_EndToEndId", "_GnrtdOrdr", "_InstdAmt", "_InstrCpy", "_IntrBkSttlmAmt", "_IntrBkSttlmDt", "_MsgId", "_PmtMtd", "_PrcgVldtyTm", "_Prty", "_Pties", "_Purp", "_ReqdExctnDt", "_Sts", "_Tp", "_TxId"]
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
	def GnrtdOrdr(self):
		return self._GnrtdOrdr

	@GnrtdOrdr.setter
	def GnrtdOrdr(self, value):
		self._GnrtdOrdr = value if value is not None else base_types.UninitialisedField(self, 'GnrtdOrdr', TrueFalseIndicator, False)

	@GnrtdOrdr.deleter
	def GnrtdOrdr(self):
		del self._GnrtdOrdr
		self._GnrtdOrdr = base_types.UninitialisedField(self, 'GnrtdOrdr', TrueFalseIndicator, False)

	@property
	def InstdAmt(self):
		return self._InstdAmt

	@InstdAmt.setter
	def InstdAmt(self, value):
		self._InstdAmt = value if value is not None else base_types.UninitialisedField(self, 'InstdAmt', Amount3Choice, False)

	@InstdAmt.deleter
	def InstdAmt(self):
		del self._InstdAmt
		self._InstdAmt = base_types.UninitialisedField(self, 'InstdAmt', Amount3Choice, False)

	@property
	def InstrCpy(self):
		return self._InstrCpy

	@InstrCpy.setter
	def InstrCpy(self, value):
		self._InstrCpy = value if value is not None else base_types.UninitialisedField(self, 'InstrCpy', Max20000Text, False)

	@InstrCpy.deleter
	def InstrCpy(self):
		del self._InstrCpy
		self._InstrCpy = base_types.UninitialisedField(self, 'InstrCpy', Max20000Text, False)

	@property
	def IntrBkSttlmAmt(self):
		return self._IntrBkSttlmAmt

	@IntrBkSttlmAmt.setter
	def IntrBkSttlmAmt(self, value):
		self._IntrBkSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmAmt', Amount2Choice, False)

	@IntrBkSttlmAmt.deleter
	def IntrBkSttlmAmt(self):
		del self._IntrBkSttlmAmt
		self._IntrBkSttlmAmt = base_types.UninitialisedField(self, 'IntrBkSttlmAmt', Amount2Choice, False)

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
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def PmtMtd(self):
		return self._PmtMtd

	@PmtMtd.setter
	def PmtMtd(self, value):
		self._PmtMtd = value if value is not None else base_types.UninitialisedField(self, 'PmtMtd', PaymentOrigin1Choice, False)

	@PmtMtd.deleter
	def PmtMtd(self):
		del self._PmtMtd
		self._PmtMtd = base_types.UninitialisedField(self, 'PmtMtd', PaymentOrigin1Choice, False)

	@property
	def PrcgVldtyTm(self):
		return self._PrcgVldtyTm

	@PrcgVldtyTm.setter
	def PrcgVldtyTm(self, value):
		self._PrcgVldtyTm = value if value is not None else base_types.UninitialisedField(self, 'PrcgVldtyTm', DateTimePeriod1Choice, False)

	@PrcgVldtyTm.deleter
	def PrcgVldtyTm(self):
		del self._PrcgVldtyTm
		self._PrcgVldtyTm = base_types.UninitialisedField(self, 'PrcgVldtyTm', DateTimePeriod1Choice, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', Priority1Choice, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', Priority1Choice, False)

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
	def Purp(self):
		return self._Purp

	@Purp.setter
	def Purp(self, value):
		self._Purp = value if value is not None else base_types.UninitialisedField(self, 'Purp', Max10Text, False)

	@Purp.deleter
	def Purp(self):
		del self._Purp
		self._Purp = base_types.UninitialisedField(self, 'Purp', Max10Text, False)

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
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', PaymentStatus6, True)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', PaymentStatus6, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', PaymentType4Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', PaymentType4Choice, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndToEndId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GnrtdOrdr', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstdAmt', type=Amount3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrCpy', type=Max20000Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmAmt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtMtd', type=PaymentOrigin1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrcgVldtyTm', type=DateTimePeriod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=Priority1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pties', type=PaymentTransactionParty4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Purp', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=PaymentStatus6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=PaymentType4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))