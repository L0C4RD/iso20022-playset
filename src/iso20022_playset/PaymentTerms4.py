import base_types
import AmountOrPercentage2Choice
import PaymentCodeOrOther1Choice

class PaymentTerms4(base_types._BaseFieldType):

	__slots__ = ["_PmtTerms", "_AmtOrPctg"]
	@property
	def PmtTerms(self):
		return self._PmtTerms

	@PmtTerms.setter
	def PmtTerms(self, value):
		self._PmtTerms = value if type(value) != auto else self.make_default("PmtTerms")

	@PmtTerms.deleter
	def PmtTerms(self):
		del self._PmtTerms
		self._PmtTerms = None

	@property
	def AmtOrPctg(self):
		return self._AmtOrPctg

	@AmtOrPctg.setter
	def AmtOrPctg(self, value):
		self._AmtOrPctg = value if type(value) != auto else self.make_default("AmtOrPctg")

	@AmtOrPctg.deleter
	def AmtOrPctg(self):
		del self._AmtOrPctg
		self._AmtOrPctg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PmtTerms', type=PaymentCodeOrOther1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmtOrPctg', type=AmountOrPercentage2Choice, min=1, max=1, mutex_group=None, array=False),
	))

