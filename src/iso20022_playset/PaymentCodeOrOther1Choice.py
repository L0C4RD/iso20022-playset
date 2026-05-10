from . import base_types
import ISODate
import PaymentPeriod3
import Max140Text

class PaymentCodeOrOther1Choice(base_types._BaseFieldType):

	__slots__ = ["_OthrPmtTerms", "_PmtDueDt", "_PmtCd"]
	@property
	def OthrPmtTerms(self):
		return self._OthrPmtTerms

	@OthrPmtTerms.setter
	def OthrPmtTerms(self, value):
		self._OthrPmtTerms = value if type(value) != auto else self.make_default("OthrPmtTerms")

	@OthrPmtTerms.deleter
	def OthrPmtTerms(self):
		del self._OthrPmtTerms
		self._OthrPmtTerms = None

	@property
	def PmtDueDt(self):
		return self._PmtDueDt

	@PmtDueDt.setter
	def PmtDueDt(self, value):
		self._PmtDueDt = value if type(value) != auto else self.make_default("PmtDueDt")

	@PmtDueDt.deleter
	def PmtDueDt(self):
		del self._PmtDueDt
		self._PmtDueDt = None

	@property
	def PmtCd(self):
		return self._PmtCd

	@PmtCd.setter
	def PmtCd(self, value):
		self._PmtCd = value if type(value) != auto else self.make_default("PmtCd")

	@PmtCd.deleter
	def PmtCd(self):
		del self._PmtCd
		self._PmtCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPmtTerms', type=Max140Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtDueDt', type=ISODate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PmtCd', type=PaymentPeriod3, min=0, max=1, mutex_group=1, array=False),
	))

