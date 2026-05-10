from . import base_types
from ._ISODateTime import ISODateTime
from ._Party50Choice import Party50Choice
from ._Max35Text import Max35Text

class ReportHeader7(base_types._BaseFieldType):

	__slots__ = ["_To", "_Id", "_Fr", "_CreDtTm"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if type(value) != base_types.auto else self.make_default("Fr")

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def To(self):
		return self._To

	@To.setter
	def To(self, value):
		self._To = value if type(value) != base_types.auto else self.make_default("To")

	@To.deleter
	def To(self):
		del self._To
		self._To = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fr', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='To', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
	))

