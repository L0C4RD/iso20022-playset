from . import base_types
from ._CompareAmountAndDirection3 import CompareAmountAndDirection3
from ._CompareDate3 import CompareDate3
from ._CompareOtherPaymentType1 import CompareOtherPaymentType1
from ._CompareOrganisationIdentification7 import CompareOrganisationIdentification7

class CompareOtherPayment1(base_types._BaseFieldType):

	__slots__ = ["_OthrPmtRcvr", "_OthrPmtDt", "_OthrPmtTp", "_OthrPmtAmt", "_OthrPmtPyer"]
	@property
	def OthrPmtRcvr(self):
		return self._OthrPmtRcvr

	@OthrPmtRcvr.setter
	def OthrPmtRcvr(self, value):
		self._OthrPmtRcvr = value if type(value) != base_types.auto else self.make_default("OthrPmtRcvr")

	@OthrPmtRcvr.deleter
	def OthrPmtRcvr(self):
		del self._OthrPmtRcvr
		self._OthrPmtRcvr = None

	@property
	def OthrPmtDt(self):
		return self._OthrPmtDt

	@OthrPmtDt.setter
	def OthrPmtDt(self, value):
		self._OthrPmtDt = value if type(value) != base_types.auto else self.make_default("OthrPmtDt")

	@OthrPmtDt.deleter
	def OthrPmtDt(self):
		del self._OthrPmtDt
		self._OthrPmtDt = None

	@property
	def OthrPmtTp(self):
		return self._OthrPmtTp

	@OthrPmtTp.setter
	def OthrPmtTp(self, value):
		self._OthrPmtTp = value if type(value) != base_types.auto else self.make_default("OthrPmtTp")

	@OthrPmtTp.deleter
	def OthrPmtTp(self):
		del self._OthrPmtTp
		self._OthrPmtTp = None

	@property
	def OthrPmtAmt(self):
		return self._OthrPmtAmt

	@OthrPmtAmt.setter
	def OthrPmtAmt(self, value):
		self._OthrPmtAmt = value if type(value) != base_types.auto else self.make_default("OthrPmtAmt")

	@OthrPmtAmt.deleter
	def OthrPmtAmt(self):
		del self._OthrPmtAmt
		self._OthrPmtAmt = None

	@property
	def OthrPmtPyer(self):
		return self._OthrPmtPyer

	@OthrPmtPyer.setter
	def OthrPmtPyer(self, value):
		self._OthrPmtPyer = value if type(value) != base_types.auto else self.make_default("OthrPmtPyer")

	@OthrPmtPyer.deleter
	def OthrPmtPyer(self):
		del self._OthrPmtPyer
		self._OthrPmtPyer = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPmtRcvr', type=CompareOrganisationIdentification7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmtDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmtTp', type=CompareOtherPaymentType1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmtAmt', type=CompareAmountAndDirection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmtPyer', type=CompareOrganisationIdentification7, min=0, max=1, mutex_group=None, array=False),
	))

