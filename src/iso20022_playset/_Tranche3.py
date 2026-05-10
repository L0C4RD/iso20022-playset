from . import base_types
from .BaseOneRate import BaseOneRate

class Tranche3(base_types._BaseFieldType):

	__slots__ = ["_AttchmntPt", "_DtchmntPt"]
	@property
	def AttchmntPt(self):
		return self._AttchmntPt

	@AttchmntPt.setter
	def AttchmntPt(self, value):
		self._AttchmntPt = value if type(value) != base_types.auto else self.make_default("AttchmntPt")

	@AttchmntPt.deleter
	def AttchmntPt(self):
		del self._AttchmntPt
		self._AttchmntPt = None

	@property
	def DtchmntPt(self):
		return self._DtchmntPt

	@DtchmntPt.setter
	def DtchmntPt(self, value):
		self._DtchmntPt = value if type(value) != base_types.auto else self.make_default("DtchmntPt")

	@DtchmntPt.deleter
	def DtchmntPt(self):
		del self._DtchmntPt
		self._DtchmntPt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AttchmntPt', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtchmntPt', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))

