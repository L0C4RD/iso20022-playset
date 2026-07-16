# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountOrRate4Choice
from . import FXAmountType1Choice
from . import PlusOrMinusIndicator

class FXCommissionOrFee1(base_types._BaseFieldType):

	__slots__ = ["_AmtOrRate", "_Sgn", "_Tp"]
	@property
	def AmtOrRate(self):
		return self._AmtOrRate

	@AmtOrRate.setter
	def AmtOrRate(self, value):
		self._AmtOrRate = value if value is not None else base_types.UninitialisedField(self, 'AmtOrRate', AmountOrRate4Choice, False)

	@AmtOrRate.deleter
	def AmtOrRate(self):
		del self._AmtOrRate
		self._AmtOrRate = base_types.UninitialisedField(self, 'AmtOrRate', AmountOrRate4Choice, False)

	@property
	def Sgn(self):
		return self._Sgn

	@Sgn.setter
	def Sgn(self, value):
		self._Sgn = value if value is not None else base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	@Sgn.deleter
	def Sgn(self):
		del self._Sgn
		self._Sgn = base_types.UninitialisedField(self, 'Sgn', PlusOrMinusIndicator, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', FXAmountType1Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', FXAmountType1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmtOrRate', type=AmountOrRate4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FXAmountType1Choice, min=1, max=1, mutex_group=None, array=False),
	))