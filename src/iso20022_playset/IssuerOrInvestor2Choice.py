from . import base_types
from .SystemPartyIdentification2Choice import SystemPartyIdentification2Choice

class IssuerOrInvestor2Choice(base_types._BaseFieldType):

	__slots__ = ["_IssrCSD", "_InvstrCSD"]
	@property
	def IssrCSD(self):
		return self._IssrCSD

	@IssrCSD.setter
	def IssrCSD(self, value):
		self._IssrCSD = value if type(value) != base_types.auto else self.make_default("IssrCSD")

	@IssrCSD.deleter
	def IssrCSD(self):
		del self._IssrCSD
		self._IssrCSD = None

	@property
	def InvstrCSD(self):
		return self._InvstrCSD

	@InvstrCSD.setter
	def InvstrCSD(self, value):
		self._InvstrCSD = value if type(value) != base_types.auto else self.make_default("InvstrCSD")

	@InvstrCSD.deleter
	def InvstrCSD(self):
		del self._InvstrCSD
		self._InvstrCSD = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IssrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='InvstrCSD', type=SystemPartyIdentification2Choice, min=0, max=1, mutex_group=1, array=False),
	))

