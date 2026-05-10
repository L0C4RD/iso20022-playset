import base_types
import Max35Text
import CorporateActionEventType106Choice
import FinancialInstrumentAttributes126
import CorporateActionEventProcessingType2Code
import CorporateActionMandatoryVoluntary3Choice
import DTCCSubEventType9Code

class CorporateActionGeneralInformation172(base_types._BaseFieldType):

	__slots__ = ["_EvtPrcgTp", "_AgtCorpActnEvtId", "_SubEvtTp", "_MndtryVlntryEvtTp", "_EvtTp", "_UndrlygScty", "_OffclCorpActnEvtId", "_CorpActnEvtId"]
	@property
	def EvtPrcgTp(self):
		return self._EvtPrcgTp

	@EvtPrcgTp.setter
	def EvtPrcgTp(self, value):
		self._EvtPrcgTp = value if type(value) != auto else self.make_default("EvtPrcgTp")

	@EvtPrcgTp.deleter
	def EvtPrcgTp(self):
		del self._EvtPrcgTp
		self._EvtPrcgTp = None

	@property
	def AgtCorpActnEvtId(self):
		return self._AgtCorpActnEvtId

	@AgtCorpActnEvtId.setter
	def AgtCorpActnEvtId(self, value):
		self._AgtCorpActnEvtId = value if type(value) != auto else self.make_default("AgtCorpActnEvtId")

	@AgtCorpActnEvtId.deleter
	def AgtCorpActnEvtId(self):
		del self._AgtCorpActnEvtId
		self._AgtCorpActnEvtId = None

	@property
	def SubEvtTp(self):
		return self._SubEvtTp

	@SubEvtTp.setter
	def SubEvtTp(self, value):
		self._SubEvtTp = value if type(value) != auto else self.make_default("SubEvtTp")

	@SubEvtTp.deleter
	def SubEvtTp(self):
		del self._SubEvtTp
		self._SubEvtTp = None

	@property
	def MndtryVlntryEvtTp(self):
		return self._MndtryVlntryEvtTp

	@MndtryVlntryEvtTp.setter
	def MndtryVlntryEvtTp(self, value):
		self._MndtryVlntryEvtTp = value if type(value) != auto else self.make_default("MndtryVlntryEvtTp")

	@MndtryVlntryEvtTp.deleter
	def MndtryVlntryEvtTp(self):
		del self._MndtryVlntryEvtTp
		self._MndtryVlntryEvtTp = None

	@property
	def EvtTp(self):
		return self._EvtTp

	@EvtTp.setter
	def EvtTp(self, value):
		self._EvtTp = value if type(value) != auto else self.make_default("EvtTp")

	@EvtTp.deleter
	def EvtTp(self):
		del self._EvtTp
		self._EvtTp = None

	@property
	def UndrlygScty(self):
		return self._UndrlygScty

	@UndrlygScty.setter
	def UndrlygScty(self, value):
		self._UndrlygScty = value if type(value) != auto else self.make_default("UndrlygScty")

	@UndrlygScty.deleter
	def UndrlygScty(self):
		del self._UndrlygScty
		self._UndrlygScty = None

	@property
	def OffclCorpActnEvtId(self):
		return self._OffclCorpActnEvtId

	@OffclCorpActnEvtId.setter
	def OffclCorpActnEvtId(self, value):
		self._OffclCorpActnEvtId = value if type(value) != auto else self.make_default("OffclCorpActnEvtId")

	@OffclCorpActnEvtId.deleter
	def OffclCorpActnEvtId(self):
		del self._OffclCorpActnEvtId
		self._OffclCorpActnEvtId = None

	@property
	def CorpActnEvtId(self):
		return self._CorpActnEvtId

	@CorpActnEvtId.setter
	def CorpActnEvtId(self, value):
		self._CorpActnEvtId = value if type(value) != auto else self.make_default("CorpActnEvtId")

	@CorpActnEvtId.deleter
	def CorpActnEvtId(self):
		del self._CorpActnEvtId
		self._CorpActnEvtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtPrcgTp', type=CorporateActionEventProcessingType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgtCorpActnEvtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubEvtTp', type=DTCCSubEventType9Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtryVlntryEvtTp', type=CorporateActionMandatoryVoluntary3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType106Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygScty', type=FinancialInstrumentAttributes126, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

