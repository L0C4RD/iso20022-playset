# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection34
from . import BillingMethod4
from . import BillingTaxIdentification3
from . import ISODate
from . import Max40Text

class BillingTaxRegion3(base_types._BaseFieldType):

	__slots__ = ["_CstmrTaxId", "_InvcNb", "_MtdC", "_PtDt", "_RgnNb", "_RgnNm", "_SndgFI", "_SttlmAmt", "_TaxDueToRgn"]
	@property
	def CstmrTaxId(self):
		return self._CstmrTaxId

	@CstmrTaxId.setter
	def CstmrTaxId(self, value):
		self._CstmrTaxId = value if value is not None else base_types.UninitialisedField(self, 'CstmrTaxId', Max40Text, False)

	@CstmrTaxId.deleter
	def CstmrTaxId(self):
		del self._CstmrTaxId
		self._CstmrTaxId = base_types.UninitialisedField(self, 'CstmrTaxId', Max40Text, False)

	@property
	def InvcNb(self):
		return self._InvcNb

	@InvcNb.setter
	def InvcNb(self, value):
		self._InvcNb = value if value is not None else base_types.UninitialisedField(self, 'InvcNb', Max40Text, False)

	@InvcNb.deleter
	def InvcNb(self):
		del self._InvcNb
		self._InvcNb = base_types.UninitialisedField(self, 'InvcNb', Max40Text, False)

	@property
	def MtdC(self):
		return self._MtdC

	@MtdC.setter
	def MtdC(self, value):
		self._MtdC = value if value is not None else base_types.UninitialisedField(self, 'MtdC', BillingMethod4, False)

	@MtdC.deleter
	def MtdC(self):
		del self._MtdC
		self._MtdC = base_types.UninitialisedField(self, 'MtdC', BillingMethod4, False)

	@property
	def PtDt(self):
		return self._PtDt

	@PtDt.setter
	def PtDt(self, value):
		self._PtDt = value if value is not None else base_types.UninitialisedField(self, 'PtDt', ISODate, False)

	@PtDt.deleter
	def PtDt(self):
		del self._PtDt
		self._PtDt = base_types.UninitialisedField(self, 'PtDt', ISODate, False)

	@property
	def RgnNb(self):
		return self._RgnNb

	@RgnNb.setter
	def RgnNb(self, value):
		self._RgnNb = value if value is not None else base_types.UninitialisedField(self, 'RgnNb', Max40Text, False)

	@RgnNb.deleter
	def RgnNb(self):
		del self._RgnNb
		self._RgnNb = base_types.UninitialisedField(self, 'RgnNb', Max40Text, False)

	@property
	def RgnNm(self):
		return self._RgnNm

	@RgnNm.setter
	def RgnNm(self, value):
		self._RgnNm = value if value is not None else base_types.UninitialisedField(self, 'RgnNm', Max40Text, False)

	@RgnNm.deleter
	def RgnNm(self):
		del self._RgnNm
		self._RgnNm = base_types.UninitialisedField(self, 'RgnNm', Max40Text, False)

	@property
	def SndgFI(self):
		return self._SndgFI

	@SndgFI.setter
	def SndgFI(self, value):
		self._SndgFI = value if value is not None else base_types.UninitialisedField(self, 'SndgFI', BillingTaxIdentification3, False)

	@SndgFI.deleter
	def SndgFI(self):
		del self._SndgFI
		self._SndgFI = base_types.UninitialisedField(self, 'SndgFI', BillingTaxIdentification3, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection34, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', AmountAndDirection34, False)

	@property
	def TaxDueToRgn(self):
		return self._TaxDueToRgn

	@TaxDueToRgn.setter
	def TaxDueToRgn(self, value):
		self._TaxDueToRgn = value if value is not None else base_types.UninitialisedField(self, 'TaxDueToRgn', AmountAndDirection34, False)

	@TaxDueToRgn.deleter
	def TaxDueToRgn(self):
		del self._TaxDueToRgn
		self._TaxDueToRgn = base_types.UninitialisedField(self, 'TaxDueToRgn', AmountAndDirection34, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CstmrTaxId', type=Max40Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvcNb', type=Max40Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtdC', type=BillingMethod4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgnNb', type=Max40Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgnNm', type=Max40Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SndgFI', type=BillingTaxIdentification3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxDueToRgn', type=AmountAndDirection34, min=1, max=1, mutex_group=None, array=False),
	))