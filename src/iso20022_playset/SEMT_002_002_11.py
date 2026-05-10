from . import base_types
import SecuritiesBalanceCustodyReport002V11

class SEMT_002_002_11():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_SctiesBalCtdyRpt"]
		@property
		def SctiesBalCtdyRpt(self):
			return self._SctiesBalCtdyRpt

		@SctiesBalCtdyRpt.setter
		def SctiesBalCtdyRpt(self, value):
			self._SctiesBalCtdyRpt = value if type(value) != auto else self.make_default("SctiesBalCtdyRpt")

		@SctiesBalCtdyRpt.deleter
		def SctiesBalCtdyRpt(self):
			del self._SctiesBalCtdyRpt
			self._SctiesBalCtdyRpt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='SctiesBalCtdyRpt', type=SecuritiesBalanceCustodyReport002V11, min=1, max=1, mutex_group=None, array=False),
		))

