from . import base_types
from .FixedAmountOrUnlimited1Choice import FixedAmountOrUnlimited1Choice
from .MaximumAmountByPeriod1 import MaximumAmountByPeriod1

class Authorisation2(base_types._BaseFieldType):

	__slots__ = ["_MaxAmtByPrd", "_MaxAmtByBlkSubmissn", "_MaxAmtByTx"]
	@property
	def MaxAmtByPrd(self):
		return self._MaxAmtByPrd

	@MaxAmtByPrd.setter
	def MaxAmtByPrd(self, value):
		self._MaxAmtByPrd = value if type(value) != base_types.auto else self.make_default("MaxAmtByPrd")

	@MaxAmtByPrd.deleter
	def MaxAmtByPrd(self):
		del self._MaxAmtByPrd
		self._MaxAmtByPrd = None

	@property
	def MaxAmtByBlkSubmissn(self):
		return self._MaxAmtByBlkSubmissn

	@MaxAmtByBlkSubmissn.setter
	def MaxAmtByBlkSubmissn(self, value):
		self._MaxAmtByBlkSubmissn = value if type(value) != base_types.auto else self.make_default("MaxAmtByBlkSubmissn")

	@MaxAmtByBlkSubmissn.deleter
	def MaxAmtByBlkSubmissn(self):
		del self._MaxAmtByBlkSubmissn
		self._MaxAmtByBlkSubmissn = None

	@property
	def MaxAmtByTx(self):
		return self._MaxAmtByTx

	@MaxAmtByTx.setter
	def MaxAmtByTx(self, value):
		self._MaxAmtByTx = value if type(value) != base_types.auto else self.make_default("MaxAmtByTx")

	@MaxAmtByTx.deleter
	def MaxAmtByTx(self):
		del self._MaxAmtByTx
		self._MaxAmtByTx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxAmtByPrd', type=MaximumAmountByPeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MaxAmtByBlkSubmissn', type=FixedAmountOrUnlimited1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxAmtByTx', type=FixedAmountOrUnlimited1Choice, min=0, max=1, mutex_group=None, array=False),
	))

