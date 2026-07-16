# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import CreditDebitCode
from . import DecimalNumber
from . import Max15NumericText

class TotalCharges7(base_types._BaseFieldType):

	__slots__ = ["_CdtDbtInd", "_CtrlSum", "_NbOfChrgsRcrds", "_TtlChrgsAmt"]
	@property
	def CdtDbtInd(self):
		return self._CdtDbtInd

	@CdtDbtInd.setter
	def CdtDbtInd(self, value):
		self._CdtDbtInd = value if value is not None else base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@CdtDbtInd.deleter
	def CdtDbtInd(self):
		del self._CdtDbtInd
		self._CdtDbtInd = base_types.UninitialisedField(self, 'CdtDbtInd', CreditDebitCode, False)

	@property
	def CtrlSum(self):
		return self._CtrlSum

	@CtrlSum.setter
	def CtrlSum(self, value):
		self._CtrlSum = value if value is not None else base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@CtrlSum.deleter
	def CtrlSum(self):
		del self._CtrlSum
		self._CtrlSum = base_types.UninitialisedField(self, 'CtrlSum', DecimalNumber, False)

	@property
	def NbOfChrgsRcrds(self):
		return self._NbOfChrgsRcrds

	@NbOfChrgsRcrds.setter
	def NbOfChrgsRcrds(self, value):
		self._NbOfChrgsRcrds = value if value is not None else base_types.UninitialisedField(self, 'NbOfChrgsRcrds', Max15NumericText, False)

	@NbOfChrgsRcrds.deleter
	def NbOfChrgsRcrds(self):
		del self._NbOfChrgsRcrds
		self._NbOfChrgsRcrds = base_types.UninitialisedField(self, 'NbOfChrgsRcrds', Max15NumericText, False)

	@property
	def TtlChrgsAmt(self):
		return self._TtlChrgsAmt

	@TtlChrgsAmt.setter
	def TtlChrgsAmt(self, value):
		self._TtlChrgsAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlChrgsAmt', ActiveCurrencyAndAmount, False)

	@TtlChrgsAmt.deleter
	def TtlChrgsAmt(self):
		del self._TtlChrgsAmt
		self._TtlChrgsAmt = base_types.UninitialisedField(self, 'TtlChrgsAmt', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CdtDbtInd', type=CreditDebitCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtrlSum', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfChrgsRcrds', type=Max15NumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlChrgsAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))