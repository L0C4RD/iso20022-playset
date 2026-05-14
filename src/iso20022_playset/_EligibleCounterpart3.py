# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._EligibilityIdentification3Choice import EligibilityIdentification3Choice
from ._EligibilityType1Code import EligibilityType1Code
from ._ISODate import ISODate
from ._SystemPartyIdentification2Choice import SystemPartyIdentification2Choice

class EligibleCounterpart3(base_types._BaseFieldType):

	__slots__ = ["_ElgblCntrptId", "_ElgbltyId", "_ElgbltyTp", "_IssrId", "_VldFr", "_VldTo"]
	@property
	def ElgblCntrptId(self):
		return self._ElgblCntrptId

	@ElgblCntrptId.setter
	def ElgblCntrptId(self, value):
		self._ElgblCntrptId = value if type(value) != base_types.auto else self.make_default("ElgblCntrptId")

	@ElgblCntrptId.deleter
	def ElgblCntrptId(self):
		del self._ElgblCntrptId
		self._ElgblCntrptId = None

	@property
	def ElgbltyId(self):
		return self._ElgbltyId

	@ElgbltyId.setter
	def ElgbltyId(self, value):
		self._ElgbltyId = value if type(value) != base_types.auto else self.make_default("ElgbltyId")

	@ElgbltyId.deleter
	def ElgbltyId(self):
		del self._ElgbltyId
		self._ElgbltyId = None

	@property
	def ElgbltyTp(self):
		return self._ElgbltyTp

	@ElgbltyTp.setter
	def ElgbltyTp(self, value):
		self._ElgbltyTp = value if type(value) != base_types.auto else self.make_default("ElgbltyTp")

	@ElgbltyTp.deleter
	def ElgbltyTp(self):
		del self._ElgbltyTp
		self._ElgbltyTp = None

	@property
	def IssrId(self):
		return self._IssrId

	@IssrId.setter
	def IssrId(self, value):
		self._IssrId = value if type(value) != base_types.auto else self.make_default("IssrId")

	@IssrId.deleter
	def IssrId(self):
		del self._IssrId
		self._IssrId = None

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if type(value) != base_types.auto else self.make_default("VldFr")

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = None

	@property
	def VldTo(self):
		return self._VldTo

	@VldTo.setter
	def VldTo(self, value):
		self._VldTo = value if type(value) != base_types.auto else self.make_default("VldTo")

	@VldTo.deleter
	def VldTo(self):
		del self._VldTo
		self._VldTo = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgblCntrptId', type=SystemPartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltyId', type=EligibilityIdentification3Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ElgbltyTp', type=EligibilityType1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IssrId', type=SystemPartyIdentification2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldTo', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))