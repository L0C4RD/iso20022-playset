# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BillingRateIdentification1Choice
from . import Number
from . import PercentageRate

class BillingRate1(base_types._BaseFieldType):

	__slots__ = ["_DaysInPrd", "_DaysInYr", "_Id", "_Val"]
	@property
	def DaysInPrd(self):
		return self._DaysInPrd

	@DaysInPrd.setter
	def DaysInPrd(self, value):
		self._DaysInPrd = value if value is not None else base_types.UninitialisedField(self, 'DaysInPrd', Number, False)

	@DaysInPrd.deleter
	def DaysInPrd(self):
		del self._DaysInPrd
		self._DaysInPrd = base_types.UninitialisedField(self, 'DaysInPrd', Number, False)

	@property
	def DaysInYr(self):
		return self._DaysInYr

	@DaysInYr.setter
	def DaysInYr(self, value):
		self._DaysInYr = value if value is not None else base_types.UninitialisedField(self, 'DaysInYr', Number, False)

	@DaysInYr.deleter
	def DaysInYr(self):
		del self._DaysInYr
		self._DaysInYr = base_types.UninitialisedField(self, 'DaysInYr', Number, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', BillingRateIdentification1Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', BillingRateIdentification1Choice, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', PercentageRate, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', PercentageRate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DaysInPrd', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DaysInYr', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=BillingRateIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
	))