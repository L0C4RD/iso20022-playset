from . import base_types
from ._Max16Text import Max16Text
from ._Number import Number

class UTMCoordinates1(base_types._BaseFieldType):

	__slots__ = ["_UTMZone", "_UTMNrthwrd", "_UTMEstwrd"]
	@property
	def UTMEstwrd(self):
		return self._UTMEstwrd

	@UTMEstwrd.setter
	def UTMEstwrd(self, value):
		self._UTMEstwrd = value if type(value) != base_types.auto else self.make_default("UTMEstwrd")

	@UTMEstwrd.deleter
	def UTMEstwrd(self):
		del self._UTMEstwrd
		self._UTMEstwrd = None

	@property
	def UTMNrthwrd(self):
		return self._UTMNrthwrd

	@UTMNrthwrd.setter
	def UTMNrthwrd(self, value):
		self._UTMNrthwrd = value if type(value) != base_types.auto else self.make_default("UTMNrthwrd")

	@UTMNrthwrd.deleter
	def UTMNrthwrd(self):
		del self._UTMNrthwrd
		self._UTMNrthwrd = None

	@property
	def UTMZone(self):
		return self._UTMZone

	@UTMZone.setter
	def UTMZone(self, value):
		self._UTMZone = value if type(value) != base_types.auto else self.make_default("UTMZone")

	@UTMZone.deleter
	def UTMZone(self):
		del self._UTMZone
		self._UTMZone = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UTMEstwrd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UTMNrthwrd', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UTMZone', type=Max16Text, min=1, max=1, mutex_group=None, array=False),
	))

