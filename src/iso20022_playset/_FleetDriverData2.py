# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ATICALaxProcessing
from . import ISOCountrySubDivisionCode
from . import ISODate
from . import ISOMax3ACountryCode
from . import LegalStructure1Code
from . import Max105Text
from . import Max16Text
from . import Max35Text
from . import Max70Text
from . import PresentationMedium2Code
from . import TravelDocument3

class FleetDriverData2(base_types._BaseFieldType):

	__slots__ = ["_AddtlId", "_DeptNb", "_DtOfBirth", "_Id", "_LicAssgnr", "_LicCtry", "_LicCtrySubDvsnMjr", "_LicCtrySubDvsnMnr", "_LicForm", "_LicId", "_LicIssncDt", "_LicOthrAuthrty", "_LicTp", "_LicXprtnDt", "_MplyeeId", "_Mplyr", "_Nm", "_NtlData", "_PrvtData"]
	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if value is not None else base_types.UninitialisedField(self, 'AddtlId', TravelDocument3, True)

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = base_types.UninitialisedField(self, 'AddtlId', TravelDocument3, True)

	@property
	def DeptNb(self):
		return self._DeptNb

	@DeptNb.setter
	def DeptNb(self, value):
		self._DeptNb = value if value is not None else base_types.UninitialisedField(self, 'DeptNb', Max35Text, False)

	@DeptNb.deleter
	def DeptNb(self):
		del self._DeptNb
		self._DeptNb = base_types.UninitialisedField(self, 'DeptNb', Max35Text, False)

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
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max70Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max70Text, False)

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
	def MplyeeId(self):
		return self._MplyeeId

	@MplyeeId.setter
	def MplyeeId(self, value):
		self._MplyeeId = value if value is not None else base_types.UninitialisedField(self, 'MplyeeId', Max70Text, False)

	@MplyeeId.deleter
	def MplyeeId(self):
		del self._MplyeeId
		self._MplyeeId = base_types.UninitialisedField(self, 'MplyeeId', Max70Text, False)

	@property
	def Mplyr(self):
		return self._Mplyr

	@Mplyr.setter
	def Mplyr(self, value):
		self._Mplyr = value if value is not None else base_types.UninitialisedField(self, 'Mplyr', Max70Text, False)

	@Mplyr.deleter
	def Mplyr(self):
		del self._Mplyr
		self._Mplyr = base_types.UninitialisedField(self, 'Mplyr', Max70Text, False)

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

	@property
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if value is not None else base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = base_types.UninitialisedField(self, 'NtlData', ATICALaxProcessing, True)

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if value is not None else base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = base_types.UninitialisedField(self, 'PrvtData', ATICALaxProcessing, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlId', type=TravelDocument3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DeptNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DtOfBirth', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
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
		base_types.FieldEntry(name='MplyeeId', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Mplyr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max105Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtlData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrvtData', type=ATICALaxProcessing, min=0, max=None, mutex_group=None, array=True),
	))