from . import base_types
from ._GenericIdentification164 import GenericIdentification164
from ._BeneficiaryCertificationCompletion1Code import BeneficiaryCertificationCompletion1Code
from ._Max350Text import Max350Text
from ._CountryAndResidentialStatusType2 import CountryAndResidentialStatusType2
from ._ISODate import ISODate

class IndividualPerson31(base_types._BaseFieldType):

	__slots__ = ["_OthrId", "_Nm", "_BirthDt", "_BnfcryCertfctnCmpltn", "_CtryAndResdtlSts"]
	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if type(value) != base_types.auto else self.make_default("OthrId")

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if type(value) != base_types.auto else self.make_default("BirthDt")

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = None

	@property
	def BnfcryCertfctnCmpltn(self):
		return self._BnfcryCertfctnCmpltn

	@BnfcryCertfctnCmpltn.setter
	def BnfcryCertfctnCmpltn(self, value):
		self._BnfcryCertfctnCmpltn = value if type(value) != base_types.auto else self.make_default("BnfcryCertfctnCmpltn")

	@BnfcryCertfctnCmpltn.deleter
	def BnfcryCertfctnCmpltn(self):
		del self._BnfcryCertfctnCmpltn
		self._BnfcryCertfctnCmpltn = None

	@property
	def CtryAndResdtlSts(self):
		return self._CtryAndResdtlSts

	@CtryAndResdtlSts.setter
	def CtryAndResdtlSts(self, value):
		self._CtryAndResdtlSts = value if type(value) != base_types.auto else self.make_default("CtryAndResdtlSts")

	@CtryAndResdtlSts.deleter
	def CtryAndResdtlSts(self):
		del self._CtryAndResdtlSts
		self._CtryAndResdtlSts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrId', type=GenericIdentification164, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryCertfctnCmpltn', type=BeneficiaryCertificationCompletion1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryAndResdtlSts', type=CountryAndResidentialStatusType2, min=0, max=1, mutex_group=None, array=False),
	))

