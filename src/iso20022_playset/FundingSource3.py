from . import base_types
import FundingSourceType1Code
import AmountAndDirection53

class FundingSource3(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_MktVal"]
	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=FundingSourceType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection53, min=1, max=1, mutex_group=None, array=False),
	))

