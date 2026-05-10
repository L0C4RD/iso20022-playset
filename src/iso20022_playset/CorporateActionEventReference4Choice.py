import base_types
import RestrictedFINXMax16Text

class CorporateActionEventReference4Choice(base_types._BaseFieldType):

	__slots__ = ["_LkdCorpActnId", "_LkdOffclCorpActnEvtId"]
	@property
	def LkdCorpActnId(self):
		return self._LkdCorpActnId

	@LkdCorpActnId.setter
	def LkdCorpActnId(self, value):
		self._LkdCorpActnId = value if type(value) != auto else self.make_default("LkdCorpActnId")

	@LkdCorpActnId.deleter
	def LkdCorpActnId(self):
		del self._LkdCorpActnId
		self._LkdCorpActnId = None

	@property
	def LkdOffclCorpActnEvtId(self):
		return self._LkdOffclCorpActnEvtId

	@LkdOffclCorpActnEvtId.setter
	def LkdOffclCorpActnEvtId(self, value):
		self._LkdOffclCorpActnEvtId = value if type(value) != auto else self.make_default("LkdOffclCorpActnEvtId")

	@LkdOffclCorpActnEvtId.deleter
	def LkdOffclCorpActnEvtId(self):
		del self._LkdOffclCorpActnEvtId
		self._LkdOffclCorpActnEvtId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LkdCorpActnId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LkdOffclCorpActnEvtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=1, array=False),
	))

