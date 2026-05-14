# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._AdditionalReference11 import AdditionalReference11
from ._DecimalNumber import DecimalNumber

class RelatedSubscription1(base_types._BaseFieldType):

	__slots__ = ["_CntngntLqdtnPerUnit", "_DprctnDpstPerUnit", "_EqulstnCdtPerUnit", "_Ref", "_RltdAmt", "_RltdQty"]
	@property
	def CntngntLqdtnPerUnit(self):
		return self._CntngntLqdtnPerUnit

	@CntngntLqdtnPerUnit.setter
	def CntngntLqdtnPerUnit(self, value):
		self._CntngntLqdtnPerUnit = value if type(value) != base_types.auto else self.make_default("CntngntLqdtnPerUnit")

	@CntngntLqdtnPerUnit.deleter
	def CntngntLqdtnPerUnit(self):
		del self._CntngntLqdtnPerUnit
		self._CntngntLqdtnPerUnit = None

	@property
	def DprctnDpstPerUnit(self):
		return self._DprctnDpstPerUnit

	@DprctnDpstPerUnit.setter
	def DprctnDpstPerUnit(self, value):
		self._DprctnDpstPerUnit = value if type(value) != base_types.auto else self.make_default("DprctnDpstPerUnit")

	@DprctnDpstPerUnit.deleter
	def DprctnDpstPerUnit(self):
		del self._DprctnDpstPerUnit
		self._DprctnDpstPerUnit = None

	@property
	def EqulstnCdtPerUnit(self):
		return self._EqulstnCdtPerUnit

	@EqulstnCdtPerUnit.setter
	def EqulstnCdtPerUnit(self, value):
		self._EqulstnCdtPerUnit = value if type(value) != base_types.auto else self.make_default("EqulstnCdtPerUnit")

	@EqulstnCdtPerUnit.deleter
	def EqulstnCdtPerUnit(self):
		del self._EqulstnCdtPerUnit
		self._EqulstnCdtPerUnit = None

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if type(value) != base_types.auto else self.make_default("Ref")

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = None

	@property
	def RltdAmt(self):
		return self._RltdAmt

	@RltdAmt.setter
	def RltdAmt(self, value):
		self._RltdAmt = value if type(value) != base_types.auto else self.make_default("RltdAmt")

	@RltdAmt.deleter
	def RltdAmt(self):
		del self._RltdAmt
		self._RltdAmt = None

	@property
	def RltdQty(self):
		return self._RltdQty

	@RltdQty.setter
	def RltdQty(self, value):
		self._RltdQty = value if type(value) != base_types.auto else self.make_default("RltdQty")

	@RltdQty.deleter
	def RltdQty(self):
		del self._RltdQty
		self._RltdQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntngntLqdtnPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DprctnDpstPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnCdtPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=AdditionalReference11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))