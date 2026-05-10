from . import base_types
from ._AcceptorConfigurationUpdateV14 import AcceptorConfigurationUpdateV14

class CATM_003_001_14():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_AccptrCfgtnUpd"]
		@property
		def AccptrCfgtnUpd(self):
			return self._AccptrCfgtnUpd

		@AccptrCfgtnUpd.setter
		def AccptrCfgtnUpd(self, value):
			self._AccptrCfgtnUpd = value if type(value) != base_types.auto else self.make_default("AccptrCfgtnUpd")

		@AccptrCfgtnUpd.deleter
		def AccptrCfgtnUpd(self):
			del self._AccptrCfgtnUpd
			self._AccptrCfgtnUpd = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='AccptrCfgtnUpd', type=AcceptorConfigurationUpdateV14, min=1, max=1, mutex_group=None, array=False),
		))

