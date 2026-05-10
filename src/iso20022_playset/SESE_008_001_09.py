from . import base_types
from .ReversalOfTransferInConfirmationV09 import ReversalOfTransferInConfirmationV09

class SESE_008_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RvslOfTrfInConf"]
		@property
		def RvslOfTrfInConf(self):
			return self._RvslOfTrfInConf

		@RvslOfTrfInConf.setter
		def RvslOfTrfInConf(self, value):
			self._RvslOfTrfInConf = value if type(value) != auto else self.make_default("RvslOfTrfInConf")

		@RvslOfTrfInConf.deleter
		def RvslOfTrfInConf(self):
			del self._RvslOfTrfInConf
			self._RvslOfTrfInConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RvslOfTrfInConf', type=ReversalOfTransferInConfirmationV09, min=1, max=1, mutex_group=None, array=False),
		))

