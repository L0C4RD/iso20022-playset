import base_types
import SubscriptionOrderConfirmationV05

class SETR_012_001_05():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SbcptOrdrConf"]
		@property
		def SbcptOrdrConf(self):
			return self._SbcptOrdrConf

		@SbcptOrdrConf.setter
		def SbcptOrdrConf(self, value):
			self._SbcptOrdrConf = value if type(value) != auto else self.make_default("SbcptOrdrConf")

		@SbcptOrdrConf.deleter
		def SbcptOrdrConf(self):
			del self._SbcptOrdrConf
			self._SbcptOrdrConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SbcptOrdrConf', type=SubscriptionOrderConfirmationV05, min=1, max=1, mutex_group=None, array=False),
		))

