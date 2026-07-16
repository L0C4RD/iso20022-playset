# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import PartyIdentification117Choice
from . import SettlementParties59
from . import SettlementStandingInstructionDatabase4Choice

class StandingSettlementInstruction13(base_types._BaseFieldType):

	__slots__ = ["_OthrDlvrgSttlmPties", "_OthrRcvgSttlmPties", "_SttlmStgInstrDB", "_Vndr"]
	@property
	def OthrDlvrgSttlmPties(self):
		return self._OthrDlvrgSttlmPties

	@OthrDlvrgSttlmPties.setter
	def OthrDlvrgSttlmPties(self, value):
		self._OthrDlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'OthrDlvrgSttlmPties', SettlementParties59, False)

	@OthrDlvrgSttlmPties.deleter
	def OthrDlvrgSttlmPties(self):
		del self._OthrDlvrgSttlmPties
		self._OthrDlvrgSttlmPties = base_types.UninitialisedField(self, 'OthrDlvrgSttlmPties', SettlementParties59, False)

	@property
	def OthrRcvgSttlmPties(self):
		return self._OthrRcvgSttlmPties

	@OthrRcvgSttlmPties.setter
	def OthrRcvgSttlmPties(self, value):
		self._OthrRcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'OthrRcvgSttlmPties', SettlementParties59, False)

	@OthrRcvgSttlmPties.deleter
	def OthrRcvgSttlmPties(self):
		del self._OthrRcvgSttlmPties
		self._OthrRcvgSttlmPties = base_types.UninitialisedField(self, 'OthrRcvgSttlmPties', SettlementParties59, False)

	@property
	def SttlmStgInstrDB(self):
		return self._SttlmStgInstrDB

	@SttlmStgInstrDB.setter
	def SttlmStgInstrDB(self, value):
		self._SttlmStgInstrDB = value if value is not None else base_types.UninitialisedField(self, 'SttlmStgInstrDB', SettlementStandingInstructionDatabase4Choice, False)

	@SttlmStgInstrDB.deleter
	def SttlmStgInstrDB(self):
		del self._SttlmStgInstrDB
		self._SttlmStgInstrDB = base_types.UninitialisedField(self, 'SttlmStgInstrDB', SettlementStandingInstructionDatabase4Choice, False)

	@property
	def Vndr(self):
		return self._Vndr

	@Vndr.setter
	def Vndr(self, value):
		self._Vndr = value if value is not None else base_types.UninitialisedField(self, 'Vndr', PartyIdentification117Choice, False)

	@Vndr.deleter
	def Vndr(self):
		del self._Vndr
		self._Vndr = base_types.UninitialisedField(self, 'Vndr', PartyIdentification117Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrDlvrgSttlmPties', type=SettlementParties59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRcvgSttlmPties', type=SettlementParties59, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmStgInstrDB', type=SettlementStandingInstructionDatabase4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vndr', type=PartyIdentification117Choice, min=0, max=1, mutex_group=None, array=False),
	))