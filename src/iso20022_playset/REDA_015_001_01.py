import base_types
import PartyQueryV01

class REDA_015_001_01():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_PtyQry"]
		@property
		def PtyQry(self):
			return self._PtyQry

		@PtyQry.setter
		def PtyQry(self, value):
			self._PtyQry = value if type(value) != auto else self.make_default("PtyQry")

		@PtyQry.deleter
		def PtyQry(self):
			del self._PtyQry
			self._PtyQry = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='PtyQry', type=PartyQueryV01, min=1, max=1, mutex_group=None, array=False),
		))

