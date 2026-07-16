# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ImpliedCurrencyAndAmount
from . import Max35Text
from . import Max4NumericText
from . import PeriodUnit4Code

class RentalRate2(base_types._BaseFieldType):

	__slots__ = ["_OthrPrd", "_Prd", "_PrdCnt", "_Rate"]
	@property
	def OthrPrd(self):
		return self._OthrPrd

	@OthrPrd.setter
	def OthrPrd(self, value):
		self._OthrPrd = value if value is not None else base_types.UninitialisedField(self, 'OthrPrd', Max35Text, False)

	@OthrPrd.deleter
	def OthrPrd(self):
		del self._OthrPrd
		self._OthrPrd = base_types.UninitialisedField(self, 'OthrPrd', Max35Text, False)

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', PeriodUnit4Code, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', PeriodUnit4Code, False)

	@property
	def PrdCnt(self):
		return self._PrdCnt

	@PrdCnt.setter
	def PrdCnt(self, value):
		self._PrdCnt = value if value is not None else base_types.UninitialisedField(self, 'PrdCnt', Max4NumericText, False)

	@PrdCnt.deleter
	def PrdCnt(self):
		del self._PrdCnt
		self._PrdCnt = base_types.UninitialisedField(self, 'PrdCnt', Max4NumericText, False)

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if value is not None else base_types.UninitialisedField(self, 'Rate', ImpliedCurrencyAndAmount, False)

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = base_types.UninitialisedField(self, 'Rate', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrPrd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=PeriodUnit4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdCnt', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))