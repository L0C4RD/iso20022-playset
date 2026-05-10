import base_types
import RateTypeAndLookback2
import PercentageRate

class RateOrName4Choice(base_types._BaseFieldType):

	__slots__ = ["_Rate", "_RateIndxDtls"]
	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def RateIndxDtls(self):
		return self._RateIndxDtls

	@RateIndxDtls.setter
	def RateIndxDtls(self, value):
		self._RateIndxDtls = value if type(value) != auto else self.make_default("RateIndxDtls")

	@RateIndxDtls.deleter
	def RateIndxDtls(self):
		del self._RateIndxDtls
		self._RateIndxDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='RateIndxDtls', type=RateTypeAndLookback2, min=0, max=1, mutex_group=1, array=False),
	))

