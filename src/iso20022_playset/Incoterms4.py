from . import base_types
from .Incoterms4Choice import Incoterms4Choice
from .Max70Text import Max70Text

class Incoterms4(base_types._BaseFieldType):

	__slots__ = ["_IncotrmsCd", "_Lctn"]
	@property
	def IncotrmsCd(self):
		return self._IncotrmsCd

	@IncotrmsCd.setter
	def IncotrmsCd(self, value):
		self._IncotrmsCd = value if type(value) != auto else self.make_default("IncotrmsCd")

	@IncotrmsCd.deleter
	def IncotrmsCd(self):
		del self._IncotrmsCd
		self._IncotrmsCd = None

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if type(value) != auto else self.make_default("Lctn")

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IncotrmsCd', type=Incoterms4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

