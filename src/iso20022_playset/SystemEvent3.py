from . import base_types
import SystemEventType4Choice
import ISODateTime

class SystemEvent3(base_types._BaseFieldType):

	__slots__ = ["_FctvTm", "_StartTm", "_EndTm", "_SchdldTm", "_Tp"]
	@property
	def FctvTm(self):
		return self._FctvTm

	@FctvTm.setter
	def FctvTm(self, value):
		self._FctvTm = value if type(value) != auto else self.make_default("FctvTm")

	@FctvTm.deleter
	def FctvTm(self):
		del self._FctvTm
		self._FctvTm = None

	@property
	def StartTm(self):
		return self._StartTm

	@StartTm.setter
	def StartTm(self, value):
		self._StartTm = value if type(value) != auto else self.make_default("StartTm")

	@StartTm.deleter
	def StartTm(self):
		del self._StartTm
		self._StartTm = None

	@property
	def EndTm(self):
		return self._EndTm

	@EndTm.setter
	def EndTm(self, value):
		self._EndTm = value if type(value) != auto else self.make_default("EndTm")

	@EndTm.deleter
	def EndTm(self):
		del self._EndTm
		self._EndTm = None

	@property
	def SchdldTm(self):
		return self._SchdldTm

	@SchdldTm.setter
	def SchdldTm(self, value):
		self._SchdldTm = value if type(value) != auto else self.make_default("SchdldTm")

	@SchdldTm.deleter
	def SchdldTm(self):
		del self._SchdldTm
		self._SchdldTm = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FctvTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchdldTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=SystemEventType4Choice, min=1, max=1, mutex_group=None, array=False),
	))

