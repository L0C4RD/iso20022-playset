# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AggregatedPenaltyAmount2
from . import AmountAndDirection5

class AggregatedPenaltyAmount1(base_types._BaseFieldType):

	__slots__ = ["_AggtdCdtAmt", "_AggtdDbtAmt", "_CtrPtyCSDAggtdAmt", "_GblNetAmt"]
	@property
	def AggtdCdtAmt(self):
		return self._AggtdCdtAmt

	@AggtdCdtAmt.setter
	def AggtdCdtAmt(self, value):
		self._AggtdCdtAmt = value if value is not None else base_types.UninitialisedField(self, 'AggtdCdtAmt', ActiveCurrencyAndAmount, False)

	@AggtdCdtAmt.deleter
	def AggtdCdtAmt(self):
		del self._AggtdCdtAmt
		self._AggtdCdtAmt = base_types.UninitialisedField(self, 'AggtdCdtAmt', ActiveCurrencyAndAmount, False)

	@property
	def AggtdDbtAmt(self):
		return self._AggtdDbtAmt

	@AggtdDbtAmt.setter
	def AggtdDbtAmt(self, value):
		self._AggtdDbtAmt = value if value is not None else base_types.UninitialisedField(self, 'AggtdDbtAmt', ActiveCurrencyAndAmount, False)

	@AggtdDbtAmt.deleter
	def AggtdDbtAmt(self):
		del self._AggtdDbtAmt
		self._AggtdDbtAmt = base_types.UninitialisedField(self, 'AggtdDbtAmt', ActiveCurrencyAndAmount, False)

	@property
	def CtrPtyCSDAggtdAmt(self):
		return self._CtrPtyCSDAggtdAmt

	@CtrPtyCSDAggtdAmt.setter
	def CtrPtyCSDAggtdAmt(self, value):
		self._CtrPtyCSDAggtdAmt = value if value is not None else base_types.UninitialisedField(self, 'CtrPtyCSDAggtdAmt', AggregatedPenaltyAmount2, True)

	@CtrPtyCSDAggtdAmt.deleter
	def CtrPtyCSDAggtdAmt(self):
		del self._CtrPtyCSDAggtdAmt
		self._CtrPtyCSDAggtdAmt = base_types.UninitialisedField(self, 'CtrPtyCSDAggtdAmt', AggregatedPenaltyAmount2, True)

	@property
	def GblNetAmt(self):
		return self._GblNetAmt

	@GblNetAmt.setter
	def GblNetAmt(self, value):
		self._GblNetAmt = value if value is not None else base_types.UninitialisedField(self, 'GblNetAmt', AmountAndDirection5, False)

	@GblNetAmt.deleter
	def GblNetAmt(self):
		del self._GblNetAmt
		self._GblNetAmt = base_types.UninitialisedField(self, 'GblNetAmt', AmountAndDirection5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtdCdtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtdDbtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrPtyCSDAggtdAmt', type=AggregatedPenaltyAmount2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GblNetAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
	))