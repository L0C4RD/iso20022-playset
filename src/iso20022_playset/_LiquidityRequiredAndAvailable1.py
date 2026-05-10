from . import base_types
from ._LiquidResources1 import LiquidResources1
from ._SettlementDate6Code import SettlementDate6Code
from ._StressLiquidResourceRequirement1 import StressLiquidResourceRequirement1

class LiquidityRequiredAndAvailable1(base_types._BaseFieldType):

	__slots__ = ["_LqdRsrcs", "_LqdtyHrzn", "_StrssLqdRsrcRqrmnt"]
	@property
	def LqdRsrcs(self):
		return self._LqdRsrcs

	@LqdRsrcs.setter
	def LqdRsrcs(self, value):
		self._LqdRsrcs = value if type(value) != base_types.auto else self.make_default("LqdRsrcs")

	@LqdRsrcs.deleter
	def LqdRsrcs(self):
		del self._LqdRsrcs
		self._LqdRsrcs = None

	@property
	def LqdtyHrzn(self):
		return self._LqdtyHrzn

	@LqdtyHrzn.setter
	def LqdtyHrzn(self, value):
		self._LqdtyHrzn = value if type(value) != base_types.auto else self.make_default("LqdtyHrzn")

	@LqdtyHrzn.deleter
	def LqdtyHrzn(self):
		del self._LqdtyHrzn
		self._LqdtyHrzn = None

	@property
	def StrssLqdRsrcRqrmnt(self):
		return self._StrssLqdRsrcRqrmnt

	@StrssLqdRsrcRqrmnt.setter
	def StrssLqdRsrcRqrmnt(self, value):
		self._StrssLqdRsrcRqrmnt = value if type(value) != base_types.auto else self.make_default("StrssLqdRsrcRqrmnt")

	@StrssLqdRsrcRqrmnt.deleter
	def StrssLqdRsrcRqrmnt(self):
		del self._StrssLqdRsrcRqrmnt
		self._StrssLqdRsrcRqrmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LqdRsrcs', type=LiquidResources1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdtyHrzn', type=SettlementDate6Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StrssLqdRsrcRqrmnt', type=StressLiquidResourceRequirement1, min=1, max=1, mutex_group=None, array=False),
	))

