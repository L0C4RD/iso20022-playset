from . import base_types
from ._PartyUpdate1 import PartyUpdate1
from ._PartyCancellation1 import PartyCancellation1

class PartyReport1Choice(base_types._BaseFieldType):

	__slots__ = ["_Upd", "_Cxl"]
	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if type(value) != base_types.auto else self.make_default("Cxl")

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = None

	@property
	def Upd(self):
		return self._Upd

	@Upd.setter
	def Upd(self, value):
		self._Upd = value if type(value) != base_types.auto else self.make_default("Upd")

	@Upd.deleter
	def Upd(self):
		del self._Upd
		self._Upd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cxl', type=PartyCancellation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Upd', type=PartyUpdate1, min=0, max=1, mutex_group=1, array=False),
	))

