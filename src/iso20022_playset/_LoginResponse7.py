from . import base_types
from ._PointOfInteractionComponent17 import PointOfInteractionComponent17
from ._ActionMessage11 import ActionMessage11
from ._PointOfInteractionCapabilities9 import PointOfInteractionCapabilities9
from ._ISODateTime import ISODateTime

class LoginResponse7(base_types._BaseFieldType):

	__slots__ = ["_POICpblties", "_OutptDisp", "_POIDtTm", "_POISftwr"]
	@property
	def POICpblties(self):
		return self._POICpblties

	@POICpblties.setter
	def POICpblties(self, value):
		self._POICpblties = value if type(value) != base_types.auto else self.make_default("POICpblties")

	@POICpblties.deleter
	def POICpblties(self):
		del self._POICpblties
		self._POICpblties = None

	@property
	def OutptDisp(self):
		return self._OutptDisp

	@OutptDisp.setter
	def OutptDisp(self, value):
		self._OutptDisp = value if type(value) != base_types.auto else self.make_default("OutptDisp")

	@OutptDisp.deleter
	def OutptDisp(self):
		del self._OutptDisp
		self._OutptDisp = None

	@property
	def POIDtTm(self):
		return self._POIDtTm

	@POIDtTm.setter
	def POIDtTm(self, value):
		self._POIDtTm = value if type(value) != base_types.auto else self.make_default("POIDtTm")

	@POIDtTm.deleter
	def POIDtTm(self):
		del self._POIDtTm
		self._POIDtTm = None

	@property
	def POISftwr(self):
		return self._POISftwr

	@POISftwr.setter
	def POISftwr(self, value):
		self._POISftwr = value if type(value) != base_types.auto else self.make_default("POISftwr")

	@POISftwr.deleter
	def POISftwr(self):
		del self._POISftwr
		self._POISftwr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POICpblties', type=PointOfInteractionCapabilities9, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutptDisp', type=ActionMessage11, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POIDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='POISftwr', type=PointOfInteractionComponent17, min=1, max=None, mutex_group=None, array=True),
	))

