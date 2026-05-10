from . import base_types
import PartyIdentificationAndAccount6
import ValidationStatusInformation1
import ISODateTime
import FinancialInstitutionIdentification6
import Max35Text
import CancellationStatusInformation1

class OriginalRequestInformation1(base_types._BaseFieldType):

	__slots__ = ["_FincgRqstr", "_FrstAgt", "_Id", "_CxlStsInf", "_IntrmyAgt", "_CreDtTm", "_VldtnStsInf"]
	@property
	def FincgRqstr(self):
		return self._FincgRqstr

	@FincgRqstr.setter
	def FincgRqstr(self, value):
		self._FincgRqstr = value if type(value) != auto else self.make_default("FincgRqstr")

	@FincgRqstr.deleter
	def FincgRqstr(self):
		del self._FincgRqstr
		self._FincgRqstr = None

	@property
	def FrstAgt(self):
		return self._FrstAgt

	@FrstAgt.setter
	def FrstAgt(self, value):
		self._FrstAgt = value if type(value) != auto else self.make_default("FrstAgt")

	@FrstAgt.deleter
	def FrstAgt(self):
		del self._FrstAgt
		self._FrstAgt = None

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
	def CxlStsInf(self):
		return self._CxlStsInf

	@CxlStsInf.setter
	def CxlStsInf(self, value):
		self._CxlStsInf = value if type(value) != auto else self.make_default("CxlStsInf")

	@CxlStsInf.deleter
	def CxlStsInf(self):
		del self._CxlStsInf
		self._CxlStsInf = None

	@property
	def IntrmyAgt(self):
		return self._IntrmyAgt

	@IntrmyAgt.setter
	def IntrmyAgt(self, value):
		self._IntrmyAgt = value if type(value) != auto else self.make_default("IntrmyAgt")

	@IntrmyAgt.deleter
	def IntrmyAgt(self):
		del self._IntrmyAgt
		self._IntrmyAgt = None

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if type(value) != auto else self.make_default("VldtnStsInf")

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FincgRqstr', type=PartyIdentificationAndAccount6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstAgt', type=FinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlStsInf', type=CancellationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt', type=FinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=1, max=1, mutex_group=None, array=False),
	))

