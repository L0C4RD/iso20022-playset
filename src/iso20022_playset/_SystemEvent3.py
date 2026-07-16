# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import SystemEventType4Choice

class SystemEvent3(base_types._BaseFieldType):

	__slots__ = ["_EndTm", "_FctvTm", "_SchdldTm", "_StartTm", "_Tp"]
	@property
	def EndTm(self):
		return self._EndTm

	@EndTm.setter
	def EndTm(self, value):
		self._EndTm = value if value is not None else base_types.UninitialisedField(self, 'EndTm', ISODateTime, False)

	@EndTm.deleter
	def EndTm(self):
		del self._EndTm
		self._EndTm = base_types.UninitialisedField(self, 'EndTm', ISODateTime, False)

	@property
	def FctvTm(self):
		return self._FctvTm

	@FctvTm.setter
	def FctvTm(self, value):
		self._FctvTm = value if value is not None else base_types.UninitialisedField(self, 'FctvTm', ISODateTime, False)

	@FctvTm.deleter
	def FctvTm(self):
		del self._FctvTm
		self._FctvTm = base_types.UninitialisedField(self, 'FctvTm', ISODateTime, False)

	@property
	def SchdldTm(self):
		return self._SchdldTm

	@SchdldTm.setter
	def SchdldTm(self, value):
		self._SchdldTm = value if value is not None else base_types.UninitialisedField(self, 'SchdldTm', ISODateTime, False)

	@SchdldTm.deleter
	def SchdldTm(self):
		del self._SchdldTm
		self._SchdldTm = base_types.UninitialisedField(self, 'SchdldTm', ISODateTime, False)

	@property
	def StartTm(self):
		return self._StartTm

	@StartTm.setter
	def StartTm(self, value):
		self._StartTm = value if value is not None else base_types.UninitialisedField(self, 'StartTm', ISODateTime, False)

	@StartTm.deleter
	def StartTm(self):
		del self._StartTm
		self._StartTm = base_types.UninitialisedField(self, 'StartTm', ISODateTime, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', SystemEventType4Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', SystemEventType4Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='EndTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchdldTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SystemEventType4Choice, min=1, max=1, mutex_group=None, array=False),
	))