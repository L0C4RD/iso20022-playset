from . import base_types
from .RestrictedFINXMax16Text import RestrictedFINXMax16Text
from .CorporateActionNarrative4Choice import CorporateActionNarrative4Choice

class CorporateActionGeneralInformation102(base_types._BaseFieldType):

	__slots__ = ["_CorpActnEvtId", "_NrrtvTp", "_OffclCorpActnEvtId"]
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

	@property
	def NrrtvTp(self):
		return self._NrrtvTp

	@NrrtvTp.setter
	def NrrtvTp(self, value):
		self._NrrtvTp = value if type(value) != auto else self.make_default("NrrtvTp")

	@NrrtvTp.deleter
	def NrrtvTp(self):
		del self._NrrtvTp
		self._NrrtvTp = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnEvtId', type=RestrictedFINXMax16Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NrrtvTp', type=CorporateActionNarrative4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OffclCorpActnEvtId', type=RestrictedFINXMax16Text, min=0, max=1, mutex_group=None, array=False),
	))

