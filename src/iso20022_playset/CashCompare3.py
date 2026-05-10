import base_types
import ComparePercentageRate3
import CompareAmountAndDirection2

class CashCompare3(base_types._BaseFieldType):

	__slots__ = ["_HrcutOrMrgn", "_Val"]
	@property
	def HrcutOrMrgn(self):
		return self._HrcutOrMrgn

	@HrcutOrMrgn.setter
	def HrcutOrMrgn(self, value):
		self._HrcutOrMrgn = value if type(value) != auto else self.make_default("HrcutOrMrgn")

	@HrcutOrMrgn.deleter
	def HrcutOrMrgn(self):
		del self._HrcutOrMrgn
		self._HrcutOrMrgn = None

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if type(value) != auto else self.make_default("Val")

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HrcutOrMrgn', type=ComparePercentageRate3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=CompareAmountAndDirection2, min=0, max=1, mutex_group=None, array=False),
	))

