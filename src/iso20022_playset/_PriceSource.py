from . import base_types
from ._PriceSource1Code import PriceSource1Code
from ._Max35Text import Max35Text

class PriceSource(base_types._BaseFieldType):

	__slots__ = ["_PricSrc", "_Nrrtv"]
	@property
	def Nrrtv(self):
		return self._Nrrtv

	@Nrrtv.setter
	def Nrrtv(self, value):
		self._Nrrtv = value if type(value) != base_types.auto else self.make_default("Nrrtv")

	@Nrrtv.deleter
	def Nrrtv(self):
		del self._Nrrtv
		self._Nrrtv = None

	@property
	def PricSrc(self):
		return self._PricSrc

	@PricSrc.setter
	def PricSrc(self, value):
		self._PricSrc = value if type(value) != base_types.auto else self.make_default("PricSrc")

	@PricSrc.deleter
	def PricSrc(self):
		del self._PricSrc
		self._PricSrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nrrtv', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricSrc', type=PriceSource1Code, min=1, max=1, mutex_group=None, array=False),
	))

