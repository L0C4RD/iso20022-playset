# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EventType1Choice
from . import ISOTime

class ExecutionType1Choice(base_types._BaseFieldType):

	__slots__ = ["_Evt", "_Tm"]
	@property
	def Evt(self):
		return self._Evt

	@Evt.setter
	def Evt(self, value):
		self._Evt = value if value is not None else base_types.UninitialisedField(self, 'Evt', EventType1Choice, False)

	@Evt.deleter
	def Evt(self):
		del self._Evt
		self._Evt = base_types.UninitialisedField(self, 'Evt', EventType1Choice, False)

	@property
	def Tm(self):
		return self._Tm

	@Tm.setter
	def Tm(self, value):
		self._Tm = value if value is not None else base_types.UninitialisedField(self, 'Tm', ISOTime, False)

	@Tm.deleter
	def Tm(self):
		del self._Tm
		self._Tm = base_types.UninitialisedField(self, 'Tm', ISOTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Evt', type=EventType1Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tm', type=ISOTime, min=0, max=1, mutex_group=1, array=False),
	))