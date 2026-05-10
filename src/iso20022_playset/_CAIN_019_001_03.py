from . import base_types
from .VerificationResponseV03 import VerificationResponseV03

class CAIN_019_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_VrfctnRspn"]
		@property
		def VrfctnRspn(self):
			return self._VrfctnRspn

		@VrfctnRspn.setter
		def VrfctnRspn(self, value):
			self._VrfctnRspn = value if type(value) != base_types.auto else self.make_default("VrfctnRspn")

		@VrfctnRspn.deleter
		def VrfctnRspn(self):
			del self._VrfctnRspn
			self._VrfctnRspn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='VrfctnRspn', type=VerificationResponseV03, min=1, max=1, mutex_group=None, array=False),
		))

