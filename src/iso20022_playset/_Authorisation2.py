# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FixedAmountOrUnlimited1Choice
from . import MaximumAmountByPeriod1

class Authorisation2(base_types._BaseFieldType):

	__slots__ = ["_MaxAmtByBlkSubmissn", "_MaxAmtByPrd", "_MaxAmtByTx"]
	@property
	def MaxAmtByBlkSubmissn(self):
		return self._MaxAmtByBlkSubmissn

	@MaxAmtByBlkSubmissn.setter
	def MaxAmtByBlkSubmissn(self, value):
		self._MaxAmtByBlkSubmissn = value if value is not None else base_types.UninitialisedField(self, 'MaxAmtByBlkSubmissn', FixedAmountOrUnlimited1Choice, False)

	@MaxAmtByBlkSubmissn.deleter
	def MaxAmtByBlkSubmissn(self):
		del self._MaxAmtByBlkSubmissn
		self._MaxAmtByBlkSubmissn = base_types.UninitialisedField(self, 'MaxAmtByBlkSubmissn', FixedAmountOrUnlimited1Choice, False)

	@property
	def MaxAmtByPrd(self):
		return self._MaxAmtByPrd

	@MaxAmtByPrd.setter
	def MaxAmtByPrd(self, value):
		self._MaxAmtByPrd = value if value is not None else base_types.UninitialisedField(self, 'MaxAmtByPrd', MaximumAmountByPeriod1, True)

	@MaxAmtByPrd.deleter
	def MaxAmtByPrd(self):
		del self._MaxAmtByPrd
		self._MaxAmtByPrd = base_types.UninitialisedField(self, 'MaxAmtByPrd', MaximumAmountByPeriod1, True)

	@property
	def MaxAmtByTx(self):
		return self._MaxAmtByTx

	@MaxAmtByTx.setter
	def MaxAmtByTx(self, value):
		self._MaxAmtByTx = value if value is not None else base_types.UninitialisedField(self, 'MaxAmtByTx', FixedAmountOrUnlimited1Choice, False)

	@MaxAmtByTx.deleter
	def MaxAmtByTx(self):
		del self._MaxAmtByTx
		self._MaxAmtByTx = base_types.UninitialisedField(self, 'MaxAmtByTx', FixedAmountOrUnlimited1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='MaxAmtByBlkSubmissn', type=FixedAmountOrUnlimited1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MaxAmtByPrd', type=MaximumAmountByPeriod1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MaxAmtByTx', type=FixedAmountOrUnlimited1Choice, min=0, max=1, mutex_group=None, array=False),
	))