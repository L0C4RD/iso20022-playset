# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import TrueFalseIndicator

class PaymentConditionStatus2(base_types._BaseFieldType):

	__slots__ = ["_AccptdAmt", "_EarlyPmt", "_GrntedPmt"]
	@property
	def AccptdAmt(self):
		return self._AccptdAmt

	@AccptdAmt.setter
	def AccptdAmt(self, value):
		self._AccptdAmt = value if value is not None else base_types.UninitialisedField(self, 'AccptdAmt', ActiveCurrencyAndAmount, False)

	@AccptdAmt.deleter
	def AccptdAmt(self):
		del self._AccptdAmt
		self._AccptdAmt = base_types.UninitialisedField(self, 'AccptdAmt', ActiveCurrencyAndAmount, False)

	@property
	def EarlyPmt(self):
		return self._EarlyPmt

	@EarlyPmt.setter
	def EarlyPmt(self, value):
		self._EarlyPmt = value if value is not None else base_types.UninitialisedField(self, 'EarlyPmt', TrueFalseIndicator, False)

	@EarlyPmt.deleter
	def EarlyPmt(self):
		del self._EarlyPmt
		self._EarlyPmt = base_types.UninitialisedField(self, 'EarlyPmt', TrueFalseIndicator, False)

	@property
	def GrntedPmt(self):
		return self._GrntedPmt

	@GrntedPmt.setter
	def GrntedPmt(self, value):
		self._GrntedPmt = value if value is not None else base_types.UninitialisedField(self, 'GrntedPmt', TrueFalseIndicator, False)

	@GrntedPmt.deleter
	def GrntedPmt(self):
		del self._GrntedPmt
		self._GrntedPmt = base_types.UninitialisedField(self, 'GrntedPmt', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EarlyPmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GrntedPmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))