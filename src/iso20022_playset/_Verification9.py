# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._ExternalAuthenticationMethod1Code import ExternalAuthenticationMethod1Code
from ._Max35Text import Max35Text
from ._Verification4Code import Verification4Code
from ._VerificationEntity3Code import VerificationEntity3Code

class Verification9(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Ntty", "_Rslt", "_RsltDtls", "_SubTp", "_Tp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def Ntty(self):
		return self._Ntty

	@Ntty.setter
	def Ntty(self, value):
		self._Ntty = value if type(value) != base_types.auto else self.make_default("Ntty")

	@Ntty.deleter
	def Ntty(self):
		del self._Ntty
		self._Ntty = None

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if type(value) != base_types.auto else self.make_default("Rslt")

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = None

	@property
	def RsltDtls(self):
		return self._RsltDtls

	@RsltDtls.setter
	def RsltDtls(self, value):
		self._RsltDtls = value if type(value) != base_types.auto else self.make_default("RsltDtls")

	@RsltDtls.deleter
	def RsltDtls(self):
		del self._RsltDtls
		self._RsltDtls = None

	@property
	def SubTp(self):
		return self._SubTp

	@SubTp.setter
	def SubTp(self, value):
		self._SubTp = value if type(value) != base_types.auto else self.make_default("SubTp")

	@SubTp.deleter
	def SubTp(self):
		del self._SubTp
		self._SubTp = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != base_types.auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ntty', type=VerificationEntity3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=Verification4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RsltDtls', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SubTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=ExternalAuthenticationMethod1Code, min=0, max=1, mutex_group=None, array=False),
	))