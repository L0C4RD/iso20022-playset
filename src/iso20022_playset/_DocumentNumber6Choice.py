from . import base_types
from ._ISO20022MessageIdentificationText import ISO20022MessageIdentificationText
from ._Exact3NumericText import Exact3NumericText
from ._GenericIdentification86 import GenericIdentification86

class DocumentNumber6Choice(base_types._BaseFieldType):

	__slots__ = ["_PrtryNb", "_ShrtNb", "_LngNb"]
	@property
	def LngNb(self):
		return self._LngNb

	@LngNb.setter
	def LngNb(self, value):
		self._LngNb = value if type(value) != base_types.auto else self.make_default("LngNb")

	@LngNb.deleter
	def LngNb(self):
		del self._LngNb
		self._LngNb = None

	@property
	def PrtryNb(self):
		return self._PrtryNb

	@PrtryNb.setter
	def PrtryNb(self, value):
		self._PrtryNb = value if type(value) != base_types.auto else self.make_default("PrtryNb")

	@PrtryNb.deleter
	def PrtryNb(self):
		del self._PrtryNb
		self._PrtryNb = None

	@property
	def ShrtNb(self):
		return self._ShrtNb

	@ShrtNb.setter
	def ShrtNb(self, value):
		self._ShrtNb = value if type(value) != base_types.auto else self.make_default("ShrtNb")

	@ShrtNb.deleter
	def ShrtNb(self):
		del self._ShrtNb
		self._ShrtNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LngNb', type=ISO20022MessageIdentificationText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryNb', type=GenericIdentification86, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ShrtNb', type=Exact3NumericText, min=0, max=1, mutex_group=1, array=False),
	))

