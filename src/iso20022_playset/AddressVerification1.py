from . import base_types
from .Max5NumericText import Max5NumericText

class AddressVerification1(base_types._BaseFieldType):

	__slots__ = ["_AdrDgts", "_PstlCdDgts"]
	@property
	def AdrDgts(self):
		return self._AdrDgts

	@AdrDgts.setter
	def AdrDgts(self, value):
		self._AdrDgts = value if type(value) != auto else self.make_default("AdrDgts")

	@AdrDgts.deleter
	def AdrDgts(self):
		del self._AdrDgts
		self._AdrDgts = None

	@property
	def PstlCdDgts(self):
		return self._PstlCdDgts

	@PstlCdDgts.setter
	def PstlCdDgts(self, value):
		self._PstlCdDgts = value if type(value) != auto else self.make_default("PstlCdDgts")

	@PstlCdDgts.deleter
	def PstlCdDgts(self):
		del self._PstlCdDgts
		self._PstlCdDgts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdrDgts', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstlCdDgts', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
	))

