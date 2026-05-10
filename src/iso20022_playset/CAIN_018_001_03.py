from . import base_types
from .VerificationInitiationV03 import VerificationInitiationV03

class CAIN_018_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_VrfctnInitn"]
		@property
		def VrfctnInitn(self):
			return self._VrfctnInitn

		@VrfctnInitn.setter
		def VrfctnInitn(self, value):
			self._VrfctnInitn = value if type(value) != base_types.auto else self.make_default("VrfctnInitn")

		@VrfctnInitn.deleter
		def VrfctnInitn(self):
			del self._VrfctnInitn
			self._VrfctnInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='VrfctnInitn', type=VerificationInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))

