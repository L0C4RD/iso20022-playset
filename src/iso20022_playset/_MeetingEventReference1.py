# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MeetingEventReference1Choice
from . import ProcessingPosition3Code

class MeetingEventReference1(base_types._BaseFieldType):

	__slots__ = ["_EvtId", "_LkgTp"]
	@property
	def EvtId(self):
		return self._EvtId

	@EvtId.setter
	def EvtId(self, value):
		self._EvtId = value if value is not None else base_types.UninitialisedField(self, 'EvtId', MeetingEventReference1Choice, False)

	@EvtId.deleter
	def EvtId(self):
		del self._EvtId
		self._EvtId = base_types.UninitialisedField(self, 'EvtId', MeetingEventReference1Choice, False)

	@property
	def LkgTp(self):
		return self._LkgTp

	@LkgTp.setter
	def LkgTp(self, value):
		self._LkgTp = value if value is not None else base_types.UninitialisedField(self, 'LkgTp', ProcessingPosition3Code, False)

	@LkgTp.deleter
	def LkgTp(self):
		del self._LkgTp
		self._LkgTp = base_types.UninitialisedField(self, 'LkgTp', ProcessingPosition3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtId', type=MeetingEventReference1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LkgTp', type=ProcessingPosition3Code, min=0, max=1, mutex_group=None, array=False),
	))