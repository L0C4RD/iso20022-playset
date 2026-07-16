# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Adjustment6
from . import CurrencyAndAmount
from . import InvoiceIdentification1
from . import ReportLine7

class ReportLine6(base_types._BaseFieldType):

	__slots__ = ["_Adjstmnt", "_BrkdwnByPurchsOrdr", "_ComrclDocRef", "_NetAmt"]
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
	def BrkdwnByPurchsOrdr(self):
		return self._BrkdwnByPurchsOrdr

	@BrkdwnByPurchsOrdr.setter
	def BrkdwnByPurchsOrdr(self, value):
		self._BrkdwnByPurchsOrdr = value if value is not None else base_types.UninitialisedField(self, 'BrkdwnByPurchsOrdr', ReportLine7, True)

	@BrkdwnByPurchsOrdr.deleter
	def BrkdwnByPurchsOrdr(self):
		del self._BrkdwnByPurchsOrdr
		self._BrkdwnByPurchsOrdr = base_types.UninitialisedField(self, 'BrkdwnByPurchsOrdr', ReportLine7, True)

	@property
	def ComrclDocRef(self):
		return self._ComrclDocRef

	@ComrclDocRef.setter
	def ComrclDocRef(self, value):
		self._ComrclDocRef = value if value is not None else base_types.UninitialisedField(self, 'ComrclDocRef', InvoiceIdentification1, False)

	@ComrclDocRef.deleter
	def ComrclDocRef(self):
		del self._ComrclDocRef
		self._ComrclDocRef = base_types.UninitialisedField(self, 'ComrclDocRef', InvoiceIdentification1, False)

	@property
	def NetAmt(self):
		return self._NetAmt

	@NetAmt.setter
	def NetAmt(self, value):
		self._NetAmt = value if value is not None else base_types.UninitialisedField(self, 'NetAmt', CurrencyAndAmount, False)

	@NetAmt.deleter
	def NetAmt(self):
		del self._NetAmt
		self._NetAmt = base_types.UninitialisedField(self, 'NetAmt', CurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='BrkdwnByPurchsOrdr', type=ReportLine7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ComrclDocRef', type=InvoiceIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))