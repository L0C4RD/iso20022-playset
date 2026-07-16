# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Adjustment6
from . import Charge25
from . import CurrencyAndAmount
from . import DocumentIdentification7
from . import Incoterms4
from . import LineItemDetails14
from . import Tax22
from . import UserDefinedInformation1
from . import YesNoIndicator

class LineItem15(base_types._BaseFieldType):

	__slots__ = ["_Adjstmnt", "_BuyrDfndInf", "_ComrclLineItms", "_FnlSubmissn", "_FrghtChrgs", "_Incotrms", "_LineItmsTtlAmt", "_PurchsOrdrRef", "_SellrDfndInf", "_Tax", "_TtlNetAmt"]
	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if value is not None else base_types.UninitialisedField(self, 'Adjstmnt', Adjustment6, True)

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = base_types.UninitialisedField(self, 'Adjstmnt', Adjustment6, True)

	@property
	def BuyrDfndInf(self):
		return self._BuyrDfndInf

	@BuyrDfndInf.setter
	def BuyrDfndInf(self, value):
		self._BuyrDfndInf = value if value is not None else base_types.UninitialisedField(self, 'BuyrDfndInf', UserDefinedInformation1, True)

	@BuyrDfndInf.deleter
	def BuyrDfndInf(self):
		del self._BuyrDfndInf
		self._BuyrDfndInf = base_types.UninitialisedField(self, 'BuyrDfndInf', UserDefinedInformation1, True)

	@property
	def ComrclLineItms(self):
		return self._ComrclLineItms

	@ComrclLineItms.setter
	def ComrclLineItms(self, value):
		self._ComrclLineItms = value if value is not None else base_types.UninitialisedField(self, 'ComrclLineItms', LineItemDetails14, True)

	@ComrclLineItms.deleter
	def ComrclLineItms(self):
		del self._ComrclLineItms
		self._ComrclLineItms = base_types.UninitialisedField(self, 'ComrclLineItms', LineItemDetails14, True)

	@property
	def FnlSubmissn(self):
		return self._FnlSubmissn

	@FnlSubmissn.setter
	def FnlSubmissn(self, value):
		self._FnlSubmissn = value if value is not None else base_types.UninitialisedField(self, 'FnlSubmissn', YesNoIndicator, False)

	@FnlSubmissn.deleter
	def FnlSubmissn(self):
		del self._FnlSubmissn
		self._FnlSubmissn = base_types.UninitialisedField(self, 'FnlSubmissn', YesNoIndicator, False)

	@property
	def FrghtChrgs(self):
		return self._FrghtChrgs

	@FrghtChrgs.setter
	def FrghtChrgs(self, value):
		self._FrghtChrgs = value if value is not None else base_types.UninitialisedField(self, 'FrghtChrgs', Charge25, False)

	@FrghtChrgs.deleter
	def FrghtChrgs(self):
		del self._FrghtChrgs
		self._FrghtChrgs = base_types.UninitialisedField(self, 'FrghtChrgs', Charge25, False)

	@property
	def Incotrms(self):
		return self._Incotrms

	@Incotrms.setter
	def Incotrms(self, value):
		self._Incotrms = value if value is not None else base_types.UninitialisedField(self, 'Incotrms', Incoterms4, False)

	@Incotrms.deleter
	def Incotrms(self):
		del self._Incotrms
		self._Incotrms = base_types.UninitialisedField(self, 'Incotrms', Incoterms4, False)

	@property
	def LineItmsTtlAmt(self):
		return self._LineItmsTtlAmt

	@LineItmsTtlAmt.setter
	def LineItmsTtlAmt(self, value):
		self._LineItmsTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'LineItmsTtlAmt', CurrencyAndAmount, False)

	@LineItmsTtlAmt.deleter
	def LineItmsTtlAmt(self):
		del self._LineItmsTtlAmt
		self._LineItmsTtlAmt = base_types.UninitialisedField(self, 'LineItmsTtlAmt', CurrencyAndAmount, False)

	@property
	def PurchsOrdrRef(self):
		return self._PurchsOrdrRef

	@PurchsOrdrRef.setter
	def PurchsOrdrRef(self, value):
		self._PurchsOrdrRef = value if value is not None else base_types.UninitialisedField(self, 'PurchsOrdrRef', DocumentIdentification7, False)

	@PurchsOrdrRef.deleter
	def PurchsOrdrRef(self):
		del self._PurchsOrdrRef
		self._PurchsOrdrRef = base_types.UninitialisedField(self, 'PurchsOrdrRef', DocumentIdentification7, False)

	@property
	def SellrDfndInf(self):
		return self._SellrDfndInf

	@SellrDfndInf.setter
	def SellrDfndInf(self, value):
		self._SellrDfndInf = value if value is not None else base_types.UninitialisedField(self, 'SellrDfndInf', UserDefinedInformation1, True)

	@SellrDfndInf.deleter
	def SellrDfndInf(self):
		del self._SellrDfndInf
		self._SellrDfndInf = base_types.UninitialisedField(self, 'SellrDfndInf', UserDefinedInformation1, True)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax22, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax22, True)

	@property
	def TtlNetAmt(self):
		return self._TtlNetAmt

	@TtlNetAmt.setter
	def TtlNetAmt(self, value):
		self._TtlNetAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlNetAmt', CurrencyAndAmount, False)

	@TtlNetAmt.deleter
	def TtlNetAmt(self):
		del self._TtlNetAmt
		self._TtlNetAmt = base_types.UninitialisedField(self, 'TtlNetAmt', CurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BuyrDfndInf', type=UserDefinedInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComrclLineItms', type=LineItemDetails14, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FnlSubmissn', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrghtChrgs', type=Charge25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Incotrms', type=Incoterms4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SellrDfndInf', type=UserDefinedInformation1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tax', type=Tax22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))