from . import base_types
import ContactIdentification4
import PartyIdentification2Choice

class ContactPerson1(base_types._BaseFieldType):

	__slots__ = ["_InstnId", "_CtctPrsn"]
	@property
	def InstnId(self):
		return self._InstnId

	@InstnId.setter
	def InstnId(self, value):
		self._InstnId = value if type(value) != auto else self.make_default("InstnId")

	@InstnId.deleter
	def InstnId(self):
		del self._InstnId
		self._InstnId = None

	@property
	def CtctPrsn(self):
		return self._CtctPrsn

	@CtctPrsn.setter
	def CtctPrsn(self, value):
		self._CtctPrsn = value if type(value) != auto else self.make_default("CtctPrsn")

	@CtctPrsn.deleter
	def CtctPrsn(self):
		del self._CtctPrsn
		self._CtctPrsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstnId', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification4, min=1, max=1, mutex_group=None, array=False),
	))

