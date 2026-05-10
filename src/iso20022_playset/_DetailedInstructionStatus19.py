from . import base_types
from .PartyIdentification231Choice import PartyIdentification231Choice
from .Vote19 import Vote19
from .Max35Text import Max35Text
from .PartyIdentification232Choice import PartyIdentification232Choice
from .DateAndDateTime1Choice import DateAndDateTime1Choice
from .PartyIdentification246Choice import PartyIdentification246Choice
from .YesNoIndicator import YesNoIndicator
from .ModalityOfCounting1Choice import ModalityOfCounting1Choice

class DetailedInstructionStatus19(base_types._BaseFieldType):

	__slots__ = ["_ModltyOfCntg", "_RghtsHldr", "_VoteRctDtTm", "_Prxy", "_SnglInstrId", "_StgInstr", "_AcctId", "_VotePerRsltn", "_SubAcctId", "_AcctOwnr"]
	@property
	def ModltyOfCntg(self):
		return self._ModltyOfCntg

	@ModltyOfCntg.setter
	def ModltyOfCntg(self, value):
		self._ModltyOfCntg = value if type(value) != base_types.auto else self.make_default("ModltyOfCntg")

	@ModltyOfCntg.deleter
	def ModltyOfCntg(self):
		del self._ModltyOfCntg
		self._ModltyOfCntg = None

	@property
	def RghtsHldr(self):
		return self._RghtsHldr

	@RghtsHldr.setter
	def RghtsHldr(self, value):
		self._RghtsHldr = value if type(value) != base_types.auto else self.make_default("RghtsHldr")

	@RghtsHldr.deleter
	def RghtsHldr(self):
		del self._RghtsHldr
		self._RghtsHldr = None

	@property
	def VoteRctDtTm(self):
		return self._VoteRctDtTm

	@VoteRctDtTm.setter
	def VoteRctDtTm(self, value):
		self._VoteRctDtTm = value if type(value) != base_types.auto else self.make_default("VoteRctDtTm")

	@VoteRctDtTm.deleter
	def VoteRctDtTm(self):
		del self._VoteRctDtTm
		self._VoteRctDtTm = None

	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if type(value) != base_types.auto else self.make_default("Prxy")

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = None

	@property
	def SnglInstrId(self):
		return self._SnglInstrId

	@SnglInstrId.setter
	def SnglInstrId(self, value):
		self._SnglInstrId = value if type(value) != base_types.auto else self.make_default("SnglInstrId")

	@SnglInstrId.deleter
	def SnglInstrId(self):
		del self._SnglInstrId
		self._SnglInstrId = None

	@property
	def StgInstr(self):
		return self._StgInstr

	@StgInstr.setter
	def StgInstr(self, value):
		self._StgInstr = value if type(value) != base_types.auto else self.make_default("StgInstr")

	@StgInstr.deleter
	def StgInstr(self):
		del self._StgInstr
		self._StgInstr = None

	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if type(value) != base_types.auto else self.make_default("AcctId")

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = None

	@property
	def VotePerRsltn(self):
		return self._VotePerRsltn

	@VotePerRsltn.setter
	def VotePerRsltn(self, value):
		self._VotePerRsltn = value if type(value) != base_types.auto else self.make_default("VotePerRsltn")

	@VotePerRsltn.deleter
	def VotePerRsltn(self):
		del self._VotePerRsltn
		self._VotePerRsltn = None

	@property
	def SubAcctId(self):
		return self._SubAcctId

	@SubAcctId.setter
	def SubAcctId(self, value):
		self._SubAcctId = value if type(value) != base_types.auto else self.make_default("SubAcctId")

	@SubAcctId.deleter
	def SubAcctId(self):
		del self._SubAcctId
		self._SubAcctId = None

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if type(value) != base_types.auto else self.make_default("AcctOwnr")

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ModltyOfCntg', type=ModalityOfCounting1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsHldr', type=PartyIdentification246Choice, min=0, max=250, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteRctDtTm', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prxy', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VotePerRsltn', type=Vote19, min=0, max=1000, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification231Choice, min=0, max=1, mutex_group=None, array=False),
	))

