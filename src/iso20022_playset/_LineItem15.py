from . import base_types
from .Incoterms4 import Incoterms4
from .DocumentIdentification7 import DocumentIdentification7
from .LineItemDetails14 import LineItemDetails14
from .CurrencyAndAmount import CurrencyAndAmount
from .Tax22 import Tax22
from .Charge25 import Charge25
from .Adjustment6 import Adjustment6
from .YesNoIndicator import YesNoIndicator
from .UserDefinedInformation1 import UserDefinedInformation1

class LineItem15(base_types._BaseFieldType):

	__slots__ = ["_FrghtChrgs", "_BuyrDfndInf", "_PurchsOrdrRef", "_ComrclLineItms", "_Tax", "_SellrDfndInf", "_TtlNetAmt", "_LineItmsTtlAmt", "_FnlSubmissn", "_Incotrms", "_Adjstmnt"]
	@property
	def FrghtChrgs(self):
		return self._FrghtChrgs

	@FrghtChrgs.setter
	def FrghtChrgs(self, value):
		self._FrghtChrgs = value if type(value) != base_types.auto else self.make_default("FrghtChrgs")

	@FrghtChrgs.deleter
	def FrghtChrgs(self):
		del self._FrghtChrgs
		self._FrghtChrgs = None

	@property
	def BuyrDfndInf(self):
		return self._BuyrDfndInf

	@BuyrDfndInf.setter
	def BuyrDfndInf(self, value):
		self._BuyrDfndInf = value if type(value) != base_types.auto else self.make_default("BuyrDfndInf")

	@BuyrDfndInf.deleter
	def BuyrDfndInf(self):
		del self._BuyrDfndInf
		self._BuyrDfndInf = None

	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if type(value) != base_types.auto else self.make_default("PurchsOrdrRef")

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = None

	@property
	def ComrclLineItms(self):
		return self._ComrclLineItms

	@ComrclLineItms.setter
	def ComrclLineItms(self, value):
		self._ComrclLineItms = value if type(value) != base_types.auto else self.make_default("ComrclLineItms")

	@ComrclLineItms.deleter
	def ComrclLineItms(self):
		del self._ComrclLineItms
		self._ComrclLineItms = None

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if type(value) != base_types.auto else self.make_default("Tax")

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = None

	@property
	def SellrDfndInf(self):
		return self._SellrDfndInf

	@SellrDfndInf.setter
	def SellrDfndInf(self, value):
		self._SellrDfndInf = value if type(value) != base_types.auto else self.make_default("SellrDfndInf")

	@SellrDfndInf.deleter
	def SellrDfndInf(self):
		del self._SellrDfndInf
		self._SellrDfndInf = None

	@property
	def TtlNetAmt(self):
		return self._TtlNetAmt

	@TtlNetAmt.setter
	def TtlNetAmt(self, value):
		self._TtlNetAmt = value if type(value) != base_types.auto else self.make_default("TtlNetAmt")

	@TtlNetAmt.deleter
	def TtlNetAmt(self):
		del self._TtlNetAmt
		self._TtlNetAmt = None

	@property
	def LineItmsTtlAmt(self):
		return self._LineItmsTtlAmt

	@LineItmsTtlAmt.setter
	def LineItmsTtlAmt(self, value):
		self._LineItmsTtlAmt = value if type(value) != base_types.auto else self.make_default("LineItmsTtlAmt")

	@LineItmsTtlAmt.deleter
	def LineItmsTtlAmt(self):
		del self._LineItmsTtlAmt
		self._LineItmsTtlAmt = None

	@property
	def FnlSubmissn(self):
		return self._FnlSubmissn

	@FnlSubmissn.setter
	def FnlSubmissn(self, value):
		self._FnlSubmissn = value if type(value) != base_types.auto else self.make_default("FnlSubmissn")

	@FnlSubmissn.deleter
	def FnlSubmissn(self):
		del self._FnlSubmissn
		self._FnlSubmissn = None

	@property
	def Incotrms(self):
		return self._Incotrms

	@Incotrms.setter
	def Incotrms(self, value):
		self._Incotrms = value if type(value) != base_types.auto else self.make_default("Incotrms")

	@Incotrms.deleter
	def Incotrms(self):
		del self._Incotrms
		self._Incotrms = None

	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if type(value) != base_types.auto else self.make_default("Adjstmnt")

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FrghtChrgs', type=Charge25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyrDfndInf', type=UserDefinedInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComrclLineItms', type=LineItemDetails14, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tax', type=Tax22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SellrDfndInf', type=UserDefinedInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlSubmissn', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incotrms', type=Incoterms4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment6, min=0, max=None, mutex_group=None, array=True),
	))

