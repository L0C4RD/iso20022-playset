from . import base_types
import ModifyReservationV07

class CAMT_048_001_07():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_ModfyRsvatn"]
		@property
		def ModfyRsvatn(self):
			return self._ModfyRsvatn

		@ModfyRsvatn.setter
		def ModfyRsvatn(self, value):
			self._ModfyRsvatn = value if type(value) != auto else self.make_default("ModfyRsvatn")

		@ModfyRsvatn.deleter
		def ModfyRsvatn(self):
			del self._ModfyRsvatn
			self._ModfyRsvatn = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='ModfyRsvatn', type=ModifyReservationV07, min=1, max=1, mutex_group=None, array=False),
		))

