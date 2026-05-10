from . import base_types
from .CorporateActionEventType112Choice import CorporateActionEventType112Choice
from .Max35Text import Max35Text

class CorporateActionGeneralInformation182(base_types._BaseFieldType):

	__slots__ = ["_OffclCorpActnEvtId", "_EvtTp", "_CorpActnEvtId", "_ClssActnNb"]
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
	def ClssActnNb(self):
		return self._ClssActnNb

	@ClssActnNb.setter
	def ClssActnNb(self, value):
		self._ClssActnNb = value if type(value) != base_types.auto else self.make_default("ClssActnNb")

	@ClssActnNb.deleter
	def ClssActnNb(self):
		del self._ClssActnNb
		self._ClssActnNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EvtTp', type=CorporateActionEventType112Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CorpActnEvtId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClssActnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

