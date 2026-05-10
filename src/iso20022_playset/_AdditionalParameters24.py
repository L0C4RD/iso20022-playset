from . import base_types
from ._Max35Text import Max35Text
from ._PartialSettlement2Code import PartialSettlement2Code
from ._PreConfirmation1Code import PreConfirmation1Code

class AdditionalParameters24(base_types._BaseFieldType):

	__slots__ = ["_PreConf", "_PrtlSttlm", "_PrvsPrtlConfId"]
	@property
	def PreConf(self):
		return self._PreConf

	@PreConf.setter
	def PreConf(self, value):
		self._PreConf = value if type(value) != base_types.auto else self.make_default("PreConf")

	@PreConf.deleter
	def PreConf(self):
		del self._PreConf
		self._PreConf = None

	@property
	def PrtlSttlm(self):
		return self._PrtlSttlm

	@PrtlSttlm.setter
	def PrtlSttlm(self, value):
		self._PrtlSttlm = value if type(value) != base_types.auto else self.make_default("PrtlSttlm")

	@PrtlSttlm.deleter
	def PrtlSttlm(self):
		del self._PrtlSttlm
		self._PrtlSttlm = None

	@property
	def PrvsPrtlConfId(self):
		return self._PrvsPrtlConfId

	@PrvsPrtlConfId.setter
	def PrvsPrtlConfId(self, value):
		self._PrvsPrtlConfId = value if type(value) != base_types.auto else self.make_default("PrvsPrtlConfId")

	@PrvsPrtlConfId.deleter
	def PrvsPrtlConfId(self):
		del self._PrvsPrtlConfId
		self._PrvsPrtlConfId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PreConf', type=PreConfirmation1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtlSttlm', type=PartialSettlement2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsPrtlConfId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

