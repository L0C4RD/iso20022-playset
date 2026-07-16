# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalData1
from . import ExternalAuthenticationMethod1Code
from . import Max35Text
from . import Max500Text
from . import Verification3Code
from . import VerificationEntity2Code

class Verification7(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Ntty", "_OthrNtty", "_OthrRslt", "_OthrTp", "_Rslt", "_RsltDtls", "_SubTp", "_Tp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max35Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max35Text, False)

	@property
	def Ntty(self):
		return self._Ntty

	@Ntty.setter
	def Ntty(self, value):
		self._Ntty = value if value is not None else base_types.UninitialisedField(self, 'Ntty', VerificationEntity2Code, False)

	@Ntty.deleter
	def Ntty(self):
		del self._Ntty
		self._Ntty = base_types.UninitialisedField(self, 'Ntty', VerificationEntity2Code, False)

	@property
	def OthrNtty(self):
		return self._OthrNtty

	@OthrNtty.setter
	def OthrNtty(self, value):
		self._OthrNtty = value if value is not None else base_types.UninitialisedField(self, 'OthrNtty', Max35Text, False)

	@OthrNtty.deleter
	def OthrNtty(self):
		del self._OthrNtty
		self._OthrNtty = base_types.UninitialisedField(self, 'OthrNtty', Max35Text, False)

	@property
	def OthrRslt(self):
		return self._OthrRslt

	@OthrRslt.setter
	def OthrRslt(self, value):
		self._OthrRslt = value if value is not None else base_types.UninitialisedField(self, 'OthrRslt', Max500Text, False)

	@OthrRslt.deleter
	def OthrRslt(self):
		del self._OthrRslt
		self._OthrRslt = base_types.UninitialisedField(self, 'OthrRslt', Max500Text, False)

	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', Verification3Code, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', Verification3Code, False)

	@property
	def RsltDtls(self):
		return self._RsltDtls

	@RsltDtls.setter
	def RsltDtls(self, value):
		self._RsltDtls = value if value is not None else base_types.UninitialisedField(self, 'RsltDtls', AdditionalData1, True)

	@RsltDtls.deleter
	def RsltDtls(self):
		del self._RsltDtls
		self._RsltDtls = base_types.UninitialisedField(self, 'RsltDtls', AdditionalData1, True)

	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if value is not None else base_types.UninitialisedField(self, 'SubTp', Max35Text, False)

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = base_types.UninitialisedField(self, 'SubTp', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', ExternalAuthenticationMethod1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', ExternalAuthenticationMethod1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntty', type=VerificationEntity2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrNtty', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrRslt', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=Verification3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltDtls', type=AdditionalData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ExternalAuthenticationMethod1Code, min=0, max=1, mutex_group=None, array=False),
	))