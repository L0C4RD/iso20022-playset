import base_types
import Max10Text
import MarketIdentification89

class Rating2(base_types._BaseFieldType):

	__slots__ = ["_Ratg", "_SrcOfRatg"]
	@property
	def Ratg(self):
		return self._Ratg

	@Ratg.setter
	def Ratg(self, value):
		self._Ratg = value if type(value) != auto else self.make_default("Ratg")

	@Ratg.deleter
	def Ratg(self):
		del self._Ratg
		self._Ratg = None

	@property
	def SrcOfRatg(self):
		return self._SrcOfRatg

	@SrcOfRatg.setter
	def SrcOfRatg(self, value):
		self._SrcOfRatg = value if type(value) != auto else self.make_default("SrcOfRatg")

	@SrcOfRatg.deleter
	def SrcOfRatg(self):
		del self._SrcOfRatg
		self._SrcOfRatg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Ratg', type=Max10Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SrcOfRatg', type=MarketIdentification89, min=1, max=1, mutex_group=None, array=False),
	))

