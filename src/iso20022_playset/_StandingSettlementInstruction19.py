from . import base_types
from .PartyIdentification157 import PartyIdentification157
from .SettlementParties105 import SettlementParties105
from .SettlementStandingInstructionDatabase5Choice import SettlementStandingInstructionDatabase5Choice
from .Counterparty16Choice import Counterparty16Choice

class StandingSettlementInstruction19(base_types._BaseFieldType):

	__slots__ = ["_Vndr", "_CtrPty", "_OthrRcvgSttlmPties", "_SttlmStgInstrDB", "_OthrDlvrgSttlmPties"]
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
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if type(value) != base_types.auto else self.make_default("CtrPty")

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = None

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
	def OthrDlvrgSttlmPties(self):
		return self._OthrDlvrgSttlmPties

	@OthrDlvrgSttlmPties.setter
	def OthrDlvrgSttlmPties(self, value):
		self._OthrDlvrgSttlmPties = value if type(value) != base_types.auto else self.make_default("OthrDlvrgSttlmPties")

	@OthrDlvrgSttlmPties.deleter
	def OthrDlvrgSttlmPties(self):
		del self._OthrDlvrgSttlmPties
		self._OthrDlvrgSttlmPties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Vndr', type=PartyIdentification157, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPty', type=Counterparty16Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRcvgSttlmPties', type=SettlementParties105, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmStgInstrDB', type=SettlementStandingInstructionDatabase5Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDlvrgSttlmPties', type=SettlementParties105, min=0, max=1, mutex_group=None, array=False),
	))

