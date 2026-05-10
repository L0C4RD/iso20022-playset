from . import base_types
from .DocumentIdentification7 import DocumentIdentification7
from .Adjustment6 import Adjustment6
from .CurrencyAndAmount import CurrencyAndAmount

class ReportLine5(base_types._BaseFieldType):

	__slots__ = ["_Adjstmnt", "_PurchsOrdrRef", "_NetAmt"]
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
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != base_types.auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PurchsOrdrRef', type=DocumentIdentification7, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

