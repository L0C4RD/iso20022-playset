from . import base_types
from .LegalOrganisation1 import LegalOrganisation1
from .OrganisationIdentification28 import OrganisationIdentification28
from .TaxParty1 import TaxParty1

class PartyIdentification116(base_types._BaseFieldType):

	__slots__ = ["_TaxPty", "_PtyId", "_LglOrg"]
	@property
	def TaxPty(self):
		return self._TaxPty

	@TaxPty.setter
	def TaxPty(self, value):
		self._TaxPty = value if type(value) != base_types.auto else self.make_default("TaxPty")

	@TaxPty.deleter
	def TaxPty(self):
		del self._TaxPty
		self._TaxPty = None

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != base_types.auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def LglOrg(self):
		return self._LglOrg

	@LglOrg.setter
	def LglOrg(self, value):
		self._LglOrg = value if type(value) != base_types.auto else self.make_default("LglOrg")

	@LglOrg.deleter
	def LglOrg(self):
		del self._LglOrg
		self._LglOrg = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxPty', type=TaxParty1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=OrganisationIdentification28, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LglOrg', type=LegalOrganisation1, min=0, max=1, mutex_group=None, array=False),
	))

