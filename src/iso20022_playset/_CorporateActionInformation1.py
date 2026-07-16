# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventProcessingType1FormatChoice
from . import CorporateActionEventType2FormatChoice
from . import CorporateActionMandatoryVoluntary1FormatChoice
from . import FinancialInstrumentDescription3
from . import Max35Text
from . import PartyIdentification2Choice

class CorporateActionInformation1(base_types._BaseFieldType):

	__slots__ = ["_AgtId", "_CorpActnPrcgId", "_EvtPrcgTp", "_EvtTp", "_IssrCorpActnId", "_MndtryVlntryEvtTp", "_UndrlygScty"]
	@property
	def AgtId(self):
		return self._AgtId

	@AgtId.setter
	def AgtId(self, value):
		self._AgtId = value if value is not None else base_types.UninitialisedField(self, 'AgtId', PartyIdentification2Choice, False)

	@AgtId.deleter
	def AgtId(self):
		del self._AgtId
		self._AgtId = base_types.UninitialisedField(self, 'AgtId', PartyIdentification2Choice, False)

	@property
	def CorpActnPrcgId(self):
		return self._CorpActnPrcgId

	@CorpActnPrcgId.setter
	def CorpActnPrcgId(self, value):
		self._CorpActnPrcgId = value if value is not None else base_types.UninitialisedField(self, 'CorpActnPrcgId', Max35Text, False)

	@CorpActnPrcgId.deleter
	def CorpActnPrcgId(self):
		del self._CorpActnPrcgId
		self._CorpActnPrcgId = base_types.UninitialisedField(self, 'CorpActnPrcgId', Max35Text, False)

	@property
	def EvtPrcgTp(self):
		return self._EvtPrcgTp

	@EvtPrcgTp.setter
	def EvtPrcgTp(self, value):
		self._EvtPrcgTp = value if value is not None else base_types.UninitialisedField(self, 'EvtPrcgTp', CorporateActionEventProcessingType1FormatChoice, False)

	@EvtPrcgTp.deleter
	def EvtPrcgTp(self):
		del self._EvtPrcgTp
		self._EvtPrcgTp = base_types.UninitialisedField(self, 'EvtPrcgTp', CorporateActionEventProcessingType1FormatChoice, False)

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType2FormatChoice, False)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType2FormatChoice, False)

	@property
	def IssrCorpActnId(self):
		return self._IssrCorpActnId

	@IssrCorpActnId.setter
	def IssrCorpActnId(self, value):
		self._IssrCorpActnId = value if value is not None else base_types.UninitialisedField(self, 'IssrCorpActnId', Max35Text, False)

	@IssrCorpActnId.deleter
	def IssrCorpActnId(self):
		del self._IssrCorpActnId
		self._IssrCorpActnId = base_types.UninitialisedField(self, 'IssrCorpActnId', Max35Text, False)

	@property
	def MndtryVlntryEvtTp(self):
		return self._MndtryVlntryEvtTp

	@MndtryVlntryEvtTp.setter
	def MndtryVlntryEvtTp(self, value):
		self._MndtryVlntryEvtTp = value if value is not None else base_types.UninitialisedField(self, 'MndtryVlntryEvtTp', CorporateActionMandatoryVoluntary1FormatChoice, False)

	@MndtryVlntryEvtTp.deleter
	def MndtryVlntryEvtTp(self):
		del self._MndtryVlntryEvtTp
		self._MndtryVlntryEvtTp = base_types.UninitialisedField(self, 'MndtryVlntryEvtTp', CorporateActionMandatoryVoluntary1FormatChoice, False)

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
		base_types.FieldEntry(name='AgtId', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnPrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtPrcgTp', type=CorporateActionEventProcessingType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType2FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCorpActnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtryVlntryEvtTp', type=CorporateActionMandatoryVoluntary1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygScty', type=FinancialInstrumentDescription3, min=1, max=1, mutex_group=None, array=False),
	))