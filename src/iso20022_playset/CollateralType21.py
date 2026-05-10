import base_types
import Commodity43
import AmountHaircutMargin1
import Security52

class CollateralType21(base_types._BaseFieldType):

	__slots__ = ["_Csh", "_Scty", "_Cmmdty"]
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

	@property
	def Cmmdty(self):
		return self._Cmmdty

	@Cmmdty.setter
	def Cmmdty(self, value):
		self._Cmmdty = value if type(value) != auto else self.make_default("Cmmdty")

	@Cmmdty.deleter
	def Cmmdty(self):
		del self._Cmmdty
		self._Cmmdty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Csh', type=AmountHaircutMargin1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Scty', type=Security52, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cmmdty', type=Commodity43, min=0, max=None, mutex_group=None, array=True),
	))

