from . import base_types
from .Max25Text import Max25Text

class CommodityDerivative5(base_types._BaseFieldType):

	__slots__ = ["_Sz", "_AvrgTmChrtr"]
	@property
	def Sz(self):
		return self._Sz

	@Sz.setter
	def Sz(self, value):
		self._Sz = value if type(value) != base_types.auto else self.make_default("Sz")

	@Sz.deleter
	def Sz(self):
		del self._Sz
		self._Sz = None

	@property
	def AvrgTmChrtr(self):
		return self._AvrgTmChrtr

	@AvrgTmChrtr.setter
	def AvrgTmChrtr(self, value):
		self._AvrgTmChrtr = value if type(value) != base_types.auto else self.make_default("AvrgTmChrtr")

	@AvrgTmChrtr.deleter
	def AvrgTmChrtr(self):
		del self._AvrgTmChrtr
		self._AvrgTmChrtr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sz', type=Max25Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgTmChrtr', type=Max25Text, min=1, max=1, mutex_group=None, array=False),
	))

