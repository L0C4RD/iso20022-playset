from . import base_types
from ._PartyIdentification129Choice import PartyIdentification129Choice
from ._PostalAddress1 import PostalAddress1
from ._ContactIdentification1 import ContactIdentification1

class PartyIdentification289(base_types._BaseFieldType):

	__slots__ = ["_CtctPrsn", "_CtctPrsnAdr", "_PtyId"]
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
	def CtctPrsnAdr(self):
		return self._CtctPrsnAdr

	@CtctPrsnAdr.setter
	def CtctPrsnAdr(self, value):
		self._CtctPrsnAdr = value if type(value) != base_types.auto else self.make_default("CtctPrsnAdr")

	@CtctPrsnAdr.deleter
	def CtctPrsnAdr(self):
		del self._CtctPrsnAdr
		self._CtctPrsnAdr = None

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
		base_types.FieldEntry(name='CtctPrsn', type=ContactIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctPrsnAdr', type=PostalAddress1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PtyId', type=PartyIdentification129Choice, min=1, max=1, mutex_group=None, array=False),
	))

