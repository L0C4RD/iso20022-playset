from . import base_types
from ._PartyIdentification117Choice import PartyIdentification117Choice
from ._SettlementStandingInstructionDatabase4Choice import SettlementStandingInstructionDatabase4Choice
from ._SettlementParties59 import SettlementParties59

class StandingSettlementInstruction13(base_types._BaseFieldType):

	__slots__ = ["_OthrDlvrgSttlmPties", "_OthrRcvgSttlmPties", "_Vndr", "_SttlmStgInstrDB"]
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
	def Vndr(self):
		return self._Vndr

	@Vndr.setter
	def Vndr(self, value):
		self._Vndr = value if type(value) != base_types.auto else self.make_default("Vndr")

	@Vndr.deleter
	def Vndr(self):
		del self._Vndr
		self._Vndr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrDlvrgSttlmPties', type=SettlementParties59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRcvgSttlmPties', type=SettlementParties59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmStgInstrDB', type=SettlementStandingInstructionDatabase4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vndr', type=PartyIdentification117Choice, min=0, max=1, mutex_group=None, array=False),
	))

