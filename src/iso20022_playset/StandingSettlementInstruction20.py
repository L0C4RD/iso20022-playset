from . import base_types
from .Counterparty15Choice import Counterparty15Choice
from .PartyIdentification136 import PartyIdentification136
from .SettlementParties126 import SettlementParties126
from .SettlementStandingInstructionDatabase4Choice import SettlementStandingInstructionDatabase4Choice

class StandingSettlementInstruction20(base_types._BaseFieldType):

	__slots__ = ["_OthrDlvrgSttlmPties", "_OthrRcvgSttlmPties", "_Vndr", "_SttlmStgInstrDB", "_CtrPty"]
	@property
	def OthrDlvrgSttlmPties(self):
		return self._OthrDlvrgSttlmPties

	@OthrDlvrgSttlmPties.setter
	def OthrDlvrgSttlmPties(self, value):
		self._OthrDlvrgSttlmPties = value if type(value) != base_types.auto else self.make_default("OthrDlvrgSttlmPties")

	@OthrDlvrgSttlmPties.deleter
	def OthrDlvrgSttlmPties(self):
		del self._OthrDlvrgSttlmPties
		self._OthrDlvrgSttlmPties = None

	@property
	def OthrRcvgSttlmPties(self):
		return self._OthrRcvgSttlmPties

	@OthrRcvgSttlmPties.setter
	def OthrRcvgSttlmPties(self, value):
		self._OthrRcvgSttlmPties = value if type(value) != base_types.auto else self.make_default("OthrRcvgSttlmPties")

	@OthrRcvgSttlmPties.deleter
	def OthrRcvgSttlmPties(self):
		del self._OthrRcvgSttlmPties
		self._OthrRcvgSttlmPties = None

	@property
	def Vndr(self):
		return self._Vndr

	@Vndr.setter
	def Vndr(self, value):
		self._Vndr = value if type(value) != base_types.auto else self.make_default("Vndr")

	@Vndr.deleter
	def Vndr(self):
		del self._Vndr
		self._Vndr = None

	@property
	def SttlmStgInstrDB(self):
		return self._SttlmStgInstrDB

	@SttlmStgInstrDB.setter
	def SttlmStgInstrDB(self, value):
		self._SttlmStgInstrDB = value if type(value) != base_types.auto else self.make_default("SttlmStgInstrDB")

	@SttlmStgInstrDB.deleter
	def SttlmStgInstrDB(self):
		del self._SttlmStgInstrDB
		self._SttlmStgInstrDB = None

	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if type(value) != base_types.auto else self.make_default("CtrPty")

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrDlvrgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRcvgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vndr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmStgInstrDB', type=SettlementStandingInstructionDatabase4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty', type=Counterparty15Choice, min=1, max=1, mutex_group=None, array=False),
	))

