# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CreditDebit3Code
from . import ISO3NumericCurrencyCode
from . import ISODate
from . import ImpliedCurrencyAndAmount
from . import Max256Text
from . import Max70Text
from . import Max99Text
from . import TrueFalseIndicator

class AccountStatementDetails3(base_types._BaseFieldType):

	__slots__ = ["_AccptrNmAndLctn", "_Amt", "_Ccy", "_CdtDbt", "_CrdhldrBllgAmt", "_CrdhldrBllgCcy", "_LngDesc", "_Pdg", "_PstngDt", "_ShrtDesc", "_TxDt"]
	@property
	def AccptrNmAndLctn(self):
		return self._AccptrNmAndLctn

	@AccptrNmAndLctn.setter
	def AccptrNmAndLctn(self, value):
		self._AccptrNmAndLctn = value if value is not None else base_types.UninitialisedField(self, 'AccptrNmAndLctn', Max99Text, False)

	@AccptrNmAndLctn.deleter
	def AccptrNmAndLctn(self):
		del self._AccptrNmAndLctn
		self._AccptrNmAndLctn = base_types.UninitialisedField(self, 'AccptrNmAndLctn', Max99Text, False)

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', ImpliedCurrencyAndAmount, False)

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if value is not None else base_types.UninitialisedField(self, 'Ccy', ISO3NumericCurrencyCode, False)

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = base_types.UninitialisedField(self, 'Ccy', ISO3NumericCurrencyCode, False)

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if value is not None else base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = base_types.UninitialisedField(self, 'CdtDbt', CreditDebit3Code, False)

	@property
	def CrdhldrBllgAmt(self):
		return self._CrdhldrBllgAmt

	@CrdhldrBllgAmt.setter
	def CrdhldrBllgAmt(self, value):
		self._CrdhldrBllgAmt = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrBllgAmt', ImpliedCurrencyAndAmount, False)

	@CrdhldrBllgAmt.deleter
	def CrdhldrBllgAmt(self):
		del self._CrdhldrBllgAmt
		self._CrdhldrBllgAmt = base_types.UninitialisedField(self, 'CrdhldrBllgAmt', ImpliedCurrencyAndAmount, False)

	@property
	def CrdhldrBllgCcy(self):
		return self._CrdhldrBllgCcy

	@CrdhldrBllgCcy.setter
	def CrdhldrBllgCcy(self, value):
		self._CrdhldrBllgCcy = value if value is not None else base_types.UninitialisedField(self, 'CrdhldrBllgCcy', ISO3NumericCurrencyCode, False)

	@CrdhldrBllgCcy.deleter
	def CrdhldrBllgCcy(self):
		del self._CrdhldrBllgCcy
		self._CrdhldrBllgCcy = base_types.UninitialisedField(self, 'CrdhldrBllgCcy', ISO3NumericCurrencyCode, False)

	@property
	def LngDesc(self):
		return self._LngDesc

	@LngDesc.setter
	def LngDesc(self, value):
		self._LngDesc = value if value is not None else base_types.UninitialisedField(self, 'LngDesc', Max256Text, False)

	@LngDesc.deleter
	def LngDesc(self):
		del self._LngDesc
		self._LngDesc = base_types.UninitialisedField(self, 'LngDesc', Max256Text, False)

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if value is not None else base_types.UninitialisedField(self, 'Pdg', TrueFalseIndicator, False)

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = base_types.UninitialisedField(self, 'Pdg', TrueFalseIndicator, False)

	@property
	def PstngDt(self):
		return self._PstngDt

	@PstngDt.setter
	def PstngDt(self, value):
		self._PstngDt = value if value is not None else base_types.UninitialisedField(self, 'PstngDt', ISODate, False)

	@PstngDt.deleter
	def PstngDt(self):
		del self._PstngDt
		self._PstngDt = base_types.UninitialisedField(self, 'PstngDt', ISODate, False)

	@property
	def ShrtDesc(self):
		return self._ShrtDesc

	@ShrtDesc.setter
	def ShrtDesc(self, value):
		self._ShrtDesc = value if value is not None else base_types.UninitialisedField(self, 'ShrtDesc', Max70Text, False)

	@ShrtDesc.deleter
	def ShrtDesc(self):
		del self._ShrtDesc
		self._ShrtDesc = base_types.UninitialisedField(self, 'ShrtDesc', Max70Text, False)

	@property
	def TxDt(self):
		return self._TxDt

	@TxDt.setter
	def TxDt(self, value):
		self._TxDt = value if value is not None else base_types.UninitialisedField(self, 'TxDt', ISODate, False)

	@TxDt.deleter
	def TxDt(self):
		del self._TxDt
		self._TxDt = base_types.UninitialisedField(self, 'TxDt', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptrNmAndLctn', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LngDesc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtDesc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))