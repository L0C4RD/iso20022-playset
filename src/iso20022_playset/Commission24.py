from . import base_types
import ISODate
import AmountOrRate2Choice
import AmountAndDirection29
import PartyIdentification117
import CommissionType6Choice
import BaseOneRate
import ActiveCurrencyAndAmount

class Commission24(base_types._BaseFieldType):

	__slots__ = ["_RcptId", "_Comssn", "_Tp", "_TtlVATAmt", "_ClctnDt", "_TtlComssn", "_VATRate"]
	@property
	def RcptId(self):
		return self._RcptId

	@RcptId.setter
	def RcptId(self, value):
		self._RcptId = value if type(value) != auto else self.make_default("RcptId")

	@RcptId.deleter
	def RcptId(self):
		del self._RcptId
		self._RcptId = None

	@property
	def Comssn(self):
		return self._Comssn

	@Comssn.setter
	def Comssn(self, value):
		self._Comssn = value if type(value) != auto else self.make_default("Comssn")

	@Comssn.deleter
	def Comssn(self):
		del self._Comssn
		self._Comssn = None

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
	def TtlVATAmt(self):
		return self._TtlVATAmt

	@TtlVATAmt.setter
	def TtlVATAmt(self, value):
		self._TtlVATAmt = value if type(value) != auto else self.make_default("TtlVATAmt")

	@TtlVATAmt.deleter
	def TtlVATAmt(self):
		del self._TtlVATAmt
		self._TtlVATAmt = None

	@property
	def ClctnDt(self):
		return self._ClctnDt

	@ClctnDt.setter
	def ClctnDt(self, value):
		self._ClctnDt = value if type(value) != auto else self.make_default("ClctnDt")

	@ClctnDt.deleter
	def ClctnDt(self):
		del self._ClctnDt
		self._ClctnDt = None

	@property
	def TtlComssn(self):
		return self._TtlComssn

	@TtlComssn.setter
	def TtlComssn(self, value):
		self._TtlComssn = value if type(value) != auto else self.make_default("TtlComssn")

	@TtlComssn.deleter
	def TtlComssn(self):
		del self._TtlComssn
		self._TtlComssn = None

	@property
	def VATRate(self):
		return self._VATRate

	@VATRate.setter
	def VATRate(self, value):
		self._VATRate = value if type(value) != auto else self.make_default("VATRate")

	@VATRate.deleter
	def VATRate(self):
		del self._VATRate
		self._VATRate = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcptId', type=PartyIdentification117, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Comssn', type=AmountOrRate2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CommissionType6Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlVATAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClctnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TtlComssn', type=AmountAndDirection29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VATRate', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
	))

