# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CorporateActionEventProcessingType2Choice
from . import CorporateActionEventType107Choice
from . import CorporateActionMandatoryVoluntary3Choice
from . import FinancialInstrumentAttributes128
from . import Max35Text

class CorporateActionGeneralInformation176(base_types._BaseFieldType):

	__slots__ = ["_ClssActnNb", "_CorpActnEvtId", "_EvtPrcgTp", "_EvtTp", "_MndtryVlntryEvtTp", "_OffclCorpActnEvtId", "_UndrlygScty"]
	@property
	def ClssActnNb(self):
		return self._ClssActnNb

	@ClssActnNb.setter
	def ClssActnNb(self, value):
		self._ClssActnNb = value if value is not None else base_types.UninitialisedField(self, 'ClssActnNb', Max35Text, False)

	@ClssActnNb.deleter
	def ClssActnNb(self):
		del self._ClssActnNb
		self._ClssActnNb = base_types.UninitialisedField(self, 'ClssActnNb', Max35Text, False)

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
		self._EvtPrcgTp = value if value is not None else base_types.UninitialisedField(self, 'EvtPrcgTp', CorporateActionEventProcessingType2Choice, False)

	@EvtPrcgTp.deleter
	def EvtPrcgTp(self):
		del self._EvtPrcgTp
		self._EvtPrcgTp = base_types.UninitialisedField(self, 'EvtPrcgTp', CorporateActionEventProcessingType2Choice, False)

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if value is not None else base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType107Choice, False)

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = base_types.UninitialisedField(self, 'EvtTp', CorporateActionEventType107Choice, False)

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
	def UndrlygScty(self):
		return self._UndrlygScty

	@UndrlygScty.setter
	def UndrlygScty(self, value):
		self._UndrlygScty = value if value is not None else base_types.UninitialisedField(self, 'UndrlygScty', FinancialInstrumentAttributes128, False)

	@UndrlygScty.deleter
	def UndrlygScty(self):
		del self._UndrlygScty
		self._UndrlygScty = base_types.UninitialisedField(self, 'UndrlygScty', FinancialInstrumentAttributes128, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssActnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtPrcgTp', type=CorporateActionEventProcessingType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType107Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtryVlntryEvtTp', type=CorporateActionMandatoryVoluntary3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygScty', type=FinancialInstrumentAttributes128, min=1, max=1, mutex_group=None, array=False),
	))