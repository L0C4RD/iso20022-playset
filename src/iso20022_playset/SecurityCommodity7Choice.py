import base_types
import Commodity42
import Security48

class SecurityCommodity7Choice(base_types._BaseFieldType):

	__slots__ = ["_Cmmdty", "_Scty"]
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
		base_types.FieldEntry(name='Cmmdty', type=Commodity42, min=0, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Scty', type=Security48, min=0, max=None, mutex_group=1, array=True),
	))

