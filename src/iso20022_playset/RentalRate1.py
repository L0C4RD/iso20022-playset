from . import base_types
import PeriodUnit3Code
import Max4NumericText
import Max35Text
import ImpliedCurrencyAndAmount

class RentalRate1(base_types._BaseFieldType):

	__slots__ = ["_Prd", "_PrdCnt", "_Rate", "_OthrPrd"]
	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def PrdCnt(self):
		return self._PrdCnt

	@PrdCnt.setter
	def PrdCnt(self, value):
		self._PrdCnt = value if type(value) != auto else self.make_default("PrdCnt")

	@PrdCnt.deleter
	def PrdCnt(self):
		del self._PrdCnt
		self._PrdCnt = None

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
	def OthrPrd(self):
		return self._OthrPrd

	@OthrPrd.setter
	def OthrPrd(self, value):
		self._OthrPrd = value if type(value) != auto else self.make_default("OthrPrd")

	@OthrPrd.deleter
	def OthrPrd(self):
		del self._OthrPrd
		self._OthrPrd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prd', type=PeriodUnit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrdCnt', type=Max4NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrPrd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

