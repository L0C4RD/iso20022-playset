import base_types
import PartyIdentification8
import ContactIdentification1

class PartyIdentificationAndContactInformation1(base_types._BaseFieldType):

	__slots__ = ["_PtyId", "_CtctInf"]
	@property
	def PtyId(self):
		return self._PtyId

	@PtyId.setter
	def PtyId(self, value):
		self._PtyId = value if type(value) != auto else self.make_default("PtyId")

	@PtyId.deleter
	def PtyId(self):
		del self._PtyId
		self._PtyId = None

	@property
	def CtctInf(self):
		return self._CtctInf

	@CtctInf.setter
	def CtctInf(self, value):
		self._CtctInf = value if type(value) != auto else self.make_default("CtctInf")

	@CtctInf.deleter
	def CtctInf(self):
		del self._CtctInf
		self._CtctInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PtyId', type=PartyIdentification8, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctInf', type=ContactIdentification1, min=0, max=1, mutex_group=None, array=False),
	))

