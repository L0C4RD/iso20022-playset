# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import LegalOrganisation1
from . import PartyIdentification43
from . import TaxParty1

class PartyIdentification72(base_types._BaseFieldType):

	__slots__ = ["_LglOrg", "_PtyId", "_TaxPty"]
	@property
	def LglOrg(self):
		return self._LglOrg

	@LglOrg.setter
	def LglOrg(self, value):
		self._LglOrg = value if value is not None else base_types.UninitialisedField(self, 'LglOrg', LegalOrganisation1, False)

	@LglOrg.deleter
	def LglOrg(self):
		del self._LglOrg
		self._LglOrg = base_types.UninitialisedField(self, 'LglOrg', LegalOrganisation1, False)

	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if value is not None else base_types.UninitialisedField(self, 'PtyId', PartyIdentification43, False)

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = base_types.UninitialisedField(self, 'PtyId', PartyIdentification43, False)

	@property
	def TaxPty(self):
		return self._TaxPty

	@TaxPty.setter
	def TaxPty(self, value):
		self._TaxPty = value if value is not None else base_types.UninitialisedField(self, 'TaxPty', TaxParty1, False)

	@TaxPty.deleter
	def TaxPty(self):
		del self._TaxPty
		self._TaxPty = base_types.UninitialisedField(self, 'TaxPty', TaxParty1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LglOrg', type=LegalOrganisation1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification43, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxPty', type=TaxParty1, min=0, max=1, mutex_group=None, array=False),
	))