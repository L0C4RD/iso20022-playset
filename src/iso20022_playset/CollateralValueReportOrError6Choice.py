import base_types
import CollateralValuePosition3
import ErrorHandling5

class CollateralValueReportOrError6Choice(base_types._BaseFieldType):

	__slots__ = ["_BizErr", "_CollVal"]
	@property
	def BizErr(self):
		return self._BizErr

	@BizErr.setter
	def BizErr(self, value):
		self._BizErr = value if type(value) != auto else self.make_default("BizErr")

	@BizErr.deleter
	def BizErr(self):
		del self._BizErr
		self._BizErr = None

	@property
	def CollVal(self):
		return self._CollVal

	@CollVal.setter
	def CollVal(self, value):
		self._CollVal = value if type(value) != auto else self.make_default("CollVal")

	@CollVal.deleter
	def CollVal(self):
		del self._CollVal
		self._CollVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizErr', type=ErrorHandling5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CollVal', type=CollateralValuePosition3, min=0, max=1, mutex_group=1, array=False),
	))

