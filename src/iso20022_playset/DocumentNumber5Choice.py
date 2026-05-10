from . import base_types
from .ISO20022MessageIdentificationText import ISO20022MessageIdentificationText
from .GenericIdentification36 import GenericIdentification36
from .Exact3NumericText import Exact3NumericText

class DocumentNumber5Choice(base_types._BaseFieldType):

	__slots__ = ["_LngNb", "_ShrtNb", "_PrtryNb"]
	@property
	def LngNb(self):
		return self._LngNb

	@LngNb.setter
	def LngNb(self, value):
		self._LngNb = value if type(value) != auto else self.make_default("LngNb")

	@LngNb.deleter
	def LngNb(self):
		del self._LngNb
		self._LngNb = None

	@property
	def ShrtNb(self):
		return self._ShrtNb

	@ShrtNb.setter
	def ShrtNb(self, value):
		self._ShrtNb = value if type(value) != auto else self.make_default("ShrtNb")

	@ShrtNb.deleter
	def ShrtNb(self):
		del self._ShrtNb
		self._ShrtNb = None

	@property
	def PrtryNb(self):
		return self._PrtryNb

	@PrtryNb.setter
	def PrtryNb(self, value):
		self._PrtryNb = value if type(value) != auto else self.make_default("PrtryNb")

	@PrtryNb.deleter
	def PrtryNb(self):
		del self._PrtryNb
		self._PrtryNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LngNb', type=ISO20022MessageIdentificationText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ShrtNb', type=Exact3NumericText, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryNb', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
	))

