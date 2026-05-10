from . import base_types
from .ISODate import ISODate
from .Max99Text import Max99Text
from .TrueFalseIndicator import TrueFalseIndicator
from .Max256Text import Max256Text
from .ImpliedCurrencyAndAmount import ImpliedCurrencyAndAmount
from .Max70Text import Max70Text
from .ISO3NumericCurrencyCode import ISO3NumericCurrencyCode
from .CreditDebit3Code import CreditDebit3Code

class AccountStatementDetails3(base_types._BaseFieldType):

	__slots__ = ["_AccptrNmAndLctn", "_Amt", "_Ccy", "_CrdhldrBllgAmt", "_CrdhldrBllgCcy", "_CdtDbt", "_ShrtDesc", "_PstngDt", "_Pdg", "_LngDesc", "_TxDt"]
	@property
	def AccptrNmAndLctn(self):
		return self._AccptrNmAndLctn

	@AccptrNmAndLctn.setter
	def AccptrNmAndLctn(self, value):
		self._AccptrNmAndLctn = value if type(value) != base_types.auto else self.make_default("AccptrNmAndLctn")

	@AccptrNmAndLctn.deleter
	def AccptrNmAndLctn(self):
		del self._AccptrNmAndLctn
		self._AccptrNmAndLctn = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != base_types.auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def CrdhldrBllgAmt(self):
		return self._CrdhldrBllgAmt

	@CrdhldrBllgAmt.setter
	def CrdhldrBllgAmt(self, value):
		self._CrdhldrBllgAmt = value if type(value) != base_types.auto else self.make_default("CrdhldrBllgAmt")

	@CrdhldrBllgAmt.deleter
	def CrdhldrBllgAmt(self):
		del self._CrdhldrBllgAmt
		self._CrdhldrBllgAmt = None

	@property
	def CrdhldrBllgCcy(self):
		return self._CrdhldrBllgCcy

	@CrdhldrBllgCcy.setter
	def CrdhldrBllgCcy(self, value):
		self._CrdhldrBllgCcy = value if type(value) != base_types.auto else self.make_default("CrdhldrBllgCcy")

	@CrdhldrBllgCcy.deleter
	def CrdhldrBllgCcy(self):
		del self._CrdhldrBllgCcy
		self._CrdhldrBllgCcy = None

	@property
	def CdtDbt(self):
		return self._CdtDbt

	@CdtDbt.setter
	def CdtDbt(self, value):
		self._CdtDbt = value if type(value) != base_types.auto else self.make_default("CdtDbt")

	@CdtDbt.deleter
	def CdtDbt(self):
		del self._CdtDbt
		self._CdtDbt = None

	@property
	def ShrtDesc(self):
		return self._ShrtDesc

	@ShrtDesc.setter
	def ShrtDesc(self, value):
		self._ShrtDesc = value if type(value) != base_types.auto else self.make_default("ShrtDesc")

	@ShrtDesc.deleter
	def ShrtDesc(self):
		del self._ShrtDesc
		self._ShrtDesc = None

	@property
	def PstngDt(self):
		return self._PstngDt

	@PstngDt.setter
	def PstngDt(self, value):
		self._PstngDt = value if type(value) != base_types.auto else self.make_default("PstngDt")

	@PstngDt.deleter
	def PstngDt(self):
		del self._PstngDt
		self._PstngDt = None

	@property
	def Pdg(self):
		return self._Pdg

	@Pdg.setter
	def Pdg(self, value):
		self._Pdg = value if type(value) != base_types.auto else self.make_default("Pdg")

	@Pdg.deleter
	def Pdg(self):
		del self._Pdg
		self._Pdg = None

	@property
	def LngDesc(self):
		return self._LngDesc

	@LngDesc.setter
	def LngDesc(self, value):
		self._LngDesc = value if type(value) != base_types.auto else self.make_default("LngDesc")

	@LngDesc.deleter
	def LngDesc(self):
		del self._LngDesc
		self._LngDesc = None

	@property
	def TxDt(self):
		return self._TxDt

	@TxDt.setter
	def TxDt(self, value):
		self._TxDt = value if type(value) != base_types.auto else self.make_default("TxDt")

	@TxDt.deleter
	def TxDt(self):
		del self._TxDt
		self._TxDt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptrNmAndLctn', type=Max99Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrdhldrBllgCcy', type=ISO3NumericCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtDbt', type=CreditDebit3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtDesc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pdg', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LngDesc', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
	))

