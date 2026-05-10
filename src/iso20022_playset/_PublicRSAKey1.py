from . import base_types
from ._Max5000Binary import Max5000Binary

class PublicRSAKey1(base_types._BaseFieldType):

	__slots__ = ["_Expnt", "_Mdlus"]
	@property
	def Expnt(self):
		return self._Expnt

	@Expnt.setter
	def Expnt(self, value):
		self._Expnt = value if type(value) != base_types.auto else self.make_default("Expnt")

	@Expnt.deleter
	def Expnt(self):
		del self._Expnt
		self._Expnt = None

	@property
	def Mdlus(self):
		return self._Mdlus

	@Mdlus.setter
	def Mdlus(self, value):
		self._Mdlus = value if type(value) != base_types.auto else self.make_default("Mdlus")

	@Mdlus.deleter
	def Mdlus(self):
		del self._Mdlus
		self._Mdlus = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Expnt', type=Max5000Binary, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mdlus', type=Max5000Binary, min=1, max=1, mutex_group=None, array=False),
	))

