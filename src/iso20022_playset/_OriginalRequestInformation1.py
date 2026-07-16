# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CancellationStatusInformation1
from . import FinancialInstitutionIdentification6
from . import ISODateTime
from . import Max35Text
from . import PartyIdentificationAndAccount6
from . import ValidationStatusInformation1

class OriginalRequestInformation1(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_CxlStsInf", "_FincgRqstr", "_FrstAgt", "_Id", "_IntrmyAgt", "_VldtnStsInf"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def CxlStsInf(self):
		return self._CxlStsInf

	@CxlStsInf.setter
	def CxlStsInf(self, value):
		self._CxlStsInf = value if value is not None else base_types.UninitialisedField(self, 'CxlStsInf', CancellationStatusInformation1, False)

	@CxlStsInf.deleter
	def CxlStsInf(self):
		del self._CxlStsInf
		self._CxlStsInf = base_types.UninitialisedField(self, 'CxlStsInf', CancellationStatusInformation1, False)

	@property
	def FincgRqstr(self):
		return self._FincgRqstr

	@FincgRqstr.setter
	def FincgRqstr(self, value):
		self._FincgRqstr = value if value is not None else base_types.UninitialisedField(self, 'FincgRqstr', PartyIdentificationAndAccount6, False)

	@FincgRqstr.deleter
	def FincgRqstr(self):
		del self._FincgRqstr
		self._FincgRqstr = base_types.UninitialisedField(self, 'FincgRqstr', PartyIdentificationAndAccount6, False)

	@property
	def FrstAgt(self):
		return self._FrstAgt

	@FrstAgt.setter
	def FrstAgt(self, value):
		self._FrstAgt = value if value is not None else base_types.UninitialisedField(self, 'FrstAgt', FinancialInstitutionIdentification6, False)

	@FrstAgt.deleter
	def FrstAgt(self):
		del self._FrstAgt
		self._FrstAgt = base_types.UninitialisedField(self, 'FrstAgt', FinancialInstitutionIdentification6, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', Max35Text, False)

	@property
	def IntrmyAgt(self):
		return self._IntrmyAgt

	@IntrmyAgt.setter
	def IntrmyAgt(self, value):
		self._IntrmyAgt = value if value is not None else base_types.UninitialisedField(self, 'IntrmyAgt', FinancialInstitutionIdentification6, False)

	@IntrmyAgt.deleter
	def IntrmyAgt(self):
		del self._IntrmyAgt
		self._IntrmyAgt = base_types.UninitialisedField(self, 'IntrmyAgt', FinancialInstitutionIdentification6, False)

	@property
	def VldtnStsInf(self):
		return self._VldtnStsInf

	@VldtnStsInf.setter
	def VldtnStsInf(self, value):
		self._VldtnStsInf = value if value is not None else base_types.UninitialisedField(self, 'VldtnStsInf', ValidationStatusInformation1, False)

	@VldtnStsInf.deleter
	def VldtnStsInf(self):
		del self._VldtnStsInf
		self._VldtnStsInf = base_types.UninitialisedField(self, 'VldtnStsInf', ValidationStatusInformation1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CxlStsInf', type=CancellationStatusInformation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FincgRqstr', type=PartyIdentificationAndAccount6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstAgt', type=FinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrmyAgt', type=FinancialInstitutionIdentification6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldtnStsInf', type=ValidationStatusInformation1, min=1, max=1, mutex_group=None, array=False),
	))