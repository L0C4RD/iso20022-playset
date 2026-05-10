import base_types
import CorporateActionMandatoryVoluntary1FormatChoice
import Max35Text
import PartyIdentification2Choice
import CorporateActionEventProcessingType1FormatChoice
import FinancialInstrumentDescription3
import CorporateActionEventType2FormatChoice

class CorporateActionInformation2(base_types._BaseFieldType):

	__slots__ = ["_AgtId", "_IssrCorpActnId", "_EvtPrcgTp", "_MndtryVlntryEvtTp", "_UndrlygScty", "_OthrUndrlygScty", "_EvtTp", "_CorpActnPrcgId"]
	@property
	def AgtId(self):
		return self._AgtId

	@AgtId.setter
	def AgtId(self, value):
		self._AgtId = value if type(value) != auto else self.make_default("AgtId")

	@AgtId.deleter
	def AgtId(self):
		del self._AgtId
		self._AgtId = None

	@property
	def IssrCorpActnId(self):
		return self._IssrCorpActnId

	@IssrCorpActnId.setter
	def IssrCorpActnId(self, value):
		self._IssrCorpActnId = value if type(value) != auto else self.make_default("IssrCorpActnId")

	@IssrCorpActnId.deleter
	def IssrCorpActnId(self):
		del self._IssrCorpActnId
		self._IssrCorpActnId = None

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
	def OthrUndrlygScty(self):
		return self._OthrUndrlygScty

	@OthrUndrlygScty.setter
	def OthrUndrlygScty(self, value):
		self._OthrUndrlygScty = value if type(value) != auto else self.make_default("OthrUndrlygScty")

	@OthrUndrlygScty.deleter
	def OthrUndrlygScty(self):
		del self._OthrUndrlygScty
		self._OthrUndrlygScty = None

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
	def CorpActnPrcgId(self):
		return self._CorpActnPrcgId

	@CorpActnPrcgId.setter
	def CorpActnPrcgId(self, value):
		self._CorpActnPrcgId = value if type(value) != auto else self.make_default("CorpActnPrcgId")

	@CorpActnPrcgId.deleter
	def CorpActnPrcgId(self):
		del self._CorpActnPrcgId
		self._CorpActnPrcgId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgtId', type=PartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrCorpActnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtPrcgTp', type=CorporateActionEventProcessingType1FormatChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtryVlntryEvtTp', type=CorporateActionMandatoryVoluntary1FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygScty', type=FinancialInstrumentDescription3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrUndrlygScty', type=FinancialInstrumentDescription3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType2FormatChoice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnPrcgId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

