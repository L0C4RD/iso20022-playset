import base_types
import RelativeDistinguishedName2
import Number
import CertificateIssuer1
import PublicRSAKey2

class CertificationRequest2(base_types._BaseFieldType):

	__slots__ = ["_Attr", "_Vrsn", "_SbjtPblcKeyInf", "_SbjtNm"]
	@property
	def Attr(self):
		return self._Attr

	@Attr.setter
	def Attr(self, value):
		self._Attr = value if type(value) != auto else self.make_default("Attr")

	@Attr.deleter
	def Attr(self):
		del self._Attr
		self._Attr = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def SbjtPblcKeyInf(self):
		return self._SbjtPblcKeyInf

	@SbjtPblcKeyInf.setter
	def SbjtPblcKeyInf(self, value):
		self._SbjtPblcKeyInf = value if type(value) != auto else self.make_default("SbjtPblcKeyInf")

	@SbjtPblcKeyInf.deleter
	def SbjtPblcKeyInf(self):
		del self._SbjtPblcKeyInf
		self._SbjtPblcKeyInf = None

	@property
	def SbjtNm(self):
		return self._SbjtNm

	@SbjtNm.setter
	def SbjtNm(self, value):
		self._SbjtNm = value if type(value) != auto else self.make_default("SbjtNm")

	@SbjtNm.deleter
	def SbjtNm(self):
		del self._SbjtNm
		self._SbjtNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Attr', type=RelativeDistinguishedName2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrsn', type=Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtPblcKeyInf', type=PublicRSAKey2, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtNm', type=CertificateIssuer1, min=0, max=1, mutex_group=None, array=False),
	))

