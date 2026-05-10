from . import base_types
from .Security48 import Security48
from .CashCompare3 import CashCompare3
from .Commodity42 import Commodity42

class SecurityCommodityCash4(base_types._BaseFieldType):

	__slots__ = ["_Scty", "_Cmmdty", "_Csh"]
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

	@property
	def Csh(self):
		return self._Csh

	@Csh.setter
	def Csh(self, value):
		self._Csh = value if type(value) != base_types.auto else self.make_default("Csh")

	@Csh.deleter
	def Csh(self):
		del self._Csh
		self._Csh = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Scty', type=Security48, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cmmdty', type=Commodity42, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Csh', type=CashCompare3, min=0, max=None, mutex_group=None, array=True),
	))

