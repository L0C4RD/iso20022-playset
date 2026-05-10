from . import base_types
from .Max35Text import Max35Text
from .Max140Text import Max140Text
from .ISODate import ISODate

class LegalOrganisation2(base_types._BaseFieldType):

	__slots__ = ["_Id", "_RegnDt", "_EstblishmtDt", "_Nm"]
	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def RegnDt(self):
		return self._RegnDt

	@RegnDt.setter
	def RegnDt(self, value):
		self._RegnDt = value if type(value) != auto else self.make_default("RegnDt")

	@RegnDt.deleter
	def RegnDt(self):
		del self._RegnDt
		self._RegnDt = None

	@property
	def EstblishmtDt(self):
		return self._EstblishmtDt

	@EstblishmtDt.setter
	def EstblishmtDt(self, value):
		self._EstblishmtDt = value if type(value) != auto else self.make_default("EstblishmtDt")

	@EstblishmtDt.deleter
	def EstblishmtDt(self):
		del self._EstblishmtDt
		self._EstblishmtDt = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Id', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EstblishmtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

