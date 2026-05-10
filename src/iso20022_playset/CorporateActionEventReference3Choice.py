from . import base_types
from .Max35Text import Max35Text

class CorporateActionEventReference3Choice(base_types._BaseFieldType):

	__slots__ = ["_LkdOffclCorpActnEvtId", "_LkdCorpActnId"]
	@property
	def LkdOffclCorpActnEvtId(self):
		return self._LkdOffclCorpActnEvtId

	@LkdOffclCorpActnEvtId.setter
	def LkdOffclCorpActnEvtId(self, value):
		self._LkdOffclCorpActnEvtId = value if type(value) != base_types.auto else self.make_default("LkdOffclCorpActnEvtId")

	@LkdOffclCorpActnEvtId.deleter
	def LkdOffclCorpActnEvtId(self):
		del self._LkdOffclCorpActnEvtId
		self._LkdOffclCorpActnEvtId = None

	@property
	def LkdCorpActnId(self):
		return self._LkdCorpActnId

	@LkdCorpActnId.setter
	def LkdCorpActnId(self, value):
		self._LkdCorpActnId = value if type(value) != base_types.auto else self.make_default("LkdCorpActnId")

	@LkdCorpActnId.deleter
	def LkdCorpActnId(self):
		del self._LkdCorpActnId
		self._LkdCorpActnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkdOffclCorpActnEvtId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LkdCorpActnId', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

