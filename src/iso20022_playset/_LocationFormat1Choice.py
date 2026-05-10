from . import base_types
from ._PlaceType1Code import PlaceType1Code
from ._PostalAddress1 import PostalAddress1

class LocationFormat1Choice(base_types._BaseFieldType):

	__slots__ = ["_LctnCd", "_Adr"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if type(value) != base_types.auto else self.make_default("Adr")

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = None

	@property
	def LctnCd(self):
		return self._LctnCd

	@LctnCd.setter
	def LctnCd(self, value):
		self._LctnCd = value if type(value) != base_types.auto else self.make_default("LctnCd")

	@LctnCd.deleter
	def LctnCd(self):
		del self._LctnCd
		self._LctnCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=PostalAddress1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='LctnCd', type=PlaceType1Code, min=0, max=1, mutex_group=1, array=False),
	))

