import base_types
import Max35Text
import TaxPeriod3
import TaxAmount3
import Max140Text

class TaxRecord3(base_types._BaseFieldType):

	__slots__ = ["_Tp", "_AddtlInf", "_Ctgy", "_FrmsCd", "_DbtrSts", "_CertId", "_Prd", "_TaxAmt", "_CtgyDtls"]
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
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if type(value) != auto else self.make_default("Ctgy")

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = None

	@property
	def FrmsCd(self):
		return self._FrmsCd

	@FrmsCd.setter
	def FrmsCd(self, value):
		self._FrmsCd = value if type(value) != auto else self.make_default("FrmsCd")

	@FrmsCd.deleter
	def FrmsCd(self):
		del self._FrmsCd
		self._FrmsCd = None

	@property
	def DbtrSts(self):
		return self._DbtrSts

	@DbtrSts.setter
	def DbtrSts(self, value):
		self._DbtrSts = value if type(value) != auto else self.make_default("DbtrSts")

	@DbtrSts.deleter
	def DbtrSts(self):
		del self._DbtrSts
		self._DbtrSts = None

	@property
	def CertId(self):
		return self._CertId

	@CertId.setter
	def CertId(self, value):
		self._CertId = value if type(value) != auto else self.make_default("CertId")

	@CertId.deleter
	def CertId(self):
		del self._CertId
		self._CertId = None

	@property
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if type(value) != auto else self.make_default("Prd")

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = None

	@property
	def TaxAmt(self):
		return self._TaxAmt

	@TaxAmt.setter
	def TaxAmt(self, value):
		self._TaxAmt = value if type(value) != auto else self.make_default("TaxAmt")

	@TaxAmt.deleter
	def TaxAmt(self):
		del self._TaxAmt
		self._TaxAmt = None

	@property
	def CtgyDtls(self):
		return self._CtgyDtls

	@CtgyDtls.setter
	def CtgyDtls(self, value):
		self._CtgyDtls = value if type(value) != auto else self.make_default("CtgyDtls")

	@CtgyDtls.deleter
	def CtgyDtls(self):
		del self._CtgyDtls
		self._CtgyDtls = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmsCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrSts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=TaxPeriod3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAmt', type=TaxAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtgyDtls', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

