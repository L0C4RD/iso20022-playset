# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection53
from . import FundingSourceType1Code

class FundingSource3(base_types._BaseFieldType):

	__slots__ = ["_MktVal", "_Tp"]
	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if value is not None else base_types.UninitialisedField(self, 'MktVal', AmountAndDirection53, False)

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = base_types.UninitialisedField(self, 'MktVal', AmountAndDirection53, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', FundingSourceType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', FundingSourceType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection53, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FundingSourceType1Code, min=1, max=1, mutex_group=None, array=False),
	))