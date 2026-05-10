from . import base_types
from .Commodity43 import Commodity43
from .Security51 import Security51

class SecurityCommodity9(base_types._BaseFieldType):

	__slots__ = ["_Scty", "_Cmmdty"]
	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if type(value) != base_types.auto else self.make_default("Scty")

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = None

	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if type(value) != base_types.auto else self.make_default("Cmmdty")

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Scty', type=Security51, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cmmdty', type=Commodity43, min=0, max=None, mutex_group=None, array=True),
	))

