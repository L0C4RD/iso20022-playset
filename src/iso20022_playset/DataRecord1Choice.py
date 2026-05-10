import base_types
import Max20MbBinary
import Max10MbText

class DataRecord1Choice(base_types._BaseFieldType):

	__slots__ = ["_Binry", "_Txt"]
	@property
	def Binry(self):
		return self._Binry

	@Binry.setter
	def Binry(self, value):
		self._Binry = value if type(value) != auto else self.make_default("Binry")

	@Binry.deleter
	def Binry(self):
		del self._Binry
		self._Binry = None

	@property
	def Txt(self):
		return self._Txt

	@Txt.setter
	def Txt(self, value):
		self._Txt = value if type(value) != auto else self.make_default("Txt")

	@Txt.deleter
	def Txt(self):
		del self._Txt
		self._Txt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Binry', type=Max20MbBinary, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Txt', type=Max10MbText, min=1, max=None, mutex_group=1, array=True),
	))

