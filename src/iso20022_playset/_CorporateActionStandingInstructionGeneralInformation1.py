# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventType2FormatChoice
from . import FinancialInstrumentDescription3
from . import IncludedAccount1
from . import Max35Text
from . import PartyIdentification2Choice
from . import StandingInstructionType1Code

class CorporateActionStandingInstructionGeneralInformation1(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_ClntStgInstrId", "_EvtTp", "_InstgPtyId", "_StgInstrTp", "_UndrlygScty"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', IncludedAccount1, True)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', IncludedAccount1, True)

	@property
	def ClntStgInstrId(self):
		return self._ClntStgInstrId

	@ClntStgInstrId.setter
	def ClntStgInstrId(self, value):
		self._ClntStgInstrId = value if value is not None else base_types.UninitialisedField(self, 'ClntStgInstrId', Max35Text, False)

	@ClntStgInstrId.deleter
	def ClntStgInstrId(self):
		del self._ClntStgInstrId
		self._ClntStgInstrId = base_types.UninitialisedField(self, 'ClntStgInstrId', Max35Text, False)

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType2FormatChoice, True)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType2FormatChoice, True)

	@property
	def InstgPtyId(self):
		return self._InstgPtyId

	@InstgPtyId.setter
	def InstgPtyId(self, value):
		self._InstgPtyId = value if value is not None else base_types.UninitialisedField(self, 'InstgPtyId', PartyIdentification2Choice, False)

	@InstgPtyId.deleter
	def InstgPtyId(self):
		del self._InstgPtyId
		self._InstgPtyId = base_types.UninitialisedField(self, 'InstgPtyId', PartyIdentification2Choice, False)

	@property
	def StgInstrTp(self):
		return self._StgInstrTp

	@StgInstrTp.setter
	def StgInstrTp(self, value):
		self._StgInstrTp = value if value is not None else base_types.UninitialisedField(self, 'StgInstrTp', StandingInstructionType1Code, False)

	@StgInstrTp.deleter
	def StgInstrTp(self):
		del self._StgInstrTp
		self._StgInstrTp = base_types.UninitialisedField(self, 'StgInstrTp', StandingInstructionType1Code, False)

	@property
	def UndrlygScty(self):
		return self._UndrlygScty

	@UndrlygScty.setter
	def UndrlygScty(self, value):
		self._UndrlygScty = value if value is not None else base_types.UninitialisedField(self, 'UndrlygScty', FinancialInstrumentDescription3, False)

	@UndrlygScty.deleter
	def UndrlygScty(self):
		del self._UndrlygScty
		self._UndrlygScty = base_types.UninitialisedField(self, 'UndrlygScty', FinancialInstrumentDescription3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=IncludedAccount1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClntStgInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType2FormatChoice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='InstgPtyId', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StgInstrTp', type=StandingInstructionType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygScty', type=FinancialInstrumentDescription3, min=0, max=1, mutex_group=None, array=False),
	))