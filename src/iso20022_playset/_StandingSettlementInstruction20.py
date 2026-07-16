# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Counterparty15Choice
from . import PartyIdentification136
from . import SettlementParties126
from . import SettlementStandingInstructionDatabase4Choice

class StandingSettlementInstruction20(base_types._BaseFieldType):

	__slots__ = ["_CtrPty", "_OthrDlvrgSttlmPties", "_OthrRcvgSttlmPties", "_SttlmStgInstrDB", "_Vndr"]
	@property
	def CtrPty(self):
		return self._CtrPty

	@CtrPty.setter
	def CtrPty(self, value):
		self._CtrPty = value if value is not None else base_types.UninitialisedField(self, 'CtrPty', Counterparty15Choice, False)

	@CtrPty.deleter
	def CtrPty(self):
		del self._CtrPty
		self._CtrPty = base_types.UninitialisedField(self, 'CtrPty', Counterparty15Choice, False)

	@property
	def OthrDlvrgSttlmPties(self):
		return self._OthrDlvrgSttlmPties

	@OthrDlvrgSttlmPties.setter
	def OthrDlvrgSttlmPties(self, value):
		self._OthrDlvrgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'OthrDlvrgSttlmPties', SettlementParties126, False)

	@OthrDlvrgSttlmPties.deleter
	def OthrDlvrgSttlmPties(self):
		del self._OthrDlvrgSttlmPties
		self._OthrDlvrgSttlmPties = base_types.UninitialisedField(self, 'OthrDlvrgSttlmPties', SettlementParties126, False)

	@property
	def OthrRcvgSttlmPties(self):
		return self._OthrRcvgSttlmPties

	@OthrRcvgSttlmPties.setter
	def OthrRcvgSttlmPties(self, value):
		self._OthrRcvgSttlmPties = value if value is not None else base_types.UninitialisedField(self, 'OthrRcvgSttlmPties', SettlementParties126, False)

	@OthrRcvgSttlmPties.deleter
	def OthrRcvgSttlmPties(self):
		del self._OthrRcvgSttlmPties
		self._OthrRcvgSttlmPties = base_types.UninitialisedField(self, 'OthrRcvgSttlmPties', SettlementParties126, False)

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
		self._Vndr = value if value is not None else base_types.UninitialisedField(self, 'Vndr', PartyIdentification136, False)

	@Vndr.deleter
	def Vndr(self):
		del self._Vndr
		self._Vndr = base_types.UninitialisedField(self, 'Vndr', PartyIdentification136, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrPty', type=Counterparty15Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrDlvrgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRcvgSttlmPties', type=SettlementParties126, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmStgInstrDB', type=SettlementStandingInstructionDatabase4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vndr', type=PartyIdentification136, min=0, max=1, mutex_group=None, array=False),
	))