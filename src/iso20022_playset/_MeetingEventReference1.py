from . import base_types
from ._ProcessingPosition3Code import ProcessingPosition3Code
from ._MeetingEventReference1Choice import MeetingEventReference1Choice

class MeetingEventReference1(base_types._BaseFieldType):

	__slots__ = ["_EvtId", "_LkgTp"]
	@property
	def EvtId(self):
		return self._EvtId

	@EvtId.setter
	def EvtId(self, value):
		self._EvtId = value if type(value) != base_types.auto else self.make_default("EvtId")

	@EvtId.deleter
	def EvtId(self):
		del self._EvtId
		self._EvtId = None

	@property
	def LkgTp(self):
		return self._LkgTp

	@LkgTp.setter
	def LkgTp(self, value):
		self._LkgTp = value if type(value) != base_types.auto else self.make_default("LkgTp")

	@LkgTp.deleter
	def LkgTp(self):
		del self._LkgTp
		self._LkgTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtId', type=MeetingEventReference1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkgTp', type=ProcessingPosition3Code, min=0, max=1, mutex_group=None, array=False),
	))

