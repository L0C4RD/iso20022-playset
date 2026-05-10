from . import base_types
from .GenericIdentification30 import GenericIdentification30
from .AgreementFramework1Code import AgreementFramework1Code

class AgreementFramework1Choice(base_types._BaseFieldType):

	__slots__ = ["_AgrmtFrmwk", "_PrtryId"]
	@property
	def AgrmtFrmwk(self):
		return self._AgrmtFrmwk

	@AgrmtFrmwk.setter
	def AgrmtFrmwk(self, value):
		self._AgrmtFrmwk = value if type(value) != base_types.auto else self.make_default("AgrmtFrmwk")

	@AgrmtFrmwk.deleter
	def AgrmtFrmwk(self):
		del self._AgrmtFrmwk
		self._AgrmtFrmwk = None

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if type(value) != base_types.auto else self.make_default("PrtryId")

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrmtFrmwk', type=AgreementFramework1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))

