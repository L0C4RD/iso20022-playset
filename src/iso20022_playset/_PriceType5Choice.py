from . import base_types
from ._Price3 import Price3

class PriceType5Choice(base_types._BaseFieldType):

	__slots__ = ["_Indctv", "_Mkt"]
	@property
	def Indctv(self):
		return self._Indctv

	@Indctv.setter
	def Indctv(self, value):
		self._Indctv = value if type(value) != base_types.auto else self.make_default("Indctv")

	@Indctv.deleter
	def Indctv(self):
		del self._Indctv
		self._Indctv = None

	@property
	def Mkt(self):
		return self._Mkt

	@Mkt.setter
	def Mkt(self, value):
		self._Mkt = value if type(value) != base_types.auto else self.make_default("Mkt")

	@Mkt.deleter
	def Mkt(self):
		del self._Mkt
		self._Mkt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Indctv', type=Price3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Mkt', type=Price3, min=0, max=1, mutex_group=1, array=False),
	))

