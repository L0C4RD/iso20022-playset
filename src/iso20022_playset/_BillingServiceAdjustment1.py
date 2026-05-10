from . import base_types
from ._ISODate import ISODate
from ._BillingSubServiceIdentification1 import BillingSubServiceIdentification1
from ._AmountAndDirection34 import AmountAndDirection34
from ._DecimalNumber import DecimalNumber
from ._Max35Text import Max35Text
from ._Max140Text import Max140Text
from ._ServiceAdjustmentType1Code import ServiceAdjustmentType1Code

class BillingServiceAdjustment1(base_types._BaseFieldType):

	__slots__ = ["_NewPric", "_NewVol", "_Tp", "_Amt", "_OrgnlVol", "_SubSvc", "_BalReqrdAmt", "_OrgnlPric", "_VolChng", "_OrgnlChrgAmt", "_PricChng", "_Desc", "_AdjstmntId", "_ErrDt", "_NewChrgAmt"]
	@property
	def AdjstmntId(self):
		return self._AdjstmntId

	@AdjstmntId.setter
	def AdjstmntId(self, value):
		self._AdjstmntId = value if type(value) != base_types.auto else self.make_default("AdjstmntId")

	@AdjstmntId.deleter
	def AdjstmntId(self):
		del self._AdjstmntId
		self._AdjstmntId = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def BalReqrdAmt(self):
		return self._BalReqrdAmt

	@BalReqrdAmt.setter
	def BalReqrdAmt(self, value):
		self._BalReqrdAmt = value if type(value) != base_types.auto else self.make_default("BalReqrdAmt")

	@BalReqrdAmt.deleter
	def BalReqrdAmt(self):
		del self._BalReqrdAmt
		self._BalReqrdAmt = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def ErrDt(self):
		return self._ErrDt

	@ErrDt.setter
	def ErrDt(self, value):
		self._ErrDt = value if type(value) != base_types.auto else self.make_default("ErrDt")

	@ErrDt.deleter
	def ErrDt(self):
		del self._ErrDt
		self._ErrDt = None

	@property
	def NewChrgAmt(self):
		return self._NewChrgAmt

	@NewChrgAmt.setter
	def NewChrgAmt(self, value):
		self._NewChrgAmt = value if type(value) != base_types.auto else self.make_default("NewChrgAmt")

	@NewChrgAmt.deleter
	def NewChrgAmt(self):
		del self._NewChrgAmt
		self._NewChrgAmt = None

	@property
	def NewPric(self):
		return self._NewPric

	@NewPric.setter
	def NewPric(self, value):
		self._NewPric = value if type(value) != base_types.auto else self.make_default("NewPric")

	@NewPric.deleter
	def NewPric(self):
		del self._NewPric
		self._NewPric = None

	@property
	def NewVol(self):
		return self._NewVol

	@NewVol.setter
	def NewVol(self, value):
		self._NewVol = value if type(value) != base_types.auto else self.make_default("NewVol")

	@NewVol.deleter
	def NewVol(self):
		del self._NewVol
		self._NewVol = None

	@property
	def OrgnlChrgAmt(self):
		return self._OrgnlChrgAmt

	@OrgnlChrgAmt.setter
	def OrgnlChrgAmt(self, value):
		self._OrgnlChrgAmt = value if type(value) != base_types.auto else self.make_default("OrgnlChrgAmt")

	@OrgnlChrgAmt.deleter
	def OrgnlChrgAmt(self):
		del self._OrgnlChrgAmt
		self._OrgnlChrgAmt = None

	@property
	def OrgnlPric(self):
		return self._OrgnlPric

	@OrgnlPric.setter
	def OrgnlPric(self, value):
		self._OrgnlPric = value if type(value) != base_types.auto else self.make_default("OrgnlPric")

	@OrgnlPric.deleter
	def OrgnlPric(self):
		del self._OrgnlPric
		self._OrgnlPric = None

	@property
	def OrgnlVol(self):
		return self._OrgnlVol

	@OrgnlVol.setter
	def OrgnlVol(self, value):
		self._OrgnlVol = value if type(value) != base_types.auto else self.make_default("OrgnlVol")

	@OrgnlVol.deleter
	def OrgnlVol(self):
		del self._OrgnlVol
		self._OrgnlVol = None

	@property
	def PricChng(self):
		return self._PricChng

	@PricChng.setter
	def PricChng(self, value):
		self._PricChng = value if type(value) != base_types.auto else self.make_default("PricChng")

	@PricChng.deleter
	def PricChng(self):
		del self._PricChng
		self._PricChng = None

	@property
	def SubSvc(self):
		return self._SubSvc

	@SubSvc.setter
	def SubSvc(self, value):
		self._SubSvc = value if type(value) != base_types.auto else self.make_default("SubSvc")

	@SubSvc.deleter
	def SubSvc(self):
		del self._SubSvc
		self._SubSvc = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def VolChng(self):
		return self._VolChng

	@VolChng.setter
	def VolChng(self, value):
		self._VolChng = value if type(value) != base_types.auto else self.make_default("VolChng")

	@VolChng.deleter
	def VolChng(self):
		del self._VolChng
		self._VolChng = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AdjstmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalReqrdAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ErrDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewChrgAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewPric', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewVol', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlChrgAmt', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlPric', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlVol', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricChng', type=AmountAndDirection34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubSvc', type=BillingSubServiceIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ServiceAdjustmentType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VolChng', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

