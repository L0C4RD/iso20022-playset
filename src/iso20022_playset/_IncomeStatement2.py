# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import AmountAndDirection102
from . import ClearingMemberFee1

class IncomeStatement2(base_types._BaseFieldType):

	__slots__ = ["_ClrMmbFee", "_NetIntrstIncm", "_NonOprgExpnss", "_OprgExpnss", "_OprgPrftOrLoss", "_OthrNonOprgRvn", "_OthrOprgRvn", "_PreTaxPrftOrLoss", "_PstTaxPrftOrLoss"]
	@property
	def ClrMmbFee(self):
		return self._ClrMmbFee

	@ClrMmbFee.setter
	def ClrMmbFee(self, value):
		self._ClrMmbFee = value if value is not None else base_types.UninitialisedField(self, 'ClrMmbFee', ClearingMemberFee1, True)

	@ClrMmbFee.deleter
	def ClrMmbFee(self):
		del self._ClrMmbFee
		self._ClrMmbFee = base_types.UninitialisedField(self, 'ClrMmbFee', ClearingMemberFee1, True)

	@property
	def NetIntrstIncm(self):
		return self._NetIntrstIncm

	@NetIntrstIncm.setter
	def NetIntrstIncm(self, value):
		self._NetIntrstIncm = value if value is not None else base_types.UninitialisedField(self, 'NetIntrstIncm', ActiveCurrencyAndAmount, False)

	@NetIntrstIncm.deleter
	def NetIntrstIncm(self):
		del self._NetIntrstIncm
		self._NetIntrstIncm = base_types.UninitialisedField(self, 'NetIntrstIncm', ActiveCurrencyAndAmount, False)

	@property
	def NonOprgExpnss(self):
		return self._NonOprgExpnss

	@NonOprgExpnss.setter
	def NonOprgExpnss(self, value):
		self._NonOprgExpnss = value if value is not None else base_types.UninitialisedField(self, 'NonOprgExpnss', ActiveCurrencyAndAmount, False)

	@NonOprgExpnss.deleter
	def NonOprgExpnss(self):
		del self._NonOprgExpnss
		self._NonOprgExpnss = base_types.UninitialisedField(self, 'NonOprgExpnss', ActiveCurrencyAndAmount, False)

	@property
	def OprgExpnss(self):
		return self._OprgExpnss

	@OprgExpnss.setter
	def OprgExpnss(self, value):
		self._OprgExpnss = value if value is not None else base_types.UninitialisedField(self, 'OprgExpnss', ActiveCurrencyAndAmount, False)

	@OprgExpnss.deleter
	def OprgExpnss(self):
		del self._OprgExpnss
		self._OprgExpnss = base_types.UninitialisedField(self, 'OprgExpnss', ActiveCurrencyAndAmount, False)

	@property
	def OprgPrftOrLoss(self):
		return self._OprgPrftOrLoss

	@OprgPrftOrLoss.setter
	def OprgPrftOrLoss(self, value):
		self._OprgPrftOrLoss = value if value is not None else base_types.UninitialisedField(self, 'OprgPrftOrLoss', AmountAndDirection102, False)

	@OprgPrftOrLoss.deleter
	def OprgPrftOrLoss(self):
		del self._OprgPrftOrLoss
		self._OprgPrftOrLoss = base_types.UninitialisedField(self, 'OprgPrftOrLoss', AmountAndDirection102, False)

	@property
	def OthrNonOprgRvn(self):
		return self._OthrNonOprgRvn

	@OthrNonOprgRvn.setter
	def OthrNonOprgRvn(self, value):
		self._OthrNonOprgRvn = value if value is not None else base_types.UninitialisedField(self, 'OthrNonOprgRvn', ActiveCurrencyAndAmount, False)

	@OthrNonOprgRvn.deleter
	def OthrNonOprgRvn(self):
		del self._OthrNonOprgRvn
		self._OthrNonOprgRvn = base_types.UninitialisedField(self, 'OthrNonOprgRvn', ActiveCurrencyAndAmount, False)

	@property
	def OthrOprgRvn(self):
		return self._OthrOprgRvn

	@OthrOprgRvn.setter
	def OthrOprgRvn(self, value):
		self._OthrOprgRvn = value if value is not None else base_types.UninitialisedField(self, 'OthrOprgRvn', ActiveCurrencyAndAmount, False)

	@OthrOprgRvn.deleter
	def OthrOprgRvn(self):
		del self._OthrOprgRvn
		self._OthrOprgRvn = base_types.UninitialisedField(self, 'OthrOprgRvn', ActiveCurrencyAndAmount, False)

	@property
	def PreTaxPrftOrLoss(self):
		return self._PreTaxPrftOrLoss

	@PreTaxPrftOrLoss.setter
	def PreTaxPrftOrLoss(self, value):
		self._PreTaxPrftOrLoss = value if value is not None else base_types.UninitialisedField(self, 'PreTaxPrftOrLoss', AmountAndDirection102, False)

	@PreTaxPrftOrLoss.deleter
	def PreTaxPrftOrLoss(self):
		del self._PreTaxPrftOrLoss
		self._PreTaxPrftOrLoss = base_types.UninitialisedField(self, 'PreTaxPrftOrLoss', AmountAndDirection102, False)

	@property
	def PstTaxPrftOrLoss(self):
		return self._PstTaxPrftOrLoss

	@PstTaxPrftOrLoss.setter
	def PstTaxPrftOrLoss(self, value):
		self._PstTaxPrftOrLoss = value if value is not None else base_types.UninitialisedField(self, 'PstTaxPrftOrLoss', AmountAndDirection102, False)

	@PstTaxPrftOrLoss.deleter
	def PstTaxPrftOrLoss(self):
		del self._PstTaxPrftOrLoss
		self._PstTaxPrftOrLoss = base_types.UninitialisedField(self, 'PstTaxPrftOrLoss', AmountAndDirection102, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClrMmbFee', type=ClearingMemberFee1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NetIntrstIncm', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonOprgExpnss', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgExpnss', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgPrftOrLoss', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrNonOprgRvn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrOprgRvn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PreTaxPrftOrLoss', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstTaxPrftOrLoss', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
	))