# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CertificateIssuer1
from . import Number
from . import PublicRSAKey2
from . import RelativeDistinguishedName2

class CertificationRequest2(base_types._BaseFieldType):

	__slots__ = ["_Attr", "_SbjtNm", "_SbjtPblcKeyInf", "_Vrsn"]
	@property
	def Attr(self):
		return self._Attr

	@Attr.setter
	def Attr(self, value):
		self._Attr = value if value is not None else base_types.UninitialisedField(self, 'Attr', RelativeDistinguishedName2, True)

	@Attr.deleter
	def Attr(self):
		del self._Attr
		self._Attr = base_types.UninitialisedField(self, 'Attr', RelativeDistinguishedName2, True)

	@property
	def SbjtNm(self):
		return self._SbjtNm

	@SbjtNm.setter
	def SbjtNm(self, value):
		self._SbjtNm = value if value is not None else base_types.UninitialisedField(self, 'SbjtNm', CertificateIssuer1, False)

	@SbjtNm.deleter
	def SbjtNm(self):
		del self._SbjtNm
		self._SbjtNm = base_types.UninitialisedField(self, 'SbjtNm', CertificateIssuer1, False)

	@property
	def SbjtPblcKeyInf(self):
		return self._SbjtPblcKeyInf

	@SbjtPblcKeyInf.setter
	def SbjtPblcKeyInf(self, value):
		self._SbjtPblcKeyInf = value if value is not None else base_types.UninitialisedField(self, 'SbjtPblcKeyInf', PublicRSAKey2, False)

	@SbjtPblcKeyInf.deleter
	def SbjtPblcKeyInf(self):
		del self._SbjtPblcKeyInf
		self._SbjtPblcKeyInf = base_types.UninitialisedField(self, 'SbjtPblcKeyInf', PublicRSAKey2, False)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Number, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Number, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attr', type=RelativeDistinguishedName2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SbjtNm', type=CertificateIssuer1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtPblcKeyInf', type=PublicRSAKey2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
	))