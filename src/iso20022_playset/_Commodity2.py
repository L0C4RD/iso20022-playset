# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAnd24Amount import ActiveCurrencyAnd24Amount
from ._AssetClassDetailedSubProductType1Choice import AssetClassDetailedSubProductType1Choice

class Commodity2(base_types._BaseFieldType):

	__slots__ = ["_CmmdtyTp", "_MktVal"]
	@property
	def CmmdtyTp(self):
		return self._CmmdtyTp

	@CmmdtyTp.setter
	def CmmdtyTp(self, value):
		self._CmmdtyTp = value if type(value) != base_types.auto else self.make_default("CmmdtyTp")

	@CmmdtyTp.deleter
	def CmmdtyTp(self):
		del self._CmmdtyTp
		self._CmmdtyTp = None

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != base_types.auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CmmdtyTp', type=AssetClassDetailedSubProductType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=ActiveCurrencyAnd24Amount, min=1, max=1, mutex_group=None, array=False),
	))