from . import base_types
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from .AmountAndDirection102 import AmountAndDirection102
from .ClearingMemberFee1 import ClearingMemberFee1

class IncomeStatement2(base_types._BaseFieldType):

	__slots__ = ["_PstTaxPrftOrLoss", "_OthrOprgRvn", "_ClrMmbFee", "_PreTaxPrftOrLoss", "_OprgExpnss", "_NonOprgExpnss", "_NetIntrstIncm", "_OthrNonOprgRvn", "_OprgPrftOrLoss"]
	@property
	def PstTaxPrftOrLoss(self):
		return self._PstTaxPrftOrLoss

	@PstTaxPrftOrLoss.setter
	def PstTaxPrftOrLoss(self, value):
		self._PstTaxPrftOrLoss = value if type(value) != base_types.auto else self.make_default("PstTaxPrftOrLoss")

	@PstTaxPrftOrLoss.deleter
	def PstTaxPrftOrLoss(self):
		del self._PstTaxPrftOrLoss
		self._PstTaxPrftOrLoss = None

	@property
	def OthrOprgRvn(self):
		return self._OthrOprgRvn

	@OthrOprgRvn.setter
	def OthrOprgRvn(self, value):
		self._OthrOprgRvn = value if type(value) != base_types.auto else self.make_default("OthrOprgRvn")

	@OthrOprgRvn.deleter
	def OthrOprgRvn(self):
		del self._OthrOprgRvn
		self._OthrOprgRvn = None

	@property
	def ClrMmbFee(self):
		return self._ClrMmbFee

	@ClrMmbFee.setter
	def ClrMmbFee(self, value):
		self._ClrMmbFee = value if type(value) != base_types.auto else self.make_default("ClrMmbFee")

	@ClrMmbFee.deleter
	def ClrMmbFee(self):
		del self._ClrMmbFee
		self._ClrMmbFee = None

	@property
	def PreTaxPrftOrLoss(self):
		return self._PreTaxPrftOrLoss

	@PreTaxPrftOrLoss.setter
	def PreTaxPrftOrLoss(self, value):
		self._PreTaxPrftOrLoss = value if type(value) != base_types.auto else self.make_default("PreTaxPrftOrLoss")

	@PreTaxPrftOrLoss.deleter
	def PreTaxPrftOrLoss(self):
		del self._PreTaxPrftOrLoss
		self._PreTaxPrftOrLoss = None

	@property
	def OprgExpnss(self):
		return self._OprgExpnss

	@OprgExpnss.setter
	def OprgExpnss(self, value):
		self._OprgExpnss = value if type(value) != base_types.auto else self.make_default("OprgExpnss")

	@OprgExpnss.deleter
	def OprgExpnss(self):
		del self._OprgExpnss
		self._OprgExpnss = None

	@property
	def NonOprgExpnss(self):
		return self._NonOprgExpnss

	@NonOprgExpnss.setter
	def NonOprgExpnss(self, value):
		self._NonOprgExpnss = value if type(value) != base_types.auto else self.make_default("NonOprgExpnss")

	@NonOprgExpnss.deleter
	def NonOprgExpnss(self):
		del self._NonOprgExpnss
		self._NonOprgExpnss = None

	@property
	def NetIntrstIncm(self):
		return self._NetIntrstIncm

	@NetIntrstIncm.setter
	def NetIntrstIncm(self, value):
		self._NetIntrstIncm = value if type(value) != base_types.auto else self.make_default("NetIntrstIncm")

	@NetIntrstIncm.deleter
	def NetIntrstIncm(self):
		del self._NetIntrstIncm
		self._NetIntrstIncm = None

	@property
	def OthrNonOprgRvn(self):
		return self._OthrNonOprgRvn

	@OthrNonOprgRvn.setter
	def OthrNonOprgRvn(self, value):
		self._OthrNonOprgRvn = value if type(value) != base_types.auto else self.make_default("OthrNonOprgRvn")

	@OthrNonOprgRvn.deleter
	def OthrNonOprgRvn(self):
		del self._OthrNonOprgRvn
		self._OthrNonOprgRvn = None

	@property
	def OprgPrftOrLoss(self):
		return self._OprgPrftOrLoss

	@OprgPrftOrLoss.setter
	def OprgPrftOrLoss(self, value):
		self._OprgPrftOrLoss = value if type(value) != base_types.auto else self.make_default("OprgPrftOrLoss")

	@OprgPrftOrLoss.deleter
	def OprgPrftOrLoss(self):
		del self._OprgPrftOrLoss
		self._OprgPrftOrLoss = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PstTaxPrftOrLoss', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrOprgRvn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClrMmbFee', type=ClearingMemberFee1, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PreTaxPrftOrLoss', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgExpnss', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NonOprgExpnss', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetIntrstIncm', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrNonOprgRvn', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprgPrftOrLoss', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
	))

