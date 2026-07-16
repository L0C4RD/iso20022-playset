# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AttendanceContext2Code
from . import DecimalNumber
from . import ImpliedCurrencyAndAmount
from . import Max10Text
from . import Max140Text
from . import Max256Text
from . import Max35Text
from . import Max70Text
from . import PlusOrMinusIndicator
from . import UnitOfMeasure6Code

class Product6(base_types._BaseFieldType):

	__slots__ = ["_AddtlPdctCd", "_AddtlPdctDesc", "_DlvryLctn", "_DlvrySvc", "_ItmId", "_PdctAmt", "_PdctAmtSgn", "_PdctCd", "_PdctDesc", "_PdctQty", "_SaleChanl", "_TaxTp", "_UnitOfMeasr", "_UnitPric", "_UnitPricSgn", "_ValAddedTax"]
	@property
	def AddtlPdctCd(self):
		return self._AddtlPdctCd

	@AddtlPdctCd.setter
	def AddtlPdctCd(self, value):
		self._AddtlPdctCd = value if value is not None else base_types.UninitialisedField(self, 'AddtlPdctCd', Max70Text, False)

	@AddtlPdctCd.deleter
	def AddtlPdctCd(self):
		del self._AddtlPdctCd
		self._AddtlPdctCd = base_types.UninitialisedField(self, 'AddtlPdctCd', Max70Text, False)

	@property
	def AddtlPdctDesc(self):
		return self._AddtlPdctDesc

	@AddtlPdctDesc.setter
	def AddtlPdctDesc(self, value):
		self._AddtlPdctDesc = value if value is not None else base_types.UninitialisedField(self, 'AddtlPdctDesc', Max256Text, False)

	@AddtlPdctDesc.deleter
	def AddtlPdctDesc(self):
		del self._AddtlPdctDesc
		self._AddtlPdctDesc = base_types.UninitialisedField(self, 'AddtlPdctDesc', Max256Text, False)

	@property
	def DlvryLctn(self):
		return self._DlvryLctn

	@DlvryLctn.setter
	def DlvryLctn(self, value):
		self._DlvryLctn = value if value is not None else base_types.UninitialisedField(self, 'DlvryLctn', Max10Text, False)

	@DlvryLctn.deleter
	def DlvryLctn(self):
		del self._DlvryLctn
		self._DlvryLctn = base_types.UninitialisedField(self, 'DlvryLctn', Max10Text, False)

	@property
	def DlvrySvc(self):
		return self._DlvrySvc

	@DlvrySvc.setter
	def DlvrySvc(self, value):
		self._DlvrySvc = value if value is not None else base_types.UninitialisedField(self, 'DlvrySvc', AttendanceContext2Code, False)

	@DlvrySvc.deleter
	def DlvrySvc(self):
		del self._DlvrySvc
		self._DlvrySvc = base_types.UninitialisedField(self, 'DlvrySvc', AttendanceContext2Code, False)

	@property
	def ItmId(self):
		return self._ItmId

	@ItmId.setter
	def ItmId(self, value):
		self._ItmId = value if value is not None else base_types.UninitialisedField(self, 'ItmId', Max35Text, False)

	@ItmId.deleter
	def ItmId(self):
		del self._ItmId
		self._ItmId = base_types.UninitialisedField(self, 'ItmId', Max35Text, False)

	@property
	def PdctAmt(self):
		return self._PdctAmt

	@PdctAmt.setter
	def PdctAmt(self, value):
		self._PdctAmt = value if value is not None else base_types.UninitialisedField(self, 'PdctAmt', ImpliedCurrencyAndAmount, False)

	@PdctAmt.deleter
	def PdctAmt(self):
		del self._PdctAmt
		self._PdctAmt = base_types.UninitialisedField(self, 'PdctAmt', ImpliedCurrencyAndAmount, False)

	@property
	def PdctAmtSgn(self):
		return self._PdctAmtSgn

	@PdctAmtSgn.setter
	def PdctAmtSgn(self, value):
		self._PdctAmtSgn = value if value is not None else base_types.UninitialisedField(self, 'PdctAmtSgn', PlusOrMinusIndicator, False)

	@PdctAmtSgn.deleter
	def PdctAmtSgn(self):
		del self._PdctAmtSgn
		self._PdctAmtSgn = base_types.UninitialisedField(self, 'PdctAmtSgn', PlusOrMinusIndicator, False)

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if value is not None else base_types.UninitialisedField(self, 'PdctCd', Max70Text, False)

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = base_types.UninitialisedField(self, 'PdctCd', Max70Text, False)

	@property
	def PdctDesc(self):
		return self._PdctDesc

	@PdctDesc.setter
	def PdctDesc(self, value):
		self._PdctDesc = value if value is not None else base_types.UninitialisedField(self, 'PdctDesc', Max140Text, False)

	@PdctDesc.deleter
	def PdctDesc(self):
		del self._PdctDesc
		self._PdctDesc = base_types.UninitialisedField(self, 'PdctDesc', Max140Text, False)

	@property
	def PdctQty(self):
		return self._PdctQty

	@PdctQty.setter
	def PdctQty(self, value):
		self._PdctQty = value if value is not None else base_types.UninitialisedField(self, 'PdctQty', DecimalNumber, False)

	@PdctQty.deleter
	def PdctQty(self):
		del self._PdctQty
		self._PdctQty = base_types.UninitialisedField(self, 'PdctQty', DecimalNumber, False)

	@property
	def SaleChanl(self):
		return self._SaleChanl

	@SaleChanl.setter
	def SaleChanl(self, value):
		self._SaleChanl = value if value is not None else base_types.UninitialisedField(self, 'SaleChanl', Max70Text, False)

	@SaleChanl.deleter
	def SaleChanl(self):
		del self._SaleChanl
		self._SaleChanl = base_types.UninitialisedField(self, 'SaleChanl', Max70Text, False)

	@property
	def TaxTp(self):
		return self._TaxTp

	@TaxTp.setter
	def TaxTp(self, value):
		self._TaxTp = value if value is not None else base_types.UninitialisedField(self, 'TaxTp', Max35Text, False)

	@TaxTp.deleter
	def TaxTp(self):
		del self._TaxTp
		self._TaxTp = base_types.UninitialisedField(self, 'TaxTp', Max35Text, False)

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if value is not None else base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure6Code, False)

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = base_types.UninitialisedField(self, 'UnitOfMeasr', UnitOfMeasure6Code, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', ImpliedCurrencyAndAmount, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', ImpliedCurrencyAndAmount, False)

	@property
	def UnitPricSgn(self):
		return self._UnitPricSgn

	@UnitPricSgn.setter
	def UnitPricSgn(self, value):
		self._UnitPricSgn = value if value is not None else base_types.UninitialisedField(self, 'UnitPricSgn', PlusOrMinusIndicator, False)

	@UnitPricSgn.deleter
	def UnitPricSgn(self):
		del self._UnitPricSgn
		self._UnitPricSgn = base_types.UninitialisedField(self, 'UnitPricSgn', PlusOrMinusIndicator, False)

	@property
	def ValAddedTax(self):
		return self._ValAddedTax

	@ValAddedTax.setter
	def ValAddedTax(self, value):
		self._ValAddedTax = value if value is not None else base_types.UninitialisedField(self, 'ValAddedTax', ImpliedCurrencyAndAmount, False)

	@ValAddedTax.deleter
	def ValAddedTax(self):
		del self._ValAddedTax
		self._ValAddedTax = base_types.UninitialisedField(self, 'ValAddedTax', ImpliedCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlPdctCd', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPdctDesc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryLctn', type=Max10Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrySvc', type=AttendanceContext2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ItmId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctAmt', type=ImpliedCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctAmtSgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctDesc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleChanl', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure6Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPricSgn', type=PlusOrMinusIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValAddedTax', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))