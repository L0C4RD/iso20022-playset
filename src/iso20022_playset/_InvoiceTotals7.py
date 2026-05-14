# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AccountIdentification4Choice import AccountIdentification4Choice
from ._Adjustment5 import Adjustment5
from ._AmountAndForeignExchange1 import AmountAndForeignExchange1
from ._BillingTaxRecord2 import BillingTaxRecord2
from ._ISODate import ISODate

class InvoiceTotals7(base_types._BaseFieldType):

	__slots__ = ["_Adjstmnt", "_CshAcct", "_PmtDueDt", "_Tax", "_TtlInvcAmt"]
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
	def CshAcct(self):
		return self._CshAcct

	@CshAcct.setter
	def CshAcct(self, value):
		self._CshAcct = value if type(value) != base_types.auto else self.make_default("CshAcct")

	@CshAcct.deleter
	def CshAcct(self):
		del self._CshAcct
		self._CshAcct = None

	@property
	def PmtDueDt(self):
		return self._PmtDueDt

	@PmtDueDt.setter
	def PmtDueDt(self, value):
		self._PmtDueDt = value if type(value) != base_types.auto else self.make_default("PmtDueDt")

	@PmtDueDt.deleter
	def PmtDueDt(self):
		del self._PmtDueDt
		self._PmtDueDt = None

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
	def TtlInvcAmt(self):
		return self._TtlInvcAmt

	@TtlInvcAmt.setter
	def TtlInvcAmt(self, value):
		self._TtlInvcAmt = value if type(value) != base_types.auto else self.make_default("TtlInvcAmt")

	@TtlInvcAmt.deleter
	def TtlInvcAmt(self):
		del self._TtlInvcAmt
		self._TtlInvcAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment5, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshAcct', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDueDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=BillingTaxRecord2, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlInvcAmt', type=AmountAndForeignExchange1, min=1, max=1, mutex_group=None, array=False),
	))