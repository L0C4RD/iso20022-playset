from . import base_types
from .RedemptionOrderConfirmationV05 import RedemptionOrderConfirmationV05

class SETR_006_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RedOrdrConf"]
		@property
		def RedOrdrConf(self):
			return self._RedOrdrConf

		@RedOrdrConf.setter
		def RedOrdrConf(self, value):
			self._RedOrdrConf = value if type(value) != auto else self.make_default("RedOrdrConf")

		@RedOrdrConf.deleter
		def RedOrdrConf(self):
			del self._RedOrdrConf
			self._RedOrdrConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RedOrdrConf', type=RedemptionOrderConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))

