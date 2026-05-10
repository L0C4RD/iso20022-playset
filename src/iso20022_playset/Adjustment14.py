import base_types
import TrueFalseIndicator
import ImpliedCurrencyAndAmount
import Max35Text
import DecimalNumber
import PercentageRate
import Max70Text

class Adjustment14(base_types._BaseFieldType):

	__slots__ = ["_PrmtnElgblty", "_UnitPric", "_AddtlTp", "_TaxOnOrgnlAmt", "_Rsn", "_PrmtnCd", "_Tp", "_Desc", "_PrmtnCpnNb", "_Qty", "_Pctg", "_Amt"]
	@property
	def PrmtnElgblty(self):
		return self._PrmtnElgblty

	@PrmtnElgblty.setter
	def PrmtnElgblty(self, value):
		self._PrmtnElgblty = value if type(value) != auto else self.make_default("PrmtnElgblty")

	@PrmtnElgblty.deleter
	def PrmtnElgblty(self):
		del self._PrmtnElgblty
		self._PrmtnElgblty = None

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if type(value) != auto else self.make_default("UnitPric")

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = None

	@property
	def AddtlTp(self):
		return self._AddtlTp

	@AddtlTp.setter
	def AddtlTp(self, value):
		self._AddtlTp = value if type(value) != auto else self.make_default("AddtlTp")

	@AddtlTp.deleter
	def AddtlTp(self):
		del self._AddtlTp
		self._AddtlTp = None

	@property
	def TaxOnOrgnlAmt(self):
		return self._TaxOnOrgnlAmt

	@TaxOnOrgnlAmt.setter
	def TaxOnOrgnlAmt(self, value):
		self._TaxOnOrgnlAmt = value if type(value) != auto else self.make_default("TaxOnOrgnlAmt")

	@TaxOnOrgnlAmt.deleter
	def TaxOnOrgnlAmt(self):
		del self._TaxOnOrgnlAmt
		self._TaxOnOrgnlAmt = None

	@property
	def Rsn(self):
		return self._Rsn

	@Rsn.setter
	def Rsn(self, value):
		self._Rsn = value if type(value) != auto else self.make_default("Rsn")

	@Rsn.deleter
	def Rsn(self):
		del self._Rsn
		self._Rsn = None

	@property
	def PrmtnCd(self):
		return self._PrmtnCd

	@PrmtnCd.setter
	def PrmtnCd(self, value):
		self._PrmtnCd = value if type(value) != auto else self.make_default("PrmtnCd")

	@PrmtnCd.deleter
	def PrmtnCd(self):
		del self._PrmtnCd
		self._PrmtnCd = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	@property
	def PrmtnCpnNb(self):
		return self._PrmtnCpnNb

	@PrmtnCpnNb.setter
	def PrmtnCpnNb(self, value):
		self._PrmtnCpnNb = value if type(value) != auto else self.make_default("PrmtnCpnNb")

	@PrmtnCpnNb.deleter
	def PrmtnCpnNb(self):
		del self._PrmtnCpnNb
		self._PrmtnCpnNb = None

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if type(value) != auto else self.make_default("Qty")

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = None

	@property
	def Pctg(self):
		return self._Pctg

	@Pctg.setter
	def Pctg(self, value):
		self._Pctg = value if type(value) != auto else self.make_default("Pctg")

	@Pctg.deleter
	def Pctg(self):
		del self._Pctg
		self._Pctg = None

	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrmtnElgblty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxOnOrgnlAmt', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rsn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmtnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrmtnCpnNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Pctg', type=PercentageRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Amt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
	))

