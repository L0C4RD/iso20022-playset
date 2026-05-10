from . import base_types
from .PartyIdentification43 import PartyIdentification43
from .ISODate import ISODate

class Presentation2(base_types._BaseFieldType):

	__slots__ = ["_BnfcryPresntnDt", "_Presntr"]
	@property
	def BnfcryPresntnDt(self):
		return self._BnfcryPresntnDt

	@BnfcryPresntnDt.setter
	def BnfcryPresntnDt(self, value):
		self._BnfcryPresntnDt = value if type(value) != base_types.auto else self.make_default("BnfcryPresntnDt")

	@BnfcryPresntnDt.deleter
	def BnfcryPresntnDt(self):
		del self._BnfcryPresntnDt
		self._BnfcryPresntnDt = None

	@property
	def Presntr(self):
		return self._Presntr

	@Presntr.setter
	def Presntr(self, value):
		self._Presntr = value if type(value) != base_types.auto else self.make_default("Presntr")

	@Presntr.deleter
	def Presntr(self):
		del self._Presntr
		self._Presntr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BnfcryPresntnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Presntr', type=PartyIdentification43, min=0, max=1, mutex_group=None, array=False),
	))

