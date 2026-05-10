from . import base_types
import Max350Text
import ExternalAuthorityIdentification1Code

class SupervisingAuthorityIdentification1Choice(base_types._BaseFieldType):

	__slots__ = ["_FullNm", "_PrtryId"]
	@property
	def FullNm(self):
		return self._FullNm

	@FullNm.setter
	def FullNm(self, value):
		self._FullNm = value if type(value) != auto else self.make_default("FullNm")

	@FullNm.deleter
	def FullNm(self):
		del self._FullNm
		self._FullNm = None

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FullNm', type=Max350Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=ExternalAuthorityIdentification1Code, min=0, max=1, mutex_group=1, array=False),
	))

