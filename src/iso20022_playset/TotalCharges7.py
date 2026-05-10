import base_types
import CreditDebitCode
import Max15NumericText
import DecimalNumber
import ActiveCurrencyAndAmount

class TotalCharges7(base_types._BaseFieldType):

	__slots__ = ["_NbOfChrgsRcrds", "_TtlChrgsAmt", "_CtrlSum", "_CdtDbtInd"]
	@property
	def NbOfChrgsRcrds(self):
		return self._NbOfChrgsRcrds

	@NbOfChrgsRcrds.setter
	def NbOfChrgsRcrds(self, value):
		self._NbOfChrgsRcrds = value if type(value) != auto else self.make_default("NbOfChrgsRcrds")

	@NbOfChrgsRcrds.deleter
	def NbOfChrgsRcrds(self):
		del self._NbOfChrgsRcrds
		self._NbOfChrgsRcrds = None

	@property
	def TtlChrgsAmt(self):
		return self._TtlChrgsAmt

	@TtlChrgsAmt.setter
	def TtlChrgsAmt(self, value):
		self._TtlChrgsAmt = value if type(value) != auto else self.make_default("TtlChrgsAmt")

	@TtlChrgsAmt.deleter
	def TtlChrgsAmt(self):
		del self._TtlChrgsAmt
		self._TtlChrgsAmt = None

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if type(value) != auto else self.make_default("CtrlSum")

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = None

	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if type(value) != auto else self.make_default("CdtDbtInd")

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NbOfChrgsRcrds', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlChrgsAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
	))

