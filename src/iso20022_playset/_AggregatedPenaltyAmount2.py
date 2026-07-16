# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AmountAndDirection5
from . import PartyIdentification136

class AggregatedPenaltyAmount2(base_types._BaseFieldType):

	__slots__ = ["_AggtdCdtAmt", "_AggtdDbtAmt", "_GblNetAmt", "_PtyId"]
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
	def GblNetAmt(self):
		return self._GblNetAmt

	@GblNetAmt.setter
	def GblNetAmt(self, value):
		self._GblNetAmt = value if value is not None else base_types.UninitialisedField(self, 'GblNetAmt', AmountAndDirection5, False)

	@GblNetAmt.deleter
	def GblNetAmt(self):
		del self._GblNetAmt
		self._GblNetAmt = base_types.UninitialisedField(self, 'GblNetAmt', AmountAndDirection5, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification136, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification136, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AggtdCdtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AggtdDbtAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GblNetAmt', type=AmountAndDirection5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification136, min=1, max=1, mutex_group=None, array=False),
	))