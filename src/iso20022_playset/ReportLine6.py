import base_types
import InvoiceIdentification1
import ReportLine7
import CurrencyAndAmount
import Adjustment6

class ReportLine6(base_types._BaseFieldType):

	__slots__ = ["_Adjstmnt", "_ComrclDocRef", "_NetAmt", "_BrkdwnByPurchsOrdr"]
	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if type(value) != auto else self.make_default("Adjstmnt")

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = None

	@property
	def ComrclDocRef(self):
		return self._ComrclDocRef

	@ComrclDocRef.setter
	def ComrclDocRef(self, value):
		self._ComrclDocRef = value if type(value) != auto else self.make_default("ComrclDocRef")

	@ComrclDocRef.deleter
	def ComrclDocRef(self):
		del self._ComrclDocRef
		self._ComrclDocRef = None

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if type(value) != auto else self.make_default("NetAmt")

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = None

	@property
	def BrkdwnByPurchsOrdr(self):
		return self._BrkdwnByPurchsOrdr

	@BrkdwnByPurchsOrdr.setter
	def BrkdwnByPurchsOrdr(self, value):
		self._BrkdwnByPurchsOrdr = value if type(value) != auto else self.make_default("BrkdwnByPurchsOrdr")

	@BrkdwnByPurchsOrdr.deleter
	def BrkdwnByPurchsOrdr(self):
		del self._BrkdwnByPurchsOrdr
		self._BrkdwnByPurchsOrdr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComrclDocRef', type=InvoiceIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BrkdwnByPurchsOrdr', type=ReportLine7, min=1, max=None, mutex_group=None, array=True),
	))

