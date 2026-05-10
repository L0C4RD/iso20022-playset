from . import base_types
from .LiquidityRequiredAndAvailable1 import LiquidityRequiredAndAvailable1
from .Max256Text import Max256Text
from .CoverTwoDefaulters1 import CoverTwoDefaulters1

class LiquidityStressTestResult1(base_types._BaseFieldType):

	__slots__ = ["_ScnroDfltrs", "_LqdtyReqrdAndAvlbl", "_Id"]
	@property
	def ScnroDfltrs(self):
		return self._ScnroDfltrs

	@ScnroDfltrs.setter
	def ScnroDfltrs(self, value):
		self._ScnroDfltrs = value if type(value) != base_types.auto else self.make_default("ScnroDfltrs")

	@ScnroDfltrs.deleter
	def ScnroDfltrs(self):
		del self._ScnroDfltrs
		self._ScnroDfltrs = None

	@property
	def LqdtyReqrdAndAvlbl(self):
		return self._LqdtyReqrdAndAvlbl

	@LqdtyReqrdAndAvlbl.setter
	def LqdtyReqrdAndAvlbl(self, value):
		self._LqdtyReqrdAndAvlbl = value if type(value) != base_types.auto else self.make_default("LqdtyReqrdAndAvlbl")

	@LqdtyReqrdAndAvlbl.deleter
	def LqdtyReqrdAndAvlbl(self):
		del self._LqdtyReqrdAndAvlbl
		self._LqdtyReqrdAndAvlbl = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ScnroDfltrs', type=CoverTwoDefaulters1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdtyReqrdAndAvlbl', type=LiquidityRequiredAndAvailable1, min=6, max=6, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
	))

