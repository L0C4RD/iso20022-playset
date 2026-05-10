from . import base_types
from ._SwitchOrderConfirmationV04 import SwitchOrderConfirmationV04

class SETR_015_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SwtchOrdrConf"]
		@property
		def SwtchOrdrConf(self):
			return self._SwtchOrdrConf

		@SwtchOrdrConf.setter
		def SwtchOrdrConf(self, value):
			self._SwtchOrdrConf = value if type(value) != base_types.auto else self.make_default("SwtchOrdrConf")

		@SwtchOrdrConf.deleter
		def SwtchOrdrConf(self):
			del self._SwtchOrdrConf
			self._SwtchOrdrConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SwtchOrdrConf', type=SwitchOrderConfirmationV04, min=1, max=1, mutex_group=None, array=False),
		))

