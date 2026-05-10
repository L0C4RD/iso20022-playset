from . import base_types
from ._Price7 import Price7

class PriceType4Choice(base_types._BaseFieldType):

	__slots__ = ["_Mkt", "_Indctv"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='Mkt', type=Price7, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Indctv', type=Price7, min=0, max=1, mutex_group=1, array=False),
	))

