from . import base_types
from .Max40Text import Max40Text
from .ISODate import ISODate
from .BillingMethod4 import BillingMethod4
from .AmountAndDirection34 import AmountAndDirection34
from .BillingTaxIdentification3 import BillingTaxIdentification3

class BillingTaxRegion3(base_types._BaseFieldType):

	__slots__ = ["_PtDt", "_RgnNb", "_RgnNm", "_InvcNb", "_SttlmAmt", "_SndgFI", "_CstmrTaxId", "_MtdC", "_TaxDueToRgn"]
	@property
	def PtDt(self):
		return self._PtDt

	@PtDt.setter
	def PtDt(self, value):
		self._PtDt = value if type(value) != base_types.auto else self.make_default("PtDt")

	@PtDt.deleter
	def PtDt(self):
		del self._PtDt
		self._PtDt = None

	@property
	def RgnNb(self):
		return self._RgnNb

	@RgnNb.setter
	def RgnNb(self, value):
		self._RgnNb = value if type(value) != base_types.auto else self.make_default("RgnNb")

	@RgnNb.deleter
	def RgnNb(self):
		del self._RgnNb
		self._RgnNb = None

	@property
	def RgnNm(self):
		return self._RgnNm

	@RgnNm.setter
	def RgnNm(self, value):
		self._RgnNm = value if type(value) != base_types.auto else self.make_default("RgnNm")

	@RgnNm.deleter
	def RgnNm(self):
		del self._RgnNm
		self._RgnNm = None

	@property
	def InvcNb(self):
		return self._InvcNb

	@InvcNb.setter
	def InvcNb(self, value):
		self._InvcNb = value if type(value) != base_types.auto else self.make_default("InvcNb")

	@InvcNb.deleter
	def InvcNb(self):
		del self._InvcNb
		self._InvcNb = None

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if type(value) != base_types.auto else self.make_default("SttlmAmt")

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = None

	@property
	def SndgFI(self):
		return self._SndgFI

	@SndgFI.setter
	def SndgFI(self, value):
		self._SndgFI = value if type(value) != base_types.auto else self.make_default("SndgFI")

	@SndgFI.deleter
	def SndgFI(self):
		del self._SndgFI
		self._SndgFI = None

	@property
	def CstmrTaxId(self):
		return self._CstmrTaxId

	@CstmrTaxId.setter
	def CstmrTaxId(self, value):
		self._CstmrTaxId = value if type(value) != base_types.auto else self.make_default("CstmrTaxId")

	@CstmrTaxId.deleter
	def CstmrTaxId(self):
		del self._CstmrTaxId
		self._CstmrTaxId = None

	@property
	def MtdC(self):
		return self._MtdC

	@MtdC.setter
	def MtdC(self, value):
		self._MtdC = value if type(value) != base_types.auto else self.make_default("MtdC")

	@MtdC.deleter
	def MtdC(self):
		del self._MtdC
		self._MtdC = None

	@property
	def TaxDueToRgn(self):
		return self._TaxDueToRgn

	@TaxDueToRgn.setter
	def TaxDueToRgn(self, value):
		self._TaxDueToRgn = value if type(value) != base_types.auto else self.make_default("TaxDueToRgn")

	@TaxDueToRgn.deleter
	def TaxDueToRgn(self):
		del self._TaxDueToRgn
		self._TaxDueToRgn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgnNb', type=Max40Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgnNm', type=Max40Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcNb', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndgFI', type=BillingTaxIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrTaxId', type=Max40Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtdC', type=BillingMethod4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxDueToRgn', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))

