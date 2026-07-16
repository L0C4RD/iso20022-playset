# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Event2

class SystemEventNotificationV02(base_types._BaseFieldType):

	__slots__ = ["_EvtInf"]
	@property
	def EvtInf(self):
		return self._EvtInf

	@EvtInf.setter
	def EvtInf(self, value):
		self._EvtInf = value if value is not None else base_types.UninitialisedField(self, 'EvtInf', Event2, False)

	@EvtInf.deleter
	def EvtInf(self):
		del self._EvtInf
		self._EvtInf = base_types.UninitialisedField(self, 'EvtInf', Event2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtInf', type=Event2, min=1, max=1, mutex_group=None, array=False),
	))