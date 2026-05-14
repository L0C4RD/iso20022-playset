# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Event2 import Event2

class SystemEventNotificationV02(base_types._BaseFieldType):

	__slots__ = ["_EvtInf"]
	@property
	def EvtInf(self):
		return self._EvtInf

	@EvtInf.setter
	def EvtInf(self, value):
		self._EvtInf = value if type(value) != base_types.auto else self.make_default("EvtInf")

	@EvtInf.deleter
	def EvtInf(self):
		del self._EvtInf
		self._EvtInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EvtInf', type=Event2, min=1, max=1, mutex_group=None, array=False),
	))