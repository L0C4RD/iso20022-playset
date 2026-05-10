from . import base_types
from ._ProxyAppointmentInformation6 import ProxyAppointmentInformation6
from ._ProxyNotAllowed1Code import ProxyNotAllowed1Code

class Proxy5Choice(base_types._BaseFieldType):

	__slots__ = ["_Prxy", "_PrxyNotAllwd"]
	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if type(value) != base_types.auto else self.make_default("Prxy")

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = None

	@property
	def PrxyNotAllwd(self):
		return self._PrxyNotAllwd

	@PrxyNotAllwd.setter
	def PrxyNotAllwd(self, value):
		self._PrxyNotAllwd = value if type(value) != base_types.auto else self.make_default("PrxyNotAllwd")

	@PrxyNotAllwd.deleter
	def PrxyNotAllwd(self):
		del self._PrxyNotAllwd
		self._PrxyNotAllwd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prxy', type=ProxyAppointmentInformation6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrxyNotAllwd', type=ProxyNotAllowed1Code, min=0, max=1, mutex_group=1, array=False),
	))

