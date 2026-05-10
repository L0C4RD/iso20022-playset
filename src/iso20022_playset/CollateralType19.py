from . import base_types
import SecurityReuseData1
import CashReuseData1

class CollateralType19(base_types._BaseFieldType):

	__slots__ = ["_Csh", "_Scty"]
	@property
	def Csh(self):
		return self._Csh

	@Csh.setter
	def Csh(self, value):
		self._Csh = value if type(value) != auto else self.make_default("Csh")

	@Csh.deleter
	def Csh(self):
		del self._Csh
		self._Csh = None

	@property
	def Scty(self):
		return self._Scty

	@Scty.setter
	def Scty(self, value):
		self._Scty = value if type(value) != auto else self.make_default("Scty")

	@Scty.deleter
	def Scty(self):
		del self._Scty
		self._Scty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Csh', type=CashReuseData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Scty', type=SecurityReuseData1, min=0, max=None, mutex_group=None, array=True),
	))

