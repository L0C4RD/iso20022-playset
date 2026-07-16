# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BranchAndFinancialInstitutionIdentification8
from . import ISODateTime
from . import Max35Text
from . import Party50Choice

class IdentificationAssignment4(base_types._BaseFieldType):

	__slots__ = ["_Assgne", "_Assgnr", "_CreDtTm", "_Cretr", "_FrstAgt", "_MsgId"]
	@property
	def Assgne(self):
		return self._Assgne

	@Assgne.setter
	def Assgne(self, value):
		self._Assgne = value if value is not None else base_types.UninitialisedField(self, 'Assgne', Party50Choice, False)

	@Assgne.deleter
	def Assgne(self):
		del self._Assgne
		self._Assgne = base_types.UninitialisedField(self, 'Assgne', Party50Choice, False)

	@property
	def Assgnr(self):
		return self._Assgnr

	@Assgnr.setter
	def Assgnr(self, value):
		self._Assgnr = value if value is not None else base_types.UninitialisedField(self, 'Assgnr', Party50Choice, False)

	@Assgnr.deleter
	def Assgnr(self):
		del self._Assgnr
		self._Assgnr = base_types.UninitialisedField(self, 'Assgnr', Party50Choice, False)

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
	def Cretr(self):
		return self._Cretr

	@Cretr.setter
	def Cretr(self, value):
		self._Cretr = value if value is not None else base_types.UninitialisedField(self, 'Cretr', Party50Choice, False)

	@Cretr.deleter
	def Cretr(self):
		del self._Cretr
		self._Cretr = base_types.UninitialisedField(self, 'Cretr', Party50Choice, False)

	@property
	def FrstAgt(self):
		return self._FrstAgt

	@FrstAgt.setter
	def FrstAgt(self, value):
		self._FrstAgt = value if value is not None else base_types.UninitialisedField(self, 'FrstAgt', BranchAndFinancialInstitutionIdentification8, False)

	@FrstAgt.deleter
	def FrstAgt(self):
		del self._FrstAgt
		self._FrstAgt = base_types.UninitialisedField(self, 'FrstAgt', BranchAndFinancialInstitutionIdentification8, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Assgne', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Assgnr', type=Party50Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cretr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrstAgt', type=BranchAndFinancialInstitutionIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))