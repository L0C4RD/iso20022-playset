import base_types
import ReturnLimitV09

class CAMT_010_001_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_RtrLmt"]
		@property
		def RtrLmt(self):
			return self._RtrLmt

		@RtrLmt.setter
		def RtrLmt(self, value):
			self._RtrLmt = value if type(value) != auto else self.make_default("RtrLmt")

		@RtrLmt.deleter
		def RtrLmt(self):
			del self._RtrLmt
			self._RtrLmt = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='RtrLmt', type=ReturnLimitV09, min=1, max=1, mutex_group=None, array=False),
		))

