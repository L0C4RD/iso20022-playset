# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AuthenticationEntity2Code
from . import AuthenticationMethod7Code
from . import Max140Binary
from . import Max500Text
from . import Verification1Code

class TransactionVerificationResult5(base_types._BaseFieldType):

	__slots__ = ["_AddtlRslt", "_AuthntcnTkn", "_Mtd", "_Rslt", "_VrfctnNtty"]
	@property
	def AddtlRslt(self):
		return self._AddtlRslt

	@AddtlRslt.setter
	def AddtlRslt(self, value):
		self._AddtlRslt = value if value is not None else base_types.UninitialisedField(self, 'AddtlRslt', Max500Text, False)

	@AddtlRslt.deleter
	def AddtlRslt(self):
		del self._AddtlRslt
		self._AddtlRslt = base_types.UninitialisedField(self, 'AddtlRslt', Max500Text, False)

	@property
	def AuthntcnTkn(self):
		return self._AuthntcnTkn

	@AuthntcnTkn.setter
	def AuthntcnTkn(self, value):
		self._AuthntcnTkn = value if value is not None else base_types.UninitialisedField(self, 'AuthntcnTkn', Max140Binary, False)

	@AuthntcnTkn.deleter
	def AuthntcnTkn(self):
		del self._AuthntcnTkn
		self._AuthntcnTkn = base_types.UninitialisedField(self, 'AuthntcnTkn', Max140Binary, False)

	@property
	def Mtd(self):
		return self._Mtd

	@Mtd.setter
	def Mtd(self, value):
		self._Mtd = value if value is not None else base_types.UninitialisedField(self, 'Mtd', AuthenticationMethod7Code, False)

	@Mtd.deleter
	def Mtd(self):
		del self._Mtd
		self._Mtd = base_types.UninitialisedField(self, 'Mtd', AuthenticationMethod7Code, False)

	@property
	def Rslt(self):
		return self._Rslt

	@Rslt.setter
	def Rslt(self, value):
		self._Rslt = value if value is not None else base_types.UninitialisedField(self, 'Rslt', Verification1Code, False)

	@Rslt.deleter
	def Rslt(self):
		del self._Rslt
		self._Rslt = base_types.UninitialisedField(self, 'Rslt', Verification1Code, False)

	@property
	def VrfctnNtty(self):
		return self._VrfctnNtty

	@VrfctnNtty.setter
	def VrfctnNtty(self, value):
		self._VrfctnNtty = value if value is not None else base_types.UninitialisedField(self, 'VrfctnNtty', AuthenticationEntity2Code, False)

	@VrfctnNtty.deleter
	def VrfctnNtty(self):
		del self._VrfctnNtty
		self._VrfctnNtty = base_types.UninitialisedField(self, 'VrfctnNtty', AuthenticationEntity2Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlRslt', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthntcnTkn', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mtd', type=AuthenticationMethod7Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rslt', type=Verification1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VrfctnNtty', type=AuthenticationEntity2Code, min=0, max=1, mutex_group=None, array=False),
	))