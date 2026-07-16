# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventProcessingType2Code
from . import CorporateActionEventType106Choice
from . import CorporateActionMandatoryVoluntary3Choice
from . import DTCCSubEventType9Code
from . import FinancialInstrumentAttributes126
from . import Max35Text

class CorporateActionGeneralInformation172(base_types._BaseFieldType):

	__slots__ = ["_AgtCorpActnEvtId", "_CorpActnEvtId", "_EvtPrcgTp", "_EvtTp", "_MndtryVlntryEvtTp", "_OffclCorpActnEvtId", "_SubEvtTp", "_UndrlygScty"]
	@property
	def AgtCorpActnEvtId(self):
		return self._AgtCorpActnEvtId

	@AgtCorpActnEvtId.setter
	def AgtCorpActnEvtId(self, value):
		self._AgtCorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'AgtCorpActnEvtId', Max35Text, False)

	@AgtCorpActnEvtId.deleter
	def AgtCorpActnEvtId(self):
		del self._AgtCorpActnEvtId
		self._AgtCorpActnEvtId = base_types.UninitialisedField(self, 'AgtCorpActnEvtId', Max35Text, False)

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'CorpActnEvtId', Max35Text, False)

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = base_types.UninitialisedField(self, 'CorpActnEvtId', Max35Text, False)

	@property
	def EvtPrcgTp(self):
		return self._EvtPrcgTp

	@EvtPrcgTp.setter
	def EvtPrcgTp(self, value):
		self._EvtPrcgTp = value if value is not None else base_types.UninitialisedField(self, 'EvtPrcgTp', CorporateActionEventProcessingType2Code, False)

	@EvtPrcgTp.deleter
	def EvtPrcgTp(self):
		del self._EvtPrcgTp
		self._EvtPrcgTp = base_types.UninitialisedField(self, 'EvtPrcgTp', CorporateActionEventProcessingType2Code, False)

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType106Choice, False)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType106Choice, False)

	@property
	def MndtryVlntryEvtTp(self):
		return self._MndtryVlntryEvtTp

	@MndtryVlntryEvtTp.setter
	def MndtryVlntryEvtTp(self, value):
		self._MndtryVlntryEvtTp = value if value is not None else base_types.UninitialisedField(self, 'MndtryVlntryEvtTp', CorporateActionMandatoryVoluntary3Choice, False)

	@MndtryVlntryEvtTp.deleter
	def MndtryVlntryEvtTp(self):
		del self._MndtryVlntryEvtTp
		self._MndtryVlntryEvtTp = base_types.UninitialisedField(self, 'MndtryVlntryEvtTp', CorporateActionMandatoryVoluntary3Choice, False)

	@property
	def OffclCorpActnEvtId(self):
		return self._OffclCorpActnEvtId

	@OffclCorpActnEvtId.setter
	def OffclCorpActnEvtId(self, value):
		self._OffclCorpActnEvtId = value if value is not None else base_types.UninitialisedField(self, 'OffclCorpActnEvtId', Max35Text, False)

	@OffclCorpActnEvtId.deleter
	def OffclCorpActnEvtId(self):
		del self._OffclCorpActnEvtId
		self._OffclCorpActnEvtId = base_types.UninitialisedField(self, 'OffclCorpActnEvtId', Max35Text, False)

	@property
	def SubEvtTp(self):
		return self._SubEvtTp

	@SubEvtTp.setter
	def SubEvtTp(self, value):
		self._SubEvtTp = value if value is not None else base_types.UninitialisedField(self, 'SubEvtTp', DTCCSubEventType9Code, False)

	@SubEvtTp.deleter
	def SubEvtTp(self):
		del self._SubEvtTp
		self._SubEvtTp = base_types.UninitialisedField(self, 'SubEvtTp', DTCCSubEventType9Code, False)

	@property
	def UndrlygScty(self):
		return self._UndrlygScty

	@UndrlygScty.setter
	def UndrlygScty(self, value):
		self._UndrlygScty = value if value is not None else base_types.UninitialisedField(self, 'UndrlygScty', FinancialInstrumentAttributes126, True)

	@UndrlygScty.deleter
	def UndrlygScty(self):
		del self._UndrlygScty
		self._UndrlygScty = base_types.UninitialisedField(self, 'UndrlygScty', FinancialInstrumentAttributes126, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCorpActnEvtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtPrcgTp', type=CorporateActionEventProcessingType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType106Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtryVlntryEvtTp', type=CorporateActionMandatoryVoluntary3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubEvtTp', type=DTCCSubEventType9Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygScty', type=FinancialInstrumentAttributes126, min=1, max=None, mutex_group=None, array=True),
	))