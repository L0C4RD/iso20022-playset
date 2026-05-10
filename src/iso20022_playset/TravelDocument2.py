from . import base_types
from .Max70Text import Max70Text
from .OfficialDocumentType1Code import OfficialDocumentType1Code
from .PresentationMedium2Code import PresentationMedium2Code
from .ISODate import ISODate
from .ISOMax3ACountryCode import ISOMax3ACountryCode

class TravelDocument2(base_types._BaseFieldType):

	__slots__ = ["_Form", "_IssncDt", "_XprtnDt", "_Tp", "_Id", "_Ctry", "_Assgnr"]
	@property
	def Form(self):
		return self._Form

	@Form.setter
	def Form(self, value):
		self._Form = value if type(value) != auto else self.make_default("Form")

	@Form.deleter
	def Form(self):
		del self._Form
		self._Form = None

	@property
	def IssncDt(self):
		return self._IssncDt

	@IssncDt.setter
	def IssncDt(self, value):
		self._IssncDt = value if type(value) != auto else self.make_default("IssncDt")

	@IssncDt.deleter
	def IssncDt(self):
		del self._IssncDt
		self._IssncDt = None

	@property
	def XprtnDt(self):
		return self._XprtnDt

	@XprtnDt.setter
	def XprtnDt(self, value):
		self._XprtnDt = value if type(value) != auto else self.make_default("XprtnDt")

	@XprtnDt.deleter
	def XprtnDt(self):
		del self._XprtnDt
		self._XprtnDt = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Ctry(self):
		return self._Ctry

	@Ctry.setter
	def Ctry(self, value):
		self._Ctry = value if type(value) != auto else self.make_default("Ctry")

	@Ctry.deleter
	def Ctry(self):
		del self._Ctry
		self._Ctry = None

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if type(value) != auto else self.make_default("Assgnr")

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Form', type=PresentationMedium2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssncDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XprtnDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=OfficialDocumentType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctry', type=ISOMax3ACountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))

