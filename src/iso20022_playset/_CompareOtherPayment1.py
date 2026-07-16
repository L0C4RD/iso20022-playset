# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CompareAmountAndDirection3
from . import CompareDate3
from . import CompareOrganisationIdentification7
from . import CompareOtherPaymentType1

class CompareOtherPayment1(base_types._BaseFieldType):

	__slots__ = ["_OthrPmtAmt", "_OthrPmtDt", "_OthrPmtPyer", "_OthrPmtRcvr", "_OthrPmtTp"]
	@property
	def OthrPmtAmt(self):
		return self._OthrPmtAmt

	@OthrPmtAmt.setter
	def OthrPmtAmt(self, value):
		self._OthrPmtAmt = value if value is not None else base_types.UninitialisedField(self, 'OthrPmtAmt', CompareAmountAndDirection3, False)

	@OthrPmtAmt.deleter
	def OthrPmtAmt(self):
		del self._OthrPmtAmt
		self._OthrPmtAmt = base_types.UninitialisedField(self, 'OthrPmtAmt', CompareAmountAndDirection3, False)

	@property
	def OthrPmtDt(self):
		return self._OthrPmtDt

	@OthrPmtDt.setter
	def OthrPmtDt(self, value):
		self._OthrPmtDt = value if value is not None else base_types.UninitialisedField(self, 'OthrPmtDt', CompareDate3, False)

	@OthrPmtDt.deleter
	def OthrPmtDt(self):
		del self._OthrPmtDt
		self._OthrPmtDt = base_types.UninitialisedField(self, 'OthrPmtDt', CompareDate3, False)

	@property
	def OthrPmtPyer(self):
		return self._OthrPmtPyer

	@OthrPmtPyer.setter
	def OthrPmtPyer(self, value):
		self._OthrPmtPyer = value if value is not None else base_types.UninitialisedField(self, 'OthrPmtPyer', CompareOrganisationIdentification7, False)

	@OthrPmtPyer.deleter
	def OthrPmtPyer(self):
		del self._OthrPmtPyer
		self._OthrPmtPyer = base_types.UninitialisedField(self, 'OthrPmtPyer', CompareOrganisationIdentification7, False)

	@property
	def OthrPmtRcvr(self):
		return self._OthrPmtRcvr

	@OthrPmtRcvr.setter
	def OthrPmtRcvr(self, value):
		self._OthrPmtRcvr = value if value is not None else base_types.UninitialisedField(self, 'OthrPmtRcvr', CompareOrganisationIdentification7, False)

	@OthrPmtRcvr.deleter
	def OthrPmtRcvr(self):
		del self._OthrPmtRcvr
		self._OthrPmtRcvr = base_types.UninitialisedField(self, 'OthrPmtRcvr', CompareOrganisationIdentification7, False)

	@property
	def OthrPmtTp(self):
		return self._OthrPmtTp

	@OthrPmtTp.setter
	def OthrPmtTp(self, value):
		self._OthrPmtTp = value if value is not None else base_types.UninitialisedField(self, 'OthrPmtTp', CompareOtherPaymentType1, False)

	@OthrPmtTp.deleter
	def OthrPmtTp(self):
		del self._OthrPmtTp
		self._OthrPmtTp = base_types.UninitialisedField(self, 'OthrPmtTp', CompareOtherPaymentType1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPmtAmt', type=CompareAmountAndDirection3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmtDt', type=CompareDate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmtPyer', type=CompareOrganisationIdentification7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmtRcvr', type=CompareOrganisationIdentification7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPmtTp', type=CompareOtherPaymentType1, min=0, max=1, mutex_group=None, array=False),
	))