from . import base_types
from ._PartyIdentification272 import PartyIdentification272
from ._LegalOrganisation2 import LegalOrganisation2
from ._TaxParty4 import TaxParty4

class TradeParty6(base_types._BaseFieldType):

	__slots__ = ["_LglOrg", "_TaxPty", "_PtyId"]
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

	_field_defs = frozenset((
		base_types.FieldEntry(name='LglOrg', type=LegalOrganisation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxPty', type=TaxParty4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification272, min=1, max=1, mutex_group=None, array=False),
	))

