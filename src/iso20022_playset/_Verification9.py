# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import ExternalAuthenticationMethod1Code
from . import Max35Text
from . import Verification4Code
from . import VerificationEntity3Code

class Verification9(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Ntty", "_Rslt", "_RsltDtls", "_SubTp", "_Tp"]
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
		self._Ntty = value if value is not None else base_types.UninitialisedField(self, 'Ntty', VerificationEntity3Code, False)

	@Ntty.deleter
	def Ntty(self):
		del self._Ntty
		self._Ntty = base_types.UninitialisedField(self, 'Ntty', VerificationEntity3Code, False)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', Verification4Code, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', Verification4Code, False)

	@property
	def RsltDtls(self):
		return self._RsltDtls

	@RsltDtls.setter
	def RsltDtls(self, value):
		self._RsltDtls = value if value is not None else base_types.UninitialisedField(self, 'RsltDtls', ATICALaxProcessing, True)

	@RsltDtls.deleter
	def RsltDtls(self):
		del self._RsltDtls
		self._RsltDtls = base_types.UninitialisedField(self, 'RsltDtls', ATICALaxProcessing, True)

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
		base_types.FieldEntry(name='Ntty', type=VerificationEntity3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=Verification4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltDtls', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ExternalAuthenticationMethod1Code, min=0, max=1, mutex_group=None, array=False),
	))