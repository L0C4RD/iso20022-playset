from . import base_types
from ._ParticipationMethod3Choice import ParticipationMethod3Choice
from ._YesNoIndicator import YesNoIndicator

class SpecificInstructionRequest4(base_types._BaseFieldType):

	__slots__ = ["_SctiesRegn", "_PrtcptnMtd"]
	@property
	def PrtcptnMtd(self):
		return self._PrtcptnMtd

	@PrtcptnMtd.setter
	def PrtcptnMtd(self, value):
		self._PrtcptnMtd = value if type(value) != base_types.auto else self.make_default("PrtcptnMtd")

	@PrtcptnMtd.deleter
	def PrtcptnMtd(self):
		del self._PrtcptnMtd
		self._PrtcptnMtd = None

	@property
	def SctiesRegn(self):
		return self._SctiesRegn

	@SctiesRegn.setter
	def SctiesRegn(self, value):
		self._SctiesRegn = value if type(value) != base_types.auto else self.make_default("SctiesRegn")

	@SctiesRegn.deleter
	def SctiesRegn(self):
		del self._SctiesRegn
		self._SctiesRegn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtcptnMtd', type=ParticipationMethod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesRegn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

