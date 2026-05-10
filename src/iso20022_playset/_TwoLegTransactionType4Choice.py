from . import base_types
from ._SecuritiesFinancing12 import SecuritiesFinancing12
from ._FutureOrOptionDetails3 import FutureOrOptionDetails3

class TwoLegTransactionType4Choice(base_types._BaseFieldType):

	__slots__ = ["_FutrOrOptnDtls", "_SctiesFincgDtls"]
	@property
	def FutrOrOptnDtls(self):
		return self._FutrOrOptnDtls

	@FutrOrOptnDtls.setter
	def FutrOrOptnDtls(self, value):
		self._FutrOrOptnDtls = value if type(value) != base_types.auto else self.make_default("FutrOrOptnDtls")

	@FutrOrOptnDtls.deleter
	def FutrOrOptnDtls(self):
		del self._FutrOrOptnDtls
		self._FutrOrOptnDtls = None

	@property
	def SctiesFincgDtls(self):
		return self._SctiesFincgDtls

	@SctiesFincgDtls.setter
	def SctiesFincgDtls(self, value):
		self._SctiesFincgDtls = value if type(value) != base_types.auto else self.make_default("SctiesFincgDtls")

	@SctiesFincgDtls.deleter
	def SctiesFincgDtls(self):
		del self._SctiesFincgDtls
		self._SctiesFincgDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FutrOrOptnDtls', type=FutureOrOptionDetails3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesFincgDtls', type=SecuritiesFinancing12, min=0, max=1, mutex_group=1, array=False),
	))

