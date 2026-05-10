from . import base_types
import ISODate

class SystemParty2(base_types._BaseFieldType):

	__slots__ = ["_OpngDt", "_ClsgDt"]
	@property
	def OpngDt(self):
		return self._OpngDt

	@OpngDt.setter
	def OpngDt(self, value):
		self._OpngDt = value if type(value) != auto else self.make_default("OpngDt")

	@OpngDt.deleter
	def OpngDt(self):
		del self._OpngDt
		self._OpngDt = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OpngDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

