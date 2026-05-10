from . import base_types
from .PortfolioTransferConfirmationV11 import PortfolioTransferConfirmationV11

class SESE_013_001_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PrtflTrfConf"]
		@property
		def PrtflTrfConf(self):
			return self._PrtflTrfConf

		@PrtflTrfConf.setter
		def PrtflTrfConf(self, value):
			self._PrtflTrfConf = value if type(value) != base_types.auto else self.make_default("PrtflTrfConf")

		@PrtflTrfConf.deleter
		def PrtflTrfConf(self):
			del self._PrtflTrfConf
			self._PrtflTrfConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PrtflTrfConf', type=PortfolioTransferConfirmationV11, min=1, max=1, mutex_group=None, array=False),
		))

