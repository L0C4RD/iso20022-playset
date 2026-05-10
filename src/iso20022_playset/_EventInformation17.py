from . import base_types
from ._CorporateActionMandatoryVoluntary3Choice import CorporateActionMandatoryVoluntary3Choice
from ._CorporateActionEventType112Choice import CorporateActionEventType112Choice
from ._NotificationIdentification5 import NotificationIdentification5
from ._Max35Text import Max35Text

class EventInformation17(base_types._BaseFieldType):

	__slots__ = ["_OffclCorpActnEvtId", "_EvtTp", "_MndtryVlntryEvtTp", "_CorpActnEvtId", "_LastNtfctnId"]
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
	def LastNtfctnId(self):
		return self._LastNtfctnId

	@LastNtfctnId.setter
	def LastNtfctnId(self, value):
		self._LastNtfctnId = value if type(value) != base_types.auto else self.make_default("LastNtfctnId")

	@LastNtfctnId.deleter
	def LastNtfctnId(self):
		del self._LastNtfctnId
		self._LastNtfctnId = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType112Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastNtfctnId', type=NotificationIdentification5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MndtryVlntryEvtTp', type=CorporateActionMandatoryVoluntary3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

