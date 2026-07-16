# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import EligibilityIdentification3Choice
from . import EligibilityType1Code
from . import ISODate
from . import SystemPartyIdentification2Choice

class EligibleCounterpart3(base_types._BaseFieldType):

	__slots__ = ["_ElgblCntrptId", "_ElgbltyId", "_ElgbltyTp", "_IssrId", "_VldFr", "_VldTo"]
	@property
	def ElgblCntrptId(self):
		return self._ElgblCntrptId

	@ElgblCntrptId.setter
	def ElgblCntrptId(self, value):
		self._ElgblCntrptId = value if value is not None else base_types.UninitialisedField(self, 'ElgblCntrptId', SystemPartyIdentification2Choice, False)

	@ElgblCntrptId.deleter
	def ElgblCntrptId(self):
		del self._ElgblCntrptId
		self._ElgblCntrptId = base_types.UninitialisedField(self, 'ElgblCntrptId', SystemPartyIdentification2Choice, False)

	@property
	def ElgbltyId(self):
		return self._ElgbltyId

	@ElgbltyId.setter
	def ElgbltyId(self, value):
		self._ElgbltyId = value if value is not None else base_types.UninitialisedField(self, 'ElgbltyId', EligibilityIdentification3Choice, False)

	@ElgbltyId.deleter
	def ElgbltyId(self):
		del self._ElgbltyId
		self._ElgbltyId = base_types.UninitialisedField(self, 'ElgbltyId', EligibilityIdentification3Choice, False)

	@property
	def ElgbltyTp(self):
		return self._ElgbltyTp

	@ElgbltyTp.setter
	def ElgbltyTp(self, value):
		self._ElgbltyTp = value if value is not None else base_types.UninitialisedField(self, 'ElgbltyTp', EligibilityType1Code, False)

	@ElgbltyTp.deleter
	def ElgbltyTp(self):
		del self._ElgbltyTp
		self._ElgbltyTp = base_types.UninitialisedField(self, 'ElgbltyTp', EligibilityType1Code, False)

	@property
	def IssrId(self):
		return self._IssrId

	@IssrId.setter
	def IssrId(self, value):
		self._IssrId = value if value is not None else base_types.UninitialisedField(self, 'IssrId', SystemPartyIdentification2Choice, False)

	@IssrId.deleter
	def IssrId(self):
		del self._IssrId
		self._IssrId = base_types.UninitialisedField(self, 'IssrId', SystemPartyIdentification2Choice, False)

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if value is not None else base_types.UninitialisedField(self, 'VldFr', ISODate, False)

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = base_types.UninitialisedField(self, 'VldFr', ISODate, False)

	@property
	def VldTo(self):
		return self._VldTo

	@VldTo.setter
	def VldTo(self, value):
		self._VldTo = value if value is not None else base_types.UninitialisedField(self, 'VldTo', ISODate, False)

	@VldTo.deleter
	def VldTo(self):
		del self._VldTo
		self._VldTo = base_types.UninitialisedField(self, 'VldTo', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgblCntrptId', type=SystemPartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltyId', type=EligibilityIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltyTp', type=EligibilityType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrId', type=SystemPartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldTo', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))