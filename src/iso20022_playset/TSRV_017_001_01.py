from . import base_types
import DemandWithdrawalNotificationV01

class TSRV_017_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_DmndWdrwlNtfctn"]
		@property
		def DmndWdrwlNtfctn(self):
			return self._DmndWdrwlNtfctn

		@DmndWdrwlNtfctn.setter
		def DmndWdrwlNtfctn(self, value):
			self._DmndWdrwlNtfctn = value if type(value) != auto else self.make_default("DmndWdrwlNtfctn")

		@DmndWdrwlNtfctn.deleter
		def DmndWdrwlNtfctn(self):
			del self._DmndWdrwlNtfctn
			self._DmndWdrwlNtfctn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='DmndWdrwlNtfctn', type=DemandWithdrawalNotificationV01, min=1, max=1, mutex_group=None, array=False),
		))

