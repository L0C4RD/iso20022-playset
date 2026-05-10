from . import base_types
from ._ContactIdentification4 import ContactIdentification4
from ._PartyIdentification2Choice import PartyIdentification2Choice

class ContactPerson1(base_types._BaseFieldType):

	__slots__ = ["_InstnId", "_CtctPrsn"]
	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if type(value) != base_types.auto else self.make_default("CtctPrsn")

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = None

	@property
	def InstnId(self):
		return self._InstnId

	@InstnId.setter
	def InstnId(self, value):
		self._InstnId = value if type(value) != base_types.auto else self.make_default("InstnId")

	@InstnId.deleter
	def InstnId(self):
		del self._InstnId
		self._InstnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstnId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
	))

