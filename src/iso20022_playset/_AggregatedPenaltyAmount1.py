# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._AggregatedPenaltyAmount2 import AggregatedPenaltyAmount2
from ._AmountAndDirection5 import AmountAndDirection5

class AggregatedPenaltyAmount1(base_types._BaseFieldType):

	__slots__ = ["_AggtdCdtAmt", "_AggtdDbtAmt", "_CtrPtyCSDAggtdAmt", "_GblNetAmt"]
	@property
	def AggtdCdtAmt(self):
		return self._AggtdCdtAmt

	@AggtdCdtAmt.setter
	def AggtdCdtAmt(self, value):
		self._AggtdCdtAmt = value if type(value) != base_types.auto else self.make_default("AggtdCdtAmt")

	@AggtdCdtAmt.deleter
	def AggtdCdtAmt(self):
		del self._AggtdCdtAmt
		self._AggtdCdtAmt = None

	@property
	def AggtdDbtAmt(self):
		return self._AggtdDbtAmt

	@AggtdDbtAmt.setter
	def AggtdDbtAmt(self, value):
		self._AggtdDbtAmt = value if type(value) != base_types.auto else self.make_default("AggtdDbtAmt")

	@AggtdDbtAmt.deleter
	def AggtdDbtAmt(self):
		del self._AggtdDbtAmt
		self._AggtdDbtAmt = None

	@property
	def CtrPtyCSDAggtdAmt(self):
		return self._CtrPtyCSDAggtdAmt

	@CtrPtyCSDAggtdAmt.setter
	def CtrPtyCSDAggtdAmt(self, value):
		self._CtrPtyCSDAggtdAmt = value if type(value) != base_types.auto else self.make_default("CtrPtyCSDAggtdAmt")

	@CtrPtyCSDAggtdAmt.deleter
	def CtrPtyCSDAggtdAmt(self):
		del self._CtrPtyCSDAggtdAmt
		self._CtrPtyCSDAggtdAmt = None

	@property
	def GblNetAmt(self):
		return self._GblNetAmt

	@GblNetAmt.setter
	def GblNetAmt(self, value):
		self._GblNetAmt = value if type(value) != base_types.auto else self.make_default("GblNetAmt")

	@GblNetAmt.deleter
	def GblNetAmt(self):
		del self._GblNetAmt
		self._GblNetAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtdCdtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtdDbtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyCSDAggtdAmt', type=AggregatedPenaltyAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GblNetAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
	))