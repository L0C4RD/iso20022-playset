from . import base_types
from ._DecimalNumber import DecimalNumber
from ._Max10Text import Max10Text
from ._Max256Text import Max256Text
from ._PlusOrMinusIndicator import PlusOrMinusIndicator
from ._UnitOfMeasure6Code import UnitOfMeasure6Code
from ._Max35Text import Max35Text
from ._ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from ._Max70Text import Max70Text
from ._Max140Text import Max140Text
from ._AttendanceContext2Code import AttendanceContext2Code

class Product6(base_types._BaseFieldType):

	__slots__ = ["_ItmId", "_TaxTp", "_PdctAmt", "_UnitOfMeasr", "_PdctAmtSgn", "_PdctQty", "_AddtlPdctDesc", "_SaleChanl", "_UnitPricSgn", "_DlvrySvc", "_AddtlPdctCd", "_DlvryLctn", "_PdctDesc", "_PdctCd", "_ValAddedTax", "_UnitPric"]
	@property
	def AddtlPdctCd(self):
		return self._AddtlPdctCd

	@AddtlPdctCd.setter
	def AddtlPdctCd(self, value):
		self._AddtlPdctCd = value if type(value) != base_types.auto else self.make_default("AddtlPdctCd")

	@AddtlPdctCd.deleter
	def AddtlPdctCd(self):
		del self._AddtlPdctCd
		self._AddtlPdctCd = None

	@property
	def AddtlPdctDesc(self):
		return self._AddtlPdctDesc

	@AddtlPdctDesc.setter
	def AddtlPdctDesc(self, value):
		self._AddtlPdctDesc = value if type(value) != base_types.auto else self.make_default("AddtlPdctDesc")

	@AddtlPdctDesc.deleter
	def AddtlPdctDesc(self):
		del self._AddtlPdctDesc
		self._AddtlPdctDesc = None

	@property
	def DlvryLctn(self):
		return self._DlvryLctn

	@DlvryLctn.setter
	def DlvryLctn(self, value):
		self._DlvryLctn = value if type(value) != base_types.auto else self.make_default("DlvryLctn")

	@DlvryLctn.deleter
	def DlvryLctn(self):
		del self._DlvryLctn
		self._DlvryLctn = None

	@property
	def DlvrySvc(self):
		return self._DlvrySvc

	@DlvrySvc.setter
	def DlvrySvc(self, value):
		self._DlvrySvc = value if type(value) != base_types.auto else self.make_default("DlvrySvc")

	@DlvrySvc.deleter
	def DlvrySvc(self):
		del self._DlvrySvc
		self._DlvrySvc = None

	@property
	def ItmId(self):
		return self._ItmId

	@ItmId.setter
	def ItmId(self, value):
		self._ItmId = value if type(value) != base_types.auto else self.make_default("ItmId")

	@ItmId.deleter
	def ItmId(self):
		del self._ItmId
		self._ItmId = None

	@property
	def PdctAmt(self):
		return self._PdctAmt

	@PdctAmt.setter
	def PdctAmt(self, value):
		self._PdctAmt = value if type(value) != base_types.auto else self.make_default("PdctAmt")

	@PdctAmt.deleter
	def PdctAmt(self):
		del self._PdctAmt
		self._PdctAmt = None

	@property
	def PdctAmtSgn(self):
		return self._PdctAmtSgn

	@PdctAmtSgn.setter
	def PdctAmtSgn(self, value):
		self._PdctAmtSgn = value if type(value) != base_types.auto else self.make_default("PdctAmtSgn")

	@PdctAmtSgn.deleter
	def PdctAmtSgn(self):
		del self._PdctAmtSgn
		self._PdctAmtSgn = None

	@property
	def PdctCd(self):
		return self._PdctCd

	@PdctCd.setter
	def PdctCd(self, value):
		self._PdctCd = value if type(value) != base_types.auto else self.make_default("PdctCd")

	@PdctCd.deleter
	def PdctCd(self):
		del self._PdctCd
		self._PdctCd = None

	@property
	def PdctDesc(self):
		return self._PdctDesc

	@PdctDesc.setter
	def PdctDesc(self, value):
		self._PdctDesc = value if type(value) != base_types.auto else self.make_default("PdctDesc")

	@PdctDesc.deleter
	def PdctDesc(self):
		del self._PdctDesc
		self._PdctDesc = None

	@property
	def PdctQty(self):
		return self._PdctQty

	@PdctQty.setter
	def PdctQty(self, value):
		self._PdctQty = value if type(value) != base_types.auto else self.make_default("PdctQty")

	@PdctQty.deleter
	def PdctQty(self):
		del self._PdctQty
		self._PdctQty = None

	@property
	def SaleChanl(self):
		return self._SaleChanl

	@SaleChanl.setter
	def SaleChanl(self, value):
		self._SaleChanl = value if type(value) != base_types.auto else self.make_default("SaleChanl")

	@SaleChanl.deleter
	def SaleChanl(self):
		del self._SaleChanl
		self._SaleChanl = None

	@property
	def TaxTp(self):
		return self._TaxTp

	@TaxTp.setter
	def TaxTp(self, value):
		self._TaxTp = value if type(value) != base_types.auto else self.make_default("TaxTp")

	@TaxTp.deleter
	def TaxTp(self):
		del self._TaxTp
		self._TaxTp = None

	@property
	def UnitOfMeasr(self):
		return self._UnitOfMeasr

	@UnitOfMeasr.setter
	def UnitOfMeasr(self, value):
		self._UnitOfMeasr = value if type(value) != base_types.auto else self.make_default("UnitOfMeasr")

	@UnitOfMeasr.deleter
	def UnitOfMeasr(self):
		del self._UnitOfMeasr
		self._UnitOfMeasr = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != base_types.auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def UnitPricSgn(self):
		return self._UnitPricSgn

	@UnitPricSgn.setter
	def UnitPricSgn(self, value):
		self._UnitPricSgn = value if type(value) != base_types.auto else self.make_default("UnitPricSgn")

	@UnitPricSgn.deleter
	def UnitPricSgn(self):
		del self._UnitPricSgn
		self._UnitPricSgn = None

	@property
	def ValAddedTax(self):
		return self._ValAddedTax

	@ValAddedTax.setter
	def ValAddedTax(self, value):
		self._ValAddedTax = value if type(value) != base_types.auto else self.make_default("ValAddedTax")

	@ValAddedTax.deleter
	def ValAddedTax(self):
		del self._ValAddedTax
		self._ValAddedTax = None

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

