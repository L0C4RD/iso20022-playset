# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import SystemPartyIdentification2Choice

class IssuerOrInvestor2Choice(base_types._BaseFieldType):

	__slots__ = ["_InvstrCSD", "_IssrCSD"]
	@property
	def InvstrCSD(self):
		return self._InvstrCSD

	@InvstrCSD.setter
	def InvstrCSD(self, value):
		self._InvstrCSD = value if value is not None else base_types.UninitialisedField(self, 'InvstrCSD', SystemPartyIdentification2Choice, False)

	@InvstrCSD.deleter
	def InvstrCSD(self):
		del self._InvstrCSD
		self._InvstrCSD = base_types.UninitialisedField(self, 'InvstrCSD', SystemPartyIdentification2Choice, False)

	@property
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if value is not None else base_types.UninitialisedField(self, 'IssrCSD', SystemPartyIdentification2Choice, False)

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = base_types.UninitialisedField(self, 'IssrCSD', SystemPartyIdentification2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='IssrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=1, array=False),
	))