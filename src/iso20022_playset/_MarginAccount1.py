from . import base_types
from ._PositionAccount1 import PositionAccount1
from ._PartyIdentification118Choice import PartyIdentification118Choice

class MarginAccount1(base_types._BaseFieldType):

	__slots__ = ["_PosAcct", "_Id"]
	@property
	def PosAcct(self):
		return self._PosAcct

	@PosAcct.setter
	def PosAcct(self, value):
		self._PosAcct = value if type(value) != base_types.auto else self.make_default("PosAcct")

	@PosAcct.deleter
	def PosAcct(self):
		del self._PosAcct
		self._PosAcct = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='PosAcct', type=PositionAccount1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=PartyIdentification118Choice, min=1, max=1, mutex_group=None, array=False),
	))

