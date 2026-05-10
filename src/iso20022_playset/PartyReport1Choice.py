from . import base_types
from .PartyCancellation1 import PartyCancellation1
from .PartyUpdate1 import PartyUpdate1

class PartyReport1Choice(base_types._BaseFieldType):

	__slots__ = ["_Cxl", "_Upd"]
	@property
	def Cxl(self):
		return self._Cxl

	@Cxl.setter
	def Cxl(self, value):
		self._Cxl = value if type(value) != auto else self.make_default("Cxl")

	@Cxl.deleter
	def Cxl(self):
		del self._Cxl
		self._Cxl = None

	@property
	def Upd(self):
		return self._Upd

	@Upd.setter
	def Upd(self, value):
		self._Upd = value if type(value) != auto else self.make_default("Upd")

	@Upd.deleter
	def Upd(self):
		del self._Upd
		self._Upd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cxl', type=PartyCancellation1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Upd', type=PartyUpdate1, min=0, max=1, mutex_group=1, array=False),
	))

