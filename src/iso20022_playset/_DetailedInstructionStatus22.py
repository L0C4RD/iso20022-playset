# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime1Choice
from . import Max35Text
from . import ModalityOfCounting1Choice
from . import PartyIdentification231Choice
from . import PartyIdentification232Choice
from . import PartyIdentification246Choice
from . import Vote22
from . import YesNoIndicator

class DetailedInstructionStatus22(base_types._BaseFieldType):

	__slots__ = ["_AcctId", "_AcctOwnr", "_ModltyOfCntg", "_Prxy", "_RghtsHldr", "_SnglInstrId", "_StgInstr", "_SubAcctId", "_VotePerRsltn", "_VoteRctDtTm"]
	@property
	def AcctId(self):
		return self._AcctId

	@AcctId.setter
	def AcctId(self, value):
		self._AcctId = value if value is not None else base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@AcctId.deleter
	def AcctId(self):
		del self._AcctId
		self._AcctId = base_types.UninitialisedField(self, 'AcctId', Max35Text, False)

	@property
	def AcctOwnr(self):
		return self._AcctOwnr

	@AcctOwnr.setter
	def AcctOwnr(self, value):
		self._AcctOwnr = value if value is not None else base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification231Choice, False)

	@AcctOwnr.deleter
	def AcctOwnr(self):
		del self._AcctOwnr
		self._AcctOwnr = base_types.UninitialisedField(self, 'AcctOwnr', PartyIdentification231Choice, False)

	@property
	def ModltyOfCntg(self):
		return self._ModltyOfCntg

	@ModltyOfCntg.setter
	def ModltyOfCntg(self, value):
		self._ModltyOfCntg = value if value is not None else base_types.UninitialisedField(self, 'ModltyOfCntg', ModalityOfCounting1Choice, False)

	@ModltyOfCntg.deleter
	def ModltyOfCntg(self):
		del self._ModltyOfCntg
		self._ModltyOfCntg = base_types.UninitialisedField(self, 'ModltyOfCntg', ModalityOfCounting1Choice, False)

	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if value is not None else base_types.UninitialisedField(self, 'Prxy', PartyIdentification232Choice, False)

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = base_types.UninitialisedField(self, 'Prxy', PartyIdentification232Choice, False)

	@property
	def RghtsHldr(self):
		return self._RghtsHldr

	@RghtsHldr.setter
	def RghtsHldr(self, value):
		self._RghtsHldr = value if value is not None else base_types.UninitialisedField(self, 'RghtsHldr', PartyIdentification246Choice, True)

	@RghtsHldr.deleter
	def RghtsHldr(self):
		del self._RghtsHldr
		self._RghtsHldr = base_types.UninitialisedField(self, 'RghtsHldr', PartyIdentification246Choice, True)

	@property
	def SnglInstrId(self):
		return self._SnglInstrId

	@SnglInstrId.setter
	def SnglInstrId(self, value):
		self._SnglInstrId = value if value is not None else base_types.UninitialisedField(self, 'SnglInstrId', Max35Text, False)

	@SnglInstrId.deleter
	def SnglInstrId(self):
		del self._SnglInstrId
		self._SnglInstrId = base_types.UninitialisedField(self, 'SnglInstrId', Max35Text, False)

	@property
	def StgInstr(self):
		return self._StgInstr

	@StgInstr.setter
	def StgInstr(self, value):
		self._StgInstr = value if value is not None else base_types.UninitialisedField(self, 'StgInstr', YesNoIndicator, False)

	@StgInstr.deleter
	def StgInstr(self):
		del self._StgInstr
		self._StgInstr = base_types.UninitialisedField(self, 'StgInstr', YesNoIndicator, False)

	@property
	def SubAcctId(self):
		return self._SubAcctId

	@SubAcctId.setter
	def SubAcctId(self, value):
		self._SubAcctId = value if value is not None else base_types.UninitialisedField(self, 'SubAcctId', Max35Text, False)

	@SubAcctId.deleter
	def SubAcctId(self):
		del self._SubAcctId
		self._SubAcctId = base_types.UninitialisedField(self, 'SubAcctId', Max35Text, False)

	@property
	def VotePerRsltn(self):
		return self._VotePerRsltn

	@VotePerRsltn.setter
	def VotePerRsltn(self, value):
		self._VotePerRsltn = value if value is not None else base_types.UninitialisedField(self, 'VotePerRsltn', Vote22, True)

	@VotePerRsltn.deleter
	def VotePerRsltn(self):
		del self._VotePerRsltn
		self._VotePerRsltn = base_types.UninitialisedField(self, 'VotePerRsltn', Vote22, True)

	@property
	def VoteRctDtTm(self):
		return self._VoteRctDtTm

	@VoteRctDtTm.setter
	def VoteRctDtTm(self, value):
		self._VoteRctDtTm = value if value is not None else base_types.UninitialisedField(self, 'VoteRctDtTm', DateAndDateTime1Choice, False)

	@VoteRctDtTm.deleter
	def VoteRctDtTm(self):
		del self._VoteRctDtTm
		self._VoteRctDtTm = base_types.UninitialisedField(self, 'VoteRctDtTm', DateAndDateTime1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctOwnr', type=PartyIdentification231Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ModltyOfCntg', type=ModalityOfCounting1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prxy', type=PartyIdentification232Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RghtsHldr', type=PartyIdentification246Choice, min=0, max=250, mutex_group=None, array=True),
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstr', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubAcctId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VotePerRsltn', type=Vote22, min=0, max=1000, mutex_group=None, array=True),
		base_types.FieldEntry(name='VoteRctDtTm', type=DateAndDateTime1Choice, min=0, max=1, mutex_group=None, array=False),
	))