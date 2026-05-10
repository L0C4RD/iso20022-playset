from . import base_types
from .OrderOriginatorEligibility1Code import OrderOriginatorEligibility1Code
from .Max350Text import Max350Text

class MiFIDClassification1(base_types._BaseFieldType):

	__slots__ = ["_Nrrtv", "_Clssfctn"]
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
	def Clssfctn(self):
		return self._Clssfctn

	@Clssfctn.setter
	def Clssfctn(self, value):
		self._Clssfctn = value if type(value) != base_types.auto else self.make_default("Clssfctn")

	@Clssfctn.deleter
	def Clssfctn(self):
		del self._Clssfctn
		self._Clssfctn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Nrrtv', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Clssfctn', type=OrderOriginatorEligibility1Code, min=1, max=1, mutex_group=None, array=False),
	))

