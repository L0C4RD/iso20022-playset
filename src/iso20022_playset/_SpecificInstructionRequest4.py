# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ParticipationMethod3Choice
from . import YesNoIndicator

class SpecificInstructionRequest4(base_types._BaseFieldType):

	__slots__ = ["_PrtcptnMtd", "_SctiesRegn"]
	@property
	def PrtcptnMtd(self):
		return self._PrtcptnMtd

	@PrtcptnMtd.setter
	def PrtcptnMtd(self, value):
		self._PrtcptnMtd = value if value is not None else base_types.UninitialisedField(self, 'PrtcptnMtd', ParticipationMethod3Choice, False)

	@PrtcptnMtd.deleter
	def PrtcptnMtd(self):
		del self._PrtcptnMtd
		self._PrtcptnMtd = base_types.UninitialisedField(self, 'PrtcptnMtd', ParticipationMethod3Choice, False)

	@property
	def SctiesRegn(self):
		return self._SctiesRegn

	@SctiesRegn.setter
	def SctiesRegn(self, value):
		self._SctiesRegn = value if value is not None else base_types.UninitialisedField(self, 'SctiesRegn', YesNoIndicator, False)

	@SctiesRegn.deleter
	def SctiesRegn(self):
		del self._SctiesRegn
		self._SctiesRegn = base_types.UninitialisedField(self, 'SctiesRegn', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtcptnMtd', type=ParticipationMethod3Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesRegn', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))