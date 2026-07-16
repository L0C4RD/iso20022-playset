# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Address4
from . import ContactPersonal2
from . import ISOCountrySubDivisionCode
from . import ISODate
from . import ISOMax3ACountryCode
from . import LegalStructure1Code
from . import Max105Text
from . import Max16Text
from . import Max2NumericText
from . import Max35Text
from . import Max70Text
from . import PresentationMedium2Code
from . import TravelDocument3

class DriverInParty4(base_types._BaseFieldType):

	__slots__ = ["_Adr", "_Age", "_Ctct", "_DrvrCrdntl", "_DtOfBirth", "_GvnNm", "_LastNm", "_LicAssgnr", "_LicCtry", "_LicCtrySubDvsnMjr", "_LicCtrySubDvsnMnr", "_LicForm", "_LicId", "_LicIssncDt", "_LicOthrAuthrty", "_LicTp", "_LicXprtnDt", "_MddlNm", "_Nm"]
	@property
	def Adr(self):
		return self._Adr

	@Adr.setter
	def Adr(self, value):
		self._Adr = value if value is not None else base_types.UninitialisedField(self, 'Adr', Address4, False)

	@Adr.deleter
	def Adr(self):
		del self._Adr
		self._Adr = base_types.UninitialisedField(self, 'Adr', Address4, False)

	@property
	def Age(self):
		return self._Age

	@Age.setter
	def Age(self, value):
		self._Age = value if value is not None else base_types.UninitialisedField(self, 'Age', Max2NumericText, False)

	@Age.deleter
	def Age(self):
		del self._Age
		self._Age = base_types.UninitialisedField(self, 'Age', Max2NumericText, False)

	@property
	def Ctct(self):
		return self._Ctct

	@Ctct.setter
	def Ctct(self, value):
		self._Ctct = value if value is not None else base_types.UninitialisedField(self, 'Ctct', ContactPersonal2, False)

	@Ctct.deleter
	def Ctct(self):
		del self._Ctct
		self._Ctct = base_types.UninitialisedField(self, 'Ctct', ContactPersonal2, False)

	@property
	def DrvrCrdntl(self):
		return self._DrvrCrdntl

	@DrvrCrdntl.setter
	def DrvrCrdntl(self, value):
		self._DrvrCrdntl = value if value is not None else base_types.UninitialisedField(self, 'DrvrCrdntl', TravelDocument3, True)

	@DrvrCrdntl.deleter
	def DrvrCrdntl(self):
		del self._DrvrCrdntl
		self._DrvrCrdntl = base_types.UninitialisedField(self, 'DrvrCrdntl', TravelDocument3, True)

	@property
	def DtOfBirth(self):
		return self._DtOfBirth

	@DtOfBirth.setter
	def DtOfBirth(self, value):
		self._DtOfBirth = value if value is not None else base_types.UninitialisedField(self, 'DtOfBirth', ISODate, False)

	@DtOfBirth.deleter
	def DtOfBirth(self):
		del self._DtOfBirth
		self._DtOfBirth = base_types.UninitialisedField(self, 'DtOfBirth', ISODate, False)

	@property
	def GvnNm(self):
		return self._GvnNm

	@GvnNm.setter
	def GvnNm(self, value):
		self._GvnNm = value if value is not None else base_types.UninitialisedField(self, 'GvnNm', Max35Text, False)

	@GvnNm.deleter
	def GvnNm(self):
		del self._GvnNm
		self._GvnNm = base_types.UninitialisedField(self, 'GvnNm', Max35Text, False)

	@property
	def LastNm(self):
		return self._LastNm

	@LastNm.setter
	def LastNm(self, value):
		self._LastNm = value if value is not None else base_types.UninitialisedField(self, 'LastNm', Max35Text, False)

	@LastNm.deleter
	def LastNm(self):
		del self._LastNm
		self._LastNm = base_types.UninitialisedField(self, 'LastNm', Max35Text, False)

	@property
	def LicAssgnr(self):
		return self._LicAssgnr

	@LicAssgnr.setter
	def LicAssgnr(self, value):
		self._LicAssgnr = value if value is not None else base_types.UninitialisedField(self, 'LicAssgnr', LegalStructure1Code, False)

	@LicAssgnr.deleter
	def LicAssgnr(self):
		del self._LicAssgnr
		self._LicAssgnr = base_types.UninitialisedField(self, 'LicAssgnr', LegalStructure1Code, False)

	@property
	def LicCtry(self):
		return self._LicCtry

	@LicCtry.setter
	def LicCtry(self, value):
		self._LicCtry = value if value is not None else base_types.UninitialisedField(self, 'LicCtry', ISOMax3ACountryCode, False)

	@LicCtry.deleter
	def LicCtry(self):
		del self._LicCtry
		self._LicCtry = base_types.UninitialisedField(self, 'LicCtry', ISOMax3ACountryCode, False)

	@property
	def LicCtrySubDvsnMjr(self):
		return self._LicCtrySubDvsnMjr

	@LicCtrySubDvsnMjr.setter
	def LicCtrySubDvsnMjr(self, value):
		self._LicCtrySubDvsnMjr = value if value is not None else base_types.UninitialisedField(self, 'LicCtrySubDvsnMjr', ISOCountrySubDivisionCode, False)

	@LicCtrySubDvsnMjr.deleter
	def LicCtrySubDvsnMjr(self):
		del self._LicCtrySubDvsnMjr
		self._LicCtrySubDvsnMjr = base_types.UninitialisedField(self, 'LicCtrySubDvsnMjr', ISOCountrySubDivisionCode, False)

	@property
	def LicCtrySubDvsnMnr(self):
		return self._LicCtrySubDvsnMnr

	@LicCtrySubDvsnMnr.setter
	def LicCtrySubDvsnMnr(self, value):
		self._LicCtrySubDvsnMnr = value if value is not None else base_types.UninitialisedField(self, 'LicCtrySubDvsnMnr', ISOCountrySubDivisionCode, False)

	@LicCtrySubDvsnMnr.deleter
	def LicCtrySubDvsnMnr(self):
		del self._LicCtrySubDvsnMnr
		self._LicCtrySubDvsnMnr = base_types.UninitialisedField(self, 'LicCtrySubDvsnMnr', ISOCountrySubDivisionCode, False)

	@property
	def LicForm(self):
		return self._LicForm

	@LicForm.setter
	def LicForm(self, value):
		self._LicForm = value if value is not None else base_types.UninitialisedField(self, 'LicForm', PresentationMedium2Code, False)

	@LicForm.deleter
	def LicForm(self):
		del self._LicForm
		self._LicForm = base_types.UninitialisedField(self, 'LicForm', PresentationMedium2Code, False)

	@property
	def LicId(self):
		return self._LicId

	@LicId.setter
	def LicId(self, value):
		self._LicId = value if value is not None else base_types.UninitialisedField(self, 'LicId', Max70Text, False)

	@LicId.deleter
	def LicId(self):
		del self._LicId
		self._LicId = base_types.UninitialisedField(self, 'LicId', Max70Text, False)

	@property
	def LicIssncDt(self):
		return self._LicIssncDt

	@LicIssncDt.setter
	def LicIssncDt(self, value):
		self._LicIssncDt = value if value is not None else base_types.UninitialisedField(self, 'LicIssncDt', ISODate, False)

	@LicIssncDt.deleter
	def LicIssncDt(self):
		del self._LicIssncDt
		self._LicIssncDt = base_types.UninitialisedField(self, 'LicIssncDt', ISODate, False)

	@property
	def LicOthrAuthrty(self):
		return self._LicOthrAuthrty

	@LicOthrAuthrty.setter
	def LicOthrAuthrty(self, value):
		self._LicOthrAuthrty = value if value is not None else base_types.UninitialisedField(self, 'LicOthrAuthrty', Max16Text, False)

	@LicOthrAuthrty.deleter
	def LicOthrAuthrty(self):
		del self._LicOthrAuthrty
		self._LicOthrAuthrty = base_types.UninitialisedField(self, 'LicOthrAuthrty', Max16Text, False)

	@property
	def LicTp(self):
		return self._LicTp

	@LicTp.setter
	def LicTp(self, value):
		self._LicTp = value if value is not None else base_types.UninitialisedField(self, 'LicTp', Max70Text, False)

	@LicTp.deleter
	def LicTp(self):
		del self._LicTp
		self._LicTp = base_types.UninitialisedField(self, 'LicTp', Max70Text, False)

	@property
	def LicXprtnDt(self):
		return self._LicXprtnDt

	@LicXprtnDt.setter
	def LicXprtnDt(self, value):
		self._LicXprtnDt = value if value is not None else base_types.UninitialisedField(self, 'LicXprtnDt', ISODate, False)

	@LicXprtnDt.deleter
	def LicXprtnDt(self):
		del self._LicXprtnDt
		self._LicXprtnDt = base_types.UninitialisedField(self, 'LicXprtnDt', ISODate, False)

	@property
	def MddlNm(self):
		return self._MddlNm

	@MddlNm.setter
	def MddlNm(self, value):
		self._MddlNm = value if value is not None else base_types.UninitialisedField(self, 'MddlNm', Max35Text, False)

	@MddlNm.deleter
	def MddlNm(self):
		del self._MddlNm
		self._MddlNm = base_types.UninitialisedField(self, 'MddlNm', Max35Text, False)

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if value is not None else base_types.UninitialisedField(self, 'Nm', Max105Text, False)

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = base_types.UninitialisedField(self, 'Nm', Max105Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adr', type=Address4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Age', type=Max2NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctct', type=ContactPersonal2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DrvrCrdntl', type=TravelDocument3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtOfBirth', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='GvnNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LastNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LicAssgnr', type=LegalStructure1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LicCtry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LicCtrySubDvsnMjr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LicCtrySubDvsnMnr', type=ISOCountrySubDivisionCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LicForm', type=PresentationMedium2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LicId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LicIssncDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LicOthrAuthrty', type=Max16Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LicTp', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LicXprtnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MddlNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
	))