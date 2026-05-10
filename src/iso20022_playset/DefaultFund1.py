import base_types
import AccountIdentification4Choice
import Contribution1
import ActiveCurrencyAndAmount

class DefaultFund1(base_types._BaseFieldType):

	__slots__ = ["_TtlDfltFndAmt", "_DfltFndAcct", "_IncrCvrgAmt", "_Cntrbtn"]
	@property
	def TtlDfltFndAmt(self):
		return self._TtlDfltFndAmt

	@TtlDfltFndAmt.setter
	def TtlDfltFndAmt(self, value):
		self._TtlDfltFndAmt = value if type(value) != auto else self.make_default("TtlDfltFndAmt")

	@TtlDfltFndAmt.deleter
	def TtlDfltFndAmt(self):
		del self._TtlDfltFndAmt
		self._TtlDfltFndAmt = None

	@property
	def DfltFndAcct(self):
		return self._DfltFndAcct

	@DfltFndAcct.setter
	def DfltFndAcct(self, value):
		self._DfltFndAcct = value if type(value) != auto else self.make_default("DfltFndAcct")

	@DfltFndAcct.deleter
	def DfltFndAcct(self):
		del self._DfltFndAcct
		self._DfltFndAcct = None

	@property
	def IncrCvrgAmt(self):
		return self._IncrCvrgAmt

	@IncrCvrgAmt.setter
	def IncrCvrgAmt(self, value):
		self._IncrCvrgAmt = value if type(value) != auto else self.make_default("IncrCvrgAmt")

	@IncrCvrgAmt.deleter
	def IncrCvrgAmt(self):
		del self._IncrCvrgAmt
		self._IncrCvrgAmt = None

	@property
	def Cntrbtn(self):
		return self._Cntrbtn

	@Cntrbtn.setter
	def Cntrbtn(self, value):
		self._Cntrbtn = value if type(value) != auto else self.make_default("Cntrbtn")

	@Cntrbtn.deleter
	def Cntrbtn(self):
		del self._Cntrbtn
		self._Cntrbtn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TtlDfltFndAmt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DfltFndAcct', type=AccountIdentification4Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IncrCvrgAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cntrbtn', type=Contribution1, min=0, max=None, mutex_group=None, array=True),
	))

