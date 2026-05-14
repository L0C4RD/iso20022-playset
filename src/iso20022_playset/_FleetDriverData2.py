from . import base_types
from ._ATICALaxProcessing import ATICALaxProcessing
from ._ISOCountrySubDivisionCode import ISOCountrySubDivisionCode
from ._ISODate import ISODate
from ._ISOMax3ACountryCode import ISOMax3ACountryCode
from ._LegalStructure1Code import LegalStructure1Code
from ._Max105Text import Max105Text
from ._Max16Text import Max16Text
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text
from ._PresentationMedium2Code import PresentationMedium2Code
from ._TravelDocument3 import TravelDocument3

class FleetDriverData2(base_types._BaseFieldType):

	__slots__ = ["_AddtlId", "_DeptNb", "_DtOfBirth", "_Id", "_LicAssgnr", "_LicCtry", "_LicCtrySubDvsnMjr", "_LicCtrySubDvsnMnr", "_LicForm", "_LicId", "_LicIssncDt", "_LicOthrAuthrty", "_LicTp", "_LicXprtnDt", "_MplyeeId", "_Mplyr", "_Nm", "_NtlData", "_PrvtData"]
	@property
	def AddtlId(self):
		return self._AddtlId

	@AddtlId.setter
	def AddtlId(self, value):
		self._AddtlId = value if type(value) != base_types.auto else self.make_default("AddtlId")

	@AddtlId.deleter
	def AddtlId(self):
		del self._AddtlId
		self._AddtlId = None

	@property
	def DeptNb(self):
		return self._DeptNb

	@DeptNb.setter
	def DeptNb(self, value):
		self._DeptNb = value if type(value) != base_types.auto else self.make_default("DeptNb")

	@DeptNb.deleter
	def DeptNb(self):
		del self._DeptNb
		self._DeptNb = None

	@property
	def DtOfBirth(self):
		return self._DtOfBirth

	@DtOfBirth.setter
	def DtOfBirth(self, value):
		self._DtOfBirth = value if type(value) != base_types.auto else self.make_default("DtOfBirth")

	@DtOfBirth.deleter
	def DtOfBirth(self):
		del self._DtOfBirth
		self._DtOfBirth = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def LicAssgnr(self):
		return self._LicAssgnr

	@LicAssgnr.setter
	def LicAssgnr(self, value):
		self._LicAssgnr = value if type(value) != base_types.auto else self.make_default("LicAssgnr")

	@LicAssgnr.deleter
	def LicAssgnr(self):
		del self._LicAssgnr
		self._LicAssgnr = None

	@property
	def LicCtry(self):
		return self._LicCtry

	@LicCtry.setter
	def LicCtry(self, value):
		self._LicCtry = value if type(value) != base_types.auto else self.make_default("LicCtry")

	@LicCtry.deleter
	def LicCtry(self):
		del self._LicCtry
		self._LicCtry = None

	@property
	def LicCtrySubDvsnMjr(self):
		return self._LicCtrySubDvsnMjr

	@LicCtrySubDvsnMjr.setter
	def LicCtrySubDvsnMjr(self, value):
		self._LicCtrySubDvsnMjr = value if type(value) != base_types.auto else self.make_default("LicCtrySubDvsnMjr")

	@LicCtrySubDvsnMjr.deleter
	def LicCtrySubDvsnMjr(self):
		del self._LicCtrySubDvsnMjr
		self._LicCtrySubDvsnMjr = None

	@property
	def LicCtrySubDvsnMnr(self):
		return self._LicCtrySubDvsnMnr

	@LicCtrySubDvsnMnr.setter
	def LicCtrySubDvsnMnr(self, value):
		self._LicCtrySubDvsnMnr = value if type(value) != base_types.auto else self.make_default("LicCtrySubDvsnMnr")

	@LicCtrySubDvsnMnr.deleter
	def LicCtrySubDvsnMnr(self):
		del self._LicCtrySubDvsnMnr
		self._LicCtrySubDvsnMnr = None

	@property
	def LicForm(self):
		return self._LicForm

	@LicForm.setter
	def LicForm(self, value):
		self._LicForm = value if type(value) != base_types.auto else self.make_default("LicForm")

	@LicForm.deleter
	def LicForm(self):
		del self._LicForm
		self._LicForm = None

	@property
	def LicId(self):
		return self._LicId

	@LicId.setter
	def LicId(self, value):
		self._LicId = value if type(value) != base_types.auto else self.make_default("LicId")

	@LicId.deleter
	def LicId(self):
		del self._LicId
		self._LicId = None

	@property
	def LicIssncDt(self):
		return self._LicIssncDt

	@LicIssncDt.setter
	def LicIssncDt(self, value):
		self._LicIssncDt = value if type(value) != base_types.auto else self.make_default("LicIssncDt")

	@LicIssncDt.deleter
	def LicIssncDt(self):
		del self._LicIssncDt
		self._LicIssncDt = None

	@property
	def LicOthrAuthrty(self):
		return self._LicOthrAuthrty

	@LicOthrAuthrty.setter
	def LicOthrAuthrty(self, value):
		self._LicOthrAuthrty = value if type(value) != base_types.auto else self.make_default("LicOthrAuthrty")

	@LicOthrAuthrty.deleter
	def LicOthrAuthrty(self):
		del self._LicOthrAuthrty
		self._LicOthrAuthrty = None

	@property
	def LicTp(self):
		return self._LicTp

	@LicTp.setter
	def LicTp(self, value):
		self._LicTp = value if type(value) != base_types.auto else self.make_default("LicTp")

	@LicTp.deleter
	def LicTp(self):
		del self._LicTp
		self._LicTp = None

	@property
	def LicXprtnDt(self):
		return self._LicXprtnDt

	@LicXprtnDt.setter
	def LicXprtnDt(self, value):
		self._LicXprtnDt = value if type(value) != base_types.auto else self.make_default("LicXprtnDt")

	@LicXprtnDt.deleter
	def LicXprtnDt(self):
		del self._LicXprtnDt
		self._LicXprtnDt = None

	@property
	def MplyeeId(self):
		return self._MplyeeId

	@MplyeeId.setter
	def MplyeeId(self, value):
		self._MplyeeId = value if type(value) != base_types.auto else self.make_default("MplyeeId")

	@MplyeeId.deleter
	def MplyeeId(self):
		del self._MplyeeId
		self._MplyeeId = None

	@property
	def Mplyr(self):
		return self._Mplyr

	@Mplyr.setter
	def Mplyr(self, value):
		self._Mplyr = value if type(value) != base_types.auto else self.make_default("Mplyr")

	@Mplyr.deleter
	def Mplyr(self):
		del self._Mplyr
		self._Mplyr = None

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
	def NtlData(self):
		return self._NtlData

	@NtlData.setter
	def NtlData(self, value):
		self._NtlData = value if type(value) != base_types.auto else self.make_default("NtlData")

	@NtlData.deleter
	def NtlData(self):
		del self._NtlData
		self._NtlData = None

	@property
	def PrvtData(self):
		return self._PrvtData

	@PrvtData.setter
	def PrvtData(self, value):
		self._PrvtData = value if type(value) != base_types.auto else self.make_default("PrvtData")

	@PrvtData.deleter
	def PrvtData(self):
		del self._PrvtData
		self._PrvtData = None

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

