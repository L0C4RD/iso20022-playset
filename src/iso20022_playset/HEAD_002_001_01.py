import base_types
import PayloadDescription2
import LaxPayload

class HEAD_002_001_01():

	class BusinessFileHeaderV01(base_types._BaseFieldType):

		__slots__ = ["_PyldDesc", "_Pyld"]
		@property
		def PyldDesc(self):
			return self._PyldDesc

		@PyldDesc.setter
		def PyldDesc(self, value):
			self._PyldDesc = value if type(value) != auto else self.make_default("PyldDesc")

		@PyldDesc.deleter
		def PyldDesc(self):
			del self._PyldDesc
			self._PyldDesc = None

		@property
		def Pyld(self):
			return self._Pyld

		@Pyld.setter
		def Pyld(self, value):
			self._Pyld = value if type(value) != auto else self.make_default("Pyld")

		@Pyld.deleter
		def Pyld(self):
			del self._Pyld
			self._Pyld = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PyldDesc', type=PayloadDescription2, min=1, max=1, mutex_group=None, array=False),
			base_types.FieldEntry(name='Pyld', type=LaxPayload, min=0, max=None, mutex_group=None, array=True),
		))

