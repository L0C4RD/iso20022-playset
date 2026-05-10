from . import base_types
from .Max35Text import Max35Text
from .UnitOfMeasure1Code import UnitOfMeasure1Code
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .DecimalNumber import DecimalNumber
from .Max70Text import Max70Text

class Product2(base_types._BaseFieldType):

	__slots__ = ["_PdctAmt", "_PdctCd", "_PdctQty", "_UnitPric", "_UnitOfMeasr", "_TaxTp", "_AddtlPdctInf"]
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
	def AddtlPdctInf(self):
		return self._AddtlPdctInf

	@AddtlPdctInf.setter
	def AddtlPdctInf(self, value):
		self._AddtlPdctInf = value if type(value) != base_types.auto else self.make_default("AddtlPdctInf")

	@AddtlPdctInf.deleter
	def AddtlPdctInf(self):
		del self._AddtlPdctInf
		self._AddtlPdctInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PdctAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctCd', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctQty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitOfMeasr', type=UnitOfMeasure1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlPdctInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

