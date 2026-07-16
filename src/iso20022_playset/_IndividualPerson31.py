# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BeneficiaryCertificationCompletion1Code
from . import CountryAndResidentialStatusType2
from . import GenericIdentification164
from . import ISODate
from . import Max350Text

class IndividualPerson31(base_types._BaseFieldType):

	__slots__ = ["_BirthDt", "_BnfcryCertfctnCmpltn", "_CtryAndResdtlSts", "_Nm", "_OthrId"]
	@property
	def BirthDt(self):
		return self._BirthDt

	@BirthDt.setter
	def BirthDt(self, value):
		self._BirthDt = value if value is not None else base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@BirthDt.deleter
	def BirthDt(self):
		del self._BirthDt
		self._BirthDt = base_types.UninitialisedField(self, 'BirthDt', ISODate, False)

	@property
	def BnfcryCertfctnCmpltn(self):
		return self._BnfcryCertfctnCmpltn

	@BnfcryCertfctnCmpltn.setter
	def BnfcryCertfctnCmpltn(self, value):
		self._BnfcryCertfctnCmpltn = value if value is not None else base_types.UninitialisedField(self, 'BnfcryCertfctnCmpltn', BeneficiaryCertificationCompletion1Code, False)

	@BnfcryCertfctnCmpltn.deleter
	def BnfcryCertfctnCmpltn(self):
		del self._BnfcryCertfctnCmpltn
		self._BnfcryCertfctnCmpltn = base_types.UninitialisedField(self, 'BnfcryCertfctnCmpltn', BeneficiaryCertificationCompletion1Code, False)

	@property
	def CtryAndResdtlSts(self):
		return self._CtryAndResdtlSts

	@CtryAndResdtlSts.setter
	def CtryAndResdtlSts(self, value):
		self._CtryAndResdtlSts = value if value is not None else base_types.UninitialisedField(self, 'CtryAndResdtlSts', CountryAndResidentialStatusType2, False)

	@CtryAndResdtlSts.deleter
	def CtryAndResdtlSts(self):
		del self._CtryAndResdtlSts
		self._CtryAndResdtlSts = base_types.UninitialisedField(self, 'CtryAndResdtlSts', CountryAndResidentialStatusType2, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max350Text, False)

	@property
	def OthrId(self):
		return self._OthrId

	@OthrId.setter
	def OthrId(self, value):
		self._OthrId = value if value is not None else base_types.UninitialisedField(self, 'OthrId', GenericIdentification164, True)

	@OthrId.deleter
	def OthrId(self):
		del self._OthrId
		self._OthrId = base_types.UninitialisedField(self, 'OthrId', GenericIdentification164, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BirthDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BnfcryCertfctnCmpltn', type=BeneficiaryCertificationCompletion1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryAndResdtlSts', type=CountryAndResidentialStatusType2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrId', type=GenericIdentification164, min=0, max=None, mutex_group=None, array=True),
	))