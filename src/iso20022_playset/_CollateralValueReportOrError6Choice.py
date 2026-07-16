# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralValuePosition3
from . import ErrorHandling5

class CollateralValueReportOrError6Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_CollVal"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if value is not None else base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, False)

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = base_types.UninitialisedField(self, 'BizErr', ErrorHandling5, False)

	@property
	def CollVal(self):
		return self._CollVal

	@CollVal.setter
	def CollVal(self, value):
		self._CollVal = value if value is not None else base_types.UninitialisedField(self, 'CollVal', CollateralValuePosition3, False)

	@CollVal.deleter
	def CollVal(self):
		del self._CollVal
		self._CollVal = base_types.UninitialisedField(self, 'CollVal', CollateralValuePosition3, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollVal', type=CollateralValuePosition3, min=0, max=1, mutex_group=1, array=False),
	))