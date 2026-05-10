import base_types
import Max70Text
import Restriction1
import ActiveCurrencyCode
import CashAccountType2Choice
import AccountIdentification4Choice
import Max140Text
import ImpliedCurrencyAndAmount
import AccountStatus3Code
import StatementFrequencyAndForm1
import ISODate
import Max5NumericText

class CustomerAccount4(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_FlrNtfctnAmt", "_AcctPurp", "_MnthlyPmtVal", "_Tp", "_Ccy", "_Id", "_StmtFrqcyAndFrmt", "_MnthlyRcvdVal", "_Rstrctn", "_ClsgDt", "_AvrgBal", "_ClngNtfctnAmt", "_MnthlyTxNb", "_Nm"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def FlrNtfctnAmt(self):
		return self._FlrNtfctnAmt

	@FlrNtfctnAmt.setter
	def FlrNtfctnAmt(self, value):
		self._FlrNtfctnAmt = value if type(value) != auto else self.make_default("FlrNtfctnAmt")

	@FlrNtfctnAmt.deleter
	def FlrNtfctnAmt(self):
		del self._FlrNtfctnAmt
		self._FlrNtfctnAmt = None

	@property
	def AcctPurp(self):
		return self._AcctPurp

	@AcctPurp.setter
	def AcctPurp(self, value):
		self._AcctPurp = value if type(value) != auto else self.make_default("AcctPurp")

	@AcctPurp.deleter
	def AcctPurp(self):
		del self._AcctPurp
		self._AcctPurp = None

	@property
	def MnthlyPmtVal(self):
		return self._MnthlyPmtVal

	@MnthlyPmtVal.setter
	def MnthlyPmtVal(self, value):
		self._MnthlyPmtVal = value if type(value) != auto else self.make_default("MnthlyPmtVal")

	@MnthlyPmtVal.deleter
	def MnthlyPmtVal(self):
		del self._MnthlyPmtVal
		self._MnthlyPmtVal = None

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
	def Ccy(self):
		return self._Ccy

	@Ccy.setter
	def Ccy(self, value):
		self._Ccy = value if type(value) != auto else self.make_default("Ccy")

	@Ccy.deleter
	def Ccy(self):
		del self._Ccy
		self._Ccy = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def StmtFrqcyAndFrmt(self):
		return self._StmtFrqcyAndFrmt

	@StmtFrqcyAndFrmt.setter
	def StmtFrqcyAndFrmt(self, value):
		self._StmtFrqcyAndFrmt = value if type(value) != auto else self.make_default("StmtFrqcyAndFrmt")

	@StmtFrqcyAndFrmt.deleter
	def StmtFrqcyAndFrmt(self):
		del self._StmtFrqcyAndFrmt
		self._StmtFrqcyAndFrmt = None

	@property
	def MnthlyRcvdVal(self):
		return self._MnthlyRcvdVal

	@MnthlyRcvdVal.setter
	def MnthlyRcvdVal(self, value):
		self._MnthlyRcvdVal = value if type(value) != auto else self.make_default("MnthlyRcvdVal")

	@MnthlyRcvdVal.deleter
	def MnthlyRcvdVal(self):
		del self._MnthlyRcvdVal
		self._MnthlyRcvdVal = None

	@property
	def Rstrctn(self):
		return self._Rstrctn

	@Rstrctn.setter
	def Rstrctn(self, value):
		self._Rstrctn = value if type(value) != auto else self.make_default("Rstrctn")

	@Rstrctn.deleter
	def Rstrctn(self):
		del self._Rstrctn
		self._Rstrctn = None

	@property
	def ClsgDt(self):
		return self._ClsgDt

	@ClsgDt.setter
	def ClsgDt(self, value):
		self._ClsgDt = value if type(value) != auto else self.make_default("ClsgDt")

	@ClsgDt.deleter
	def ClsgDt(self):
		del self._ClsgDt
		self._ClsgDt = None

	@property
	def AvrgBal(self):
		return self._AvrgBal

	@AvrgBal.setter
	def AvrgBal(self, value):
		self._AvrgBal = value if type(value) != auto else self.make_default("AvrgBal")

	@AvrgBal.deleter
	def AvrgBal(self):
		del self._AvrgBal
		self._AvrgBal = None

	@property
	def ClngNtfctnAmt(self):
		return self._ClngNtfctnAmt

	@ClngNtfctnAmt.setter
	def ClngNtfctnAmt(self, value):
		self._ClngNtfctnAmt = value if type(value) != auto else self.make_default("ClngNtfctnAmt")

	@ClngNtfctnAmt.deleter
	def ClngNtfctnAmt(self):
		del self._ClngNtfctnAmt
		self._ClngNtfctnAmt = None

	@property
	def MnthlyTxNb(self):
		return self._MnthlyTxNb

	@MnthlyTxNb.setter
	def MnthlyTxNb(self, value):
		self._MnthlyTxNb = value if type(value) != auto else self.make_default("MnthlyTxNb")

	@MnthlyTxNb.deleter
	def MnthlyTxNb(self):
		del self._MnthlyTxNb
		self._MnthlyTxNb = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=AccountStatus3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FlrNtfctnAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctPurp', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnthlyPmtVal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=CashAccountType2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ccy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=AccountIdentification4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StmtFrqcyAndFrmt', type=StatementFrequencyAndForm1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MnthlyRcvdVal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rstrctn', type=Restriction1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClsgDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AvrgBal', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ClngNtfctnAmt', type=ImpliedCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MnthlyTxNb', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

