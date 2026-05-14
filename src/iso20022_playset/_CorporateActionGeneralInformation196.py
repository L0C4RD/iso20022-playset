# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._CorporateActionEventProcessingType2Code import CorporateActionEventProcessingType2Code
from ._CorporateActionEventType127Choice import CorporateActionEventType127Choice
from ._CorporateActionMandatoryVoluntary3Choice import CorporateActionMandatoryVoluntary3Choice
from ._DTCCSubEventType9Code import DTCCSubEventType9Code
from ._FinancialInstrumentAttributes126 import FinancialInstrumentAttributes126
from ._Max35Text import Max35Text

class CorporateActionGeneralInformation196(base_types._BaseFieldType):

	__slots__ = ["_AgtCorpActnEvtId", "_CorpActnEvtId", "_EvtPrcgTp", "_EvtTp", "_MndtryVlntryEvtTp", "_OffclCorpActnEvtId", "_SubEvtTp", "_UndrlygScty"]
	@property
	def AgtCorpActnEvtId(self):
		return self._AgtCorpActnEvtId

	@AgtCorpActnEvtId.setter
	def AgtCorpActnEvtId(self, value):
		self._AgtCorpActnEvtId = value if type(value) != base_types.auto else self.make_default("AgtCorpActnEvtId")

	@AgtCorpActnEvtId.deleter
	def AgtCorpActnEvtId(self):
		del self._AgtCorpActnEvtId
		self._AgtCorpActnEvtId = None

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if type(value) != base_types.auto else self.make_default("CorpActnEvtId")

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = None

	@property
	def EvtPrcgTp(self):
		return self._EvtPrcgTp

	@EvtPrcgTp.setter
	def EvtPrcgTp(self, value):
		self._EvtPrcgTp = value if type(value) != base_types.auto else self.make_default("EvtPrcgTp")

	@EvtPrcgTp.deleter
	def EvtPrcgTp(self):
		del self._EvtPrcgTp
		self._EvtPrcgTp = None

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if type(value) != base_types.auto else self.make_default("EvtTp")

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = None

	@property
	def MndtryVlntryEvtTp(self):
		return self._MndtryVlntryEvtTp

	@MndtryVlntryEvtTp.setter
	def MndtryVlntryEvtTp(self, value):
		self._MndtryVlntryEvtTp = value if type(value) != base_types.auto else self.make_default("MndtryVlntryEvtTp")

	@MndtryVlntryEvtTp.deleter
	def MndtryVlntryEvtTp(self):
		del self._MndtryVlntryEvtTp
		self._MndtryVlntryEvtTp = None

	@property
	def OffclCorpActnEvtId(self):
		return self._OffclCorpActnEvtId

	@OffclCorpActnEvtId.setter
	def OffclCorpActnEvtId(self, value):
		self._OffclCorpActnEvtId = value if type(value) != base_types.auto else self.make_default("OffclCorpActnEvtId")

	@OffclCorpActnEvtId.deleter
	def OffclCorpActnEvtId(self):
		del self._OffclCorpActnEvtId
		self._OffclCorpActnEvtId = None

	@property
	def SubEvtTp(self):
		return self._SubEvtTp

	@SubEvtTp.setter
	def SubEvtTp(self, value):
		self._SubEvtTp = value if type(value) != base_types.auto else self.make_default("SubEvtTp")

	@SubEvtTp.deleter
	def SubEvtTp(self):
		del self._SubEvtTp
		self._SubEvtTp = None

	@property
	def UndrlygScty(self):
		return self._UndrlygScty

	@UndrlygScty.setter
	def UndrlygScty(self, value):
		self._UndrlygScty = value if type(value) != base_types.auto else self.make_default("UndrlygScty")

	@UndrlygScty.deleter
	def UndrlygScty(self):
		del self._UndrlygScty
		self._UndrlygScty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtCorpActnEvtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtPrcgTp', type=CorporateActionEventProcessingType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType127Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtryVlntryEvtTp', type=CorporateActionMandatoryVoluntary3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubEvtTp', type=DTCCSubEventType9Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygScty', type=FinancialInstrumentAttributes126, min=1, max=None, mutex_group=None, array=True),
	))