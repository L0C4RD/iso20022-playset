# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FutureOrOptionDetails3
from . import SecuritiesFinancing12

class TwoLegTransactionType4Choice(base_types._BaseFieldType):

	__slots__ = ["_FutrOrOptnDtls", "_SctiesFincgDtls"]
	@property
	def FutrOrOptnDtls(self):
		return self._FutrOrOptnDtls

	@FutrOrOptnDtls.setter
	def FutrOrOptnDtls(self, value):
		self._FutrOrOptnDtls = value if value is not None else base_types.UninitialisedField(self, 'FutrOrOptnDtls', FutureOrOptionDetails3, False)

	@FutrOrOptnDtls.deleter
	def FutrOrOptnDtls(self):
		del self._FutrOrOptnDtls
		self._FutrOrOptnDtls = base_types.UninitialisedField(self, 'FutrOrOptnDtls', FutureOrOptionDetails3, False)

	@property
	def SctiesFincgDtls(self):
		return self._SctiesFincgDtls

	@SctiesFincgDtls.setter
	def SctiesFincgDtls(self, value):
		self._SctiesFincgDtls = value if value is not None else base_types.UninitialisedField(self, 'SctiesFincgDtls', SecuritiesFinancing12, False)

	@SctiesFincgDtls.deleter
	def SctiesFincgDtls(self):
		del self._SctiesFincgDtls
		self._SctiesFincgDtls = base_types.UninitialisedField(self, 'SctiesFincgDtls', SecuritiesFinancing12, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='FutrOrOptnDtls', type=FutureOrOptionDetails3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SctiesFincgDtls', type=SecuritiesFinancing12, min=0, max=1, mutex_group=1, array=False),
	))