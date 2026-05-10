from . import base_types
import AmendmentV03

class CAIN_020_001_03():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_Amdmnt"]
		@property
		def Amdmnt(self):
			return self._Amdmnt

		@Amdmnt.setter
		def Amdmnt(self, value):
			self._Amdmnt = value if type(value) != auto else self.make_default("Amdmnt")

		@Amdmnt.deleter
		def Amdmnt(self):
			del self._Amdmnt
			self._Amdmnt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='Amdmnt', type=AmendmentV03, min=1, max=1, mutex_group=None, array=False),
		))

