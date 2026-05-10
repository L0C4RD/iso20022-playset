import base_types
import FinancialInstrument57
import InvestmentAccount58
import Max350Text
import Fee3
import LegIdentification1Choice

class SwitchLegReferences2(base_types._BaseFieldType):

	__slots__ = ["_LegId", "_LegRjctnRsn", "_InvstmtAcctDtls", "_RprdFee", "_FinInstrmDtls"]
	@property
	def LegId(self):
		return self._LegId

	@LegId.setter
	def LegId(self, value):
		self._LegId = value if type(value) != auto else self.make_default("LegId")

	@LegId.deleter
	def LegId(self):
		del self._LegId
		self._LegId = None

	@property
	def LegRjctnRsn(self):
		return self._LegRjctnRsn

	@LegRjctnRsn.setter
	def LegRjctnRsn(self, value):
		self._LegRjctnRsn = value if type(value) != auto else self.make_default("LegRjctnRsn")

	@LegRjctnRsn.deleter
	def LegRjctnRsn(self):
		del self._LegRjctnRsn
		self._LegRjctnRsn = None

	@property
	def InvstmtAcctDtls(self):
		return self._InvstmtAcctDtls

	@InvstmtAcctDtls.setter
	def InvstmtAcctDtls(self, value):
		self._InvstmtAcctDtls = value if type(value) != auto else self.make_default("InvstmtAcctDtls")

	@InvstmtAcctDtls.deleter
	def InvstmtAcctDtls(self):
		del self._InvstmtAcctDtls
		self._InvstmtAcctDtls = None

	@property
	def RprdFee(self):
		return self._RprdFee

	@RprdFee.setter
	def RprdFee(self, value):
		self._RprdFee = value if type(value) != auto else self.make_default("RprdFee")

	@RprdFee.deleter
	def RprdFee(self):
		del self._RprdFee
		self._RprdFee = None

	@property
	def FinInstrmDtls(self):
		return self._FinInstrmDtls

	@FinInstrmDtls.setter
	def FinInstrmDtls(self, value):
		self._FinInstrmDtls = value if type(value) != auto else self.make_default("FinInstrmDtls")

	@FinInstrmDtls.deleter
	def FinInstrmDtls(self):
		del self._FinInstrmDtls
		self._FinInstrmDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LegId', type=LegIdentification1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LegRjctnRsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstmtAcctDtls', type=InvestmentAccount58, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RprdFee', type=Fee3, min=0, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmDtls', type=FinancialInstrument57, min=0, max=1, mutex_group=None, array=False),
	))

