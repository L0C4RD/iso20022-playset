from . import base_types
from ._CancellationReason37Choice import CancellationReason37Choice
from ._RestrictedFINMax16Text import RestrictedFINMax16Text

class CancellationReason27(base_types._BaseFieldType):

	__slots__ = ["_CorpActnEvtId", "_Cd"]
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
	def Cd(self):
		return self._Cd

	@Cd.setter
	def Cd(self, value):
		self._Cd = value if type(value) != base_types.auto else self.make_default("Cd")

	@Cd.deleter
	def Cd(self):
		del self._Cd
		self._Cd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CorpActnEvtId', type=RestrictedFINMax16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cd', type=CancellationReason37Choice, min=1, max=1, mutex_group=None, array=False),
	))

