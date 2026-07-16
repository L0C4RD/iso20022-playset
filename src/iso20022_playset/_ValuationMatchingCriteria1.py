# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareAmountAndDirection3
from . import CompareValuationType1

class ValuationMatchingCriteria1(base_types._BaseFieldType):

	__slots__ = ["_CtrctVal", "_Tp"]
	@property
	def CtrctVal(self):
		return self._CtrctVal

	@CtrctVal.setter
	def CtrctVal(self, value):
		self._CtrctVal = value if value is not None else base_types.UninitialisedField(self, 'CtrctVal', CompareAmountAndDirection3, False)

	@CtrctVal.deleter
	def CtrctVal(self):
		del self._CtrctVal
		self._CtrctVal = base_types.UninitialisedField(self, 'CtrctVal', CompareAmountAndDirection3, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CompareValuationType1, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CompareValuationType1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctVal', type=CompareAmountAndDirection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CompareValuationType1, min=0, max=1, mutex_group=None, array=False),
	))