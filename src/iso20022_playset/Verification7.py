from . import base_types
import ExternalAuthenticationMethod1Code
import Max500Text
import VerificationEntity2Code
import AdditionalData1
import Verification3Code
import Max35Text

class Verification7(base_types._BaseFieldType):

	__slots__ = ["_OthrNtty", "_SubTp", "_Ntty", "_Rslt", "_Tp", "_OthrTp", "_OthrRslt", "_RsltDtls", "_AddtlInf"]
	@property
	def OthrNtty(self):
		return self._OthrNtty

	@OthrNtty.setter
	def OthrNtty(self, value):
		self._OthrNtty = value if type(value) != auto else self.make_default("OthrNtty")

	@OthrNtty.deleter
	def OthrNtty(self):
		del self._OthrNtty
		self._OthrNtty = None

	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if type(value) != auto else self.make_default("SubTp")

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = None

	@property
	def Ntty(self):
		return self._Ntty

	@Ntty.setter
	def Ntty(self, value):
		self._Ntty = value if type(value) != auto else self.make_default("Ntty")

	@Ntty.deleter
	def Ntty(self):
		del self._Ntty
		self._Ntty = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

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
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if type(value) != auto else self.make_default("OthrTp")

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = None

	@property
	def OthrRslt(self):
		return self._OthrRslt

	@OthrRslt.setter
	def OthrRslt(self, value):
		self._OthrRslt = value if type(value) != auto else self.make_default("OthrRslt")

	@OthrRslt.deleter
	def OthrRslt(self):
		del self._OthrRslt
		self._OthrRslt = None

	@property
	def RsltDtls(self):
		return self._RsltDtls

	@RsltDtls.setter
	def RsltDtls(self, value):
		self._RsltDtls = value if type(value) != auto else self.make_default("RsltDtls")

	@RsltDtls.deleter
	def RsltDtls(self):
		del self._RsltDtls
		self._RsltDtls = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrNtty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntty', type=VerificationEntity2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=Verification3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ExternalAuthenticationMethod1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRslt', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltDtls', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

