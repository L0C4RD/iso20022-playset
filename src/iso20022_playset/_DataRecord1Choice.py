from . import base_types
from .Max10MbText import Max10MbText
from .Max20MbBinary import Max20MbBinary

class DataRecord1Choice(base_types._BaseFieldType):

	__slots__ = ["_Txt", "_Binry"]
	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if type(value) != base_types.auto else self.make_default("Txt")

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = None

	@property
	def Binry(self):
		return self._Binry

	@Binry.setter
	def Binry(self, value):
		self._Binry = value if type(value) != base_types.auto else self.make_default("Binry")

	@Binry.deleter
	def Binry(self):
		del self._Binry
		self._Binry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Txt', type=Max10MbText, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Binry', type=Max20MbBinary, min=1, max=None, mutex_group=1, array=True),
	))

