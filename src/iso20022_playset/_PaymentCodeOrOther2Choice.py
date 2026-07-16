# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import Max140Text
from . import PaymentPeriod4

class PaymentCodeOrOther2Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrPmtTerms", "_PmtCd", "_PmtDueDt"]
	@property
	def OthrPmtTerms(self):
		return self._OthrPmtTerms

	@OthrPmtTerms.setter
	def OthrPmtTerms(self, value):
		self._OthrPmtTerms = value if value is not None else base_types.UninitialisedField(self, 'OthrPmtTerms', Max140Text, False)

	@OthrPmtTerms.deleter
	def OthrPmtTerms(self):
		del self._OthrPmtTerms
		self._OthrPmtTerms = base_types.UninitialisedField(self, 'OthrPmtTerms', Max140Text, False)

	@property
	def PmtCd(self):
		return self._PmtCd

	@PmtCd.setter
	def PmtCd(self, value):
		self._PmtCd = value if value is not None else base_types.UninitialisedField(self, 'PmtCd', PaymentPeriod4, False)

	@PmtCd.deleter
	def PmtCd(self):
		del self._PmtCd
		self._PmtCd = base_types.UninitialisedField(self, 'PmtCd', PaymentPeriod4, False)

	@property
	def PmtDueDt(self):
		return self._PmtDueDt

	@PmtDueDt.setter
	def PmtDueDt(self, value):
		self._PmtDueDt = value if value is not None else base_types.UninitialisedField(self, 'PmtDueDt', ISODate, False)

	@PmtDueDt.deleter
	def PmtDueDt(self):
		del self._PmtDueDt
		self._PmtDueDt = base_types.UninitialisedField(self, 'PmtDueDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPmtTerms', type=Max140Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtCd', type=PaymentPeriod4, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtDueDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
	))