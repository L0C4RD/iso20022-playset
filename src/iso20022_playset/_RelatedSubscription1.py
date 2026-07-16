# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveOrHistoricCurrencyAndAmount
from . import AdditionalReference11
from . import DecimalNumber

class RelatedSubscription1(base_types._BaseFieldType):

	__slots__ = ["_CntngntLqdtnPerUnit", "_DprctnDpstPerUnit", "_EqulstnCdtPerUnit", "_Ref", "_RltdAmt", "_RltdQty"]
	@property
	def CntngntLqdtnPerUnit(self):
		return self._CntngntLqdtnPerUnit

	@CntngntLqdtnPerUnit.setter
	def CntngntLqdtnPerUnit(self, value):
		self._CntngntLqdtnPerUnit = value if value is not None else base_types.UninitialisedField(self, 'CntngntLqdtnPerUnit', ActiveOrHistoricCurrencyAndAmount, False)

	@CntngntLqdtnPerUnit.deleter
	def CntngntLqdtnPerUnit(self):
		del self._CntngntLqdtnPerUnit
		self._CntngntLqdtnPerUnit = base_types.UninitialisedField(self, 'CntngntLqdtnPerUnit', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def DprctnDpstPerUnit(self):
		return self._DprctnDpstPerUnit

	@DprctnDpstPerUnit.setter
	def DprctnDpstPerUnit(self, value):
		self._DprctnDpstPerUnit = value if value is not None else base_types.UninitialisedField(self, 'DprctnDpstPerUnit', ActiveOrHistoricCurrencyAndAmount, False)

	@DprctnDpstPerUnit.deleter
	def DprctnDpstPerUnit(self):
		del self._DprctnDpstPerUnit
		self._DprctnDpstPerUnit = base_types.UninitialisedField(self, 'DprctnDpstPerUnit', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def EqulstnCdtPerUnit(self):
		return self._EqulstnCdtPerUnit

	@EqulstnCdtPerUnit.setter
	def EqulstnCdtPerUnit(self, value):
		self._EqulstnCdtPerUnit = value if value is not None else base_types.UninitialisedField(self, 'EqulstnCdtPerUnit', ActiveOrHistoricCurrencyAndAmount, False)

	@EqulstnCdtPerUnit.deleter
	def EqulstnCdtPerUnit(self):
		del self._EqulstnCdtPerUnit
		self._EqulstnCdtPerUnit = base_types.UninitialisedField(self, 'EqulstnCdtPerUnit', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', AdditionalReference11, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', AdditionalReference11, False)

	@property
	def RltdAmt(self):
		return self._RltdAmt

	@RltdAmt.setter
	def RltdAmt(self, value):
		self._RltdAmt = value if value is not None else base_types.UninitialisedField(self, 'RltdAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@RltdAmt.deleter
	def RltdAmt(self):
		del self._RltdAmt
		self._RltdAmt = base_types.UninitialisedField(self, 'RltdAmt', ActiveOrHistoricCurrencyAndAmount, False)

	@property
	def RltdQty(self):
		return self._RltdQty

	@RltdQty.setter
	def RltdQty(self, value):
		self._RltdQty = value if value is not None else base_types.UninitialisedField(self, 'RltdQty', DecimalNumber, False)

	@RltdQty.deleter
	def RltdQty(self):
		del self._RltdQty
		self._RltdQty = base_types.UninitialisedField(self, 'RltdQty', DecimalNumber, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntngntLqdtnPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DprctnDpstPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EqulstnCdtPerUnit', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=AdditionalReference11, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdAmt', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))