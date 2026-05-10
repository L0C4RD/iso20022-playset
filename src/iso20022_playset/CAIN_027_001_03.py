from . import base_types
from .ChargeBackInitiationV03 import ChargeBackInitiationV03

class CAIN_027_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ChrgBckInitn"]
		@property
		def ChrgBckInitn(self):
			return self._ChrgBckInitn

		@ChrgBckInitn.setter
		def ChrgBckInitn(self, value):
			self._ChrgBckInitn = value if type(value) != auto else self.make_default("ChrgBckInitn")

		@ChrgBckInitn.deleter
		def ChrgBckInitn(self):
			del self._ChrgBckInitn
			self._ChrgBckInitn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ChrgBckInitn', type=ChargeBackInitiationV03, min=1, max=1, mutex_group=None, array=False),
		))

