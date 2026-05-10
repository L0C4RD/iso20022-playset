from . import base_types
import DateAndDateTimeChoice
import CashAccount19
import Max35Text
import ActiveCurrencyAndAmount

class CorporateActionCashMovements2(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_PstngId", "_PstngAmt", "_PstngDtTm"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def PstngId(self):
		return self._PstngId

	@PstngId.setter
	def PstngId(self, value):
		self._PstngId = value if type(value) != auto else self.make_default("PstngId")

	@PstngId.deleter
	def PstngId(self):
		del self._PstngId
		self._PstngId = None

	@property
	def PstngAmt(self):
		return self._PstngAmt

	@PstngAmt.setter
	def PstngAmt(self, value):
		self._PstngAmt = value if type(value) != auto else self.make_default("PstngAmt")

	@PstngAmt.deleter
	def PstngAmt(self):
		del self._PstngAmt
		self._PstngAmt = None

	@property
	def PstngDtTm(self):
		return self._PstngDtTm

	@PstngDtTm.setter
	def PstngDtTm(self, value):
		self._PstngDtTm = value if type(value) != auto else self.make_default("PstngDtTm")

	@PstngDtTm.deleter
	def PstngDtTm(self):
		del self._PstngDtTm
		self._PstngDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=CashAccount19, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
	))

