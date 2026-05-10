from . import base_types
from .SubscriptionBulkOrderConfirmationV04 import SubscriptionBulkOrderConfirmationV04

class SETR_009_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SbcptBlkOrdrConf"]
		@property
		def SbcptBlkOrdrConf(self):
			return self._SbcptBlkOrdrConf

		@SbcptBlkOrdrConf.setter
		def SbcptBlkOrdrConf(self, value):
			self._SbcptBlkOrdrConf = value if type(value) != auto else self.make_default("SbcptBlkOrdrConf")

		@SbcptBlkOrdrConf.deleter
		def SbcptBlkOrdrConf(self):
			del self._SbcptBlkOrdrConf
			self._SbcptBlkOrdrConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptBlkOrdrConf', type=SubscriptionBulkOrderConfirmationV04, min=1, max=1, mutex_group=None, array=False),
		))

