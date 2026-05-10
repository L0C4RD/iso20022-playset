from . import base_types
from .ATMDeviceControlV04 import ATMDeviceControlV04

class CAAM_002_001_04():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ATMDvcCtrl"]
		@property
		def ATMDvcCtrl(self):
			return self._ATMDvcCtrl

		@ATMDvcCtrl.setter
		def ATMDvcCtrl(self, value):
			self._ATMDvcCtrl = value if type(value) != base_types.auto else self.make_default("ATMDvcCtrl")

		@ATMDvcCtrl.deleter
		def ATMDvcCtrl(self):
			del self._ATMDvcCtrl
			self._ATMDvcCtrl = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ATMDvcCtrl', type=ATMDeviceControlV04, min=1, max=1, mutex_group=None, array=False),
		))

